//Since we don't have access to the full API, we used the drive file to filter and get the names to start the API calling process
const fs = require("fs");

let summonerName = new Set();

let json = require('Data/lolMatch.json');

for (var i=0 in json) {
  let users = json[i].details.info.participants
  for (var z=0 in users) {
    summonerName.add(users[z].summonerName)
  
  }
}

const myArray = Array.from(summonerName);
console.log(myArray.length);

fs.writeFile("users.json", JSON.stringify(myArray), err => {
     
  // Checking for errors
  if (err) throw err; 
 
  console.log("Done writing"); // Success
});