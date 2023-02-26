const token = ["RGAPI-ca6d04f3-288c-484f-9dab-da85f6b6f18b", "RGAPI-b7161626-d453-4cfe-8443-e0802fb3342a"]
var t = 0;
/*var myHeaders = new Headers();
myHeaders.append("X-Riot-Token", token[t]);*/


//let summonerName = require('/Users/mvpst/OneDrive/Documentos/HACK3/users.json');
let summonerName = "Mark003";

var requestOptions = {
  method: 'GET',
  headers: {"X-Riot-Token": token[t]},
  redirect: 'follow'
};

const fs = require("fs");
let matches = [];


//Travels the name of user names taken from the example of the drive
for (var u in summonerName){

  //First request - find the user data from the name
  fetch(`https://eun1.api.riotgames.com/tft/summoner/v1/summoners/by-name/${summonerName}`, requestOptions)
    .then(response => response.text(),
      console.log("arroz"))
    .then(
      function(rawUser) {
        var resultUser = JSON.parse(rawUser);
        console.log("what");
        
        var puuid = resultUser.puuid;
        
        /*if (puuid == undefined){
          console.log("summoner name: ", summonerName[u]);
        }else{
          console.log(puuid);
        }*/
        //Second Request - find the matches from each Puuid (one of the users id)
        fetch(`https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/${puuid}/ids?start=0&count=2`, requestOptions)
        .then(response => response.text())
        .then(
          function(rawMatchesID) {
            var resultMatches = JSON.parse(rawMatchesID);
            console.log("vei");
            console.log(token[t]);
            //var aux = 0;            

            //Third Request - find the matches by the ID
            for (var i in resultMatches){
              fetch(`https://europe.api.riotgames.com/lol/match/v5/matches/${resultMatches[i]}`, requestOptions)
              .then(response => response.text())
              .then(
                function(rawMatches) {
                  var result = JSON.parse(rawMatches);  
                  //matches.push(result)

                  fs.writeFile("matches_test.json", JSON.stringify(result), err => {
  
                    // Checking for errors
                    if (err) throw err; 
                  
                    console.log("Done writing"); // Success
                  });
              
                }
              )
              .catch(error => console.log('error 3', error));
            }
            
          }
        )
        .catch(error => console.log('error 2', error));
      }
    )
    .catch(error => console.log('error 1', error));
}

/*                  if (aux >= 17){
                    aux=0;
                    if (t>1){
                      t=0;
                    }
                    requestOptions = {
                      method: 'GET',
                      headers: {"X-Riot-Token": token[t]},
                      redirect: 'follow'
                    };
                    
                  }else{
                    aux++;
                    if(t>1){
                      t=0;
                    }
                    t++;
                  } */