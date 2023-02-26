from flask import Flask, render_template, request
from pymongo import MongoClient
from pprint import pprint
from datetime import datetime,timezone
import data_parser

app = Flask(__name__)

client = MongoClient('mongodb://192.168.1.145:27017/')
db=client.teste
storage = db.storage
board=db["leaderboard"]
queue_db=db["queue"]
#storage.drop()
#exit()

def database_new_entry(new_result):

            global storage
            if storage.find({'Name': new_result['Name'] }).count() > 0:
                  avaliability_flag=True
                  print('Trying to overwrite issue')
                  exit()

            
            student_details = {
                  'Name': new_result['Name'],
                  'grds': new_result
            }
            
            entry_status = storage.insert_one(student_details)
            return entry_status

def database_update_entry(key_val,new_result):
            global storage
            entry_status = storage.update_one(
                  {'Name':key_val},
                  {
                        "$set": {'grds':new_result}
                  }
            )
            print('inside database_update_entry', key_val, new_result)
            return entry_status


def filter_date(start, end):
    global board
    date_filter={
    'history.date': {
        '$gte': datetime(2021, 10, 23, 13, 41, 2, tzinfo=timezone.utc), 
        '$lte': datetime(2021, 10, 23, 14, 28, 8, tzinfo=timezone.utc)
        }
    }
    return board.find(date_filter)


data={}
#data['Headings']=
@app.route('/')
def student():
   return render_template('student.html')

@app.route('/leaderboard')
def leaderboard():
    print("Into full list===========")
    global data
    tl=['  Summoner Name  ','  ELO  ','  Position  ','  Main  ','Wins','Games played', 'KDA', 'gold acquired']
    global board

    mod_dict={}
    for document in board.find():
        new_document={}
        new_document['summoner_name']=document['summoner_name']
        new_document['ELO']=int(document['ELO'])
        new_document['position']=document['position']
        new_document['main']=document['main']
        new_document['wins']=document['wins']
        new_document['games']=document['games']
        new_document['KDA']=f"{document['kills']}/{document['deaths']}/{document['assists']}"
        new_document['gold']=document['gold']
        
        mod_dict[document['summoner_name']]=new_document
    return render_template('leaderboard.html',dict=mod_dict,headings=tl)

@app.route('/queue/add_all')
def add_all_to_queue():
    global queue_db
    global board
    data_parser.create_pool(board,queue_db)
    print("added")
    queue_obj=queue_db.find_one()
    on_queue=queue_obj["players"]
    l=[]
    h=["Name","Elo","Position"]
    for el in on_queue:
        name=board.find_one({"puuid":el["puuid"]})["summoner_name"]
        d={
            "name":name,
            "elo": el["elo"],
            "position":el["position"],
        }
        l.append(d)
    return render_template("queue.html",player_queue=l,old_result={},dict={},heading=h)

@app.route('/queue/remove_all')
def remove_all_to_queue():
    h=["Name","Elo","Position"]
    global queue_db
    global board
    data_parser.clean_queue(queue_db)
    print("cleaning")
    return render_template("queue.html",player_queue=[],old_result={},dict={},heading=h)


@app.route('/queue/create_match')
def create_match():
    global queue_db
    global board
    data_parser.create_n_matches(1,queue_db)
    queue_obj=queue_db.find_one()
    on_queue=queue_obj["players"]
    p=queue_obj["parties"]
    m=queue_obj['matches']
    l=[]
    h=["Name","Elo","Position"]
    print(bt)
    bt=m[0]['parties'][0]
    rt=m[0]['parties'][1]
    for el in on_queue:
        name=board.find_one({"puuid":el["puuid"]})["summoner_name"]
        d={
            "name":name,
            "elo": el["elo"],
            "position":el["position"],
        }
        l.append(d)
    return  render_template("queue.html",player_queue=l,red_team=rt,blue_team=bt,parties=p,heading=h)

@app.route('/queue/create_party')
def create_party():
    global queue_db
    global board
    data_parser.create_n_parties(1,queue_db)
    queue_obj=queue_db.find_one()
    on_queue=queue_obj["players"]
    p=queue_obj["parties"]
    l=[]
    h=["Name","Elo","Position"]
    for el in on_queue:
        name=board.find_one({"puuid":el["puuid"]})["summoner_name"]
        d={
            "name":name,
            "elo": el["elo"],
            "position":el["position"],
        }
        l.append(d)
    
        
    
    return  render_template("queue.html",player_queue=l,red_team=[],blue_team=[],parties=p,heading=h)

@app.route('/queue')
def queue():
    
    return render_template('queue.html',player_queue=[],red_team=[],blue_team=[],parties=[])

@app.route('/player/<string:iname>',methods=['GET'])
def player(iname):
    global board
    query_result=board.find_one({'summoner_name':iname})
    print("result")
    pprint(query_result)
    return render_template('player.html',sname=iname,obj=query_result)
    pass


if __name__ == '__main__':
    app.jinja_env.add_extension('jinja2.ext.loopcontrols')
    app.run(debug = True)