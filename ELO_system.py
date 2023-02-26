import data_parser
import pymongo
from pymongo.collection import Collection


client=pymongo.MongoClient('mongodb://4.tcp.eu.ngrok.io:18012/')
db=client.teste
col=db.col1
board=db["leaderboard"]

matches=col.find({})

data_parser.create_pool(board)
data_parser.create_n_parties(10)
data_parser.create_n_matches(1)



