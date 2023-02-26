import { MongoClient } from 'mongodb';
var url = "mongodb://4.tcp.eu.ngrok.io:18012/";

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("matches");
  var myobj = require('/Users/mvpst/OneDrive/Documentos/HACK3/matches_test.json');
  dbo.collection("matches").insertOne(myobj, function(err, res) {
    if (err) throw err;
    console.log("1 document inserted");
    db.close();
  });
});