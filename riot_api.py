from riotwatcher import LolWatcher
import pymongo

client=pymongo.MongoClient('mongodb://4.tcp.eu.ngrok.io:18012/')
db=client.teste
raw=db.raw

# golbal variables
api_key = 'RGAPI-ca6d04f3-288c-484f-9dab-da85f6b6f18b'
watcher = LolWatcher(api_key)
my_region = 'EUN1'

#my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])
names=["Naqpenda","Mark003",]
data=[]
for name in names:
    user=watcher.summoner.by_name(my_region, name)
    #print(user)
    matches=watcher.match.matchlist_by_puuid(my_region, user['puuid'])
    print(matches)
    for m in matches:
        details=watcher.match.by_id(my_region, m)
        data.append(details)
        raw.insert_one(details)
        
print(data)
