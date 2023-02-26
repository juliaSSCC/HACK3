from Classes import *
import pymongo
from pymongo.collection import Collection
from pymongo.cursor import Cursor


def get_player_data(participant_data:dict) -> PlayerMatchData:
    player =PlayerMatchData()
    player.assist(participant_data["assists"])
    player.character(participant_data["championName"])
    player.damage_dealt(participant_data["totalDamageDealt"])
    player.damage_taken(participant_data["totalDamageTaken"])
    player.death(participant_data["deaths"])
    player.id(participant_data["puuid"])
    player.kills1(participant_data["kills"])
    player.kills2(participant_data["doubleKills"])
    player.kills3(participant_data["tripleKills"])
    player.kills4(participant_data["quadraKills"])
    player.kills5(participant_data["pentaKills"])
    player.pos(participant_data["teamPosition"])
    player.money(participant_data["goldEarned"])
    player.role(participant_data["role"])
    player.lane(participant_data["lane"])
    player.farm(participant_data["totalMinionsKilled"])
    player.heal_t(participant_data["totalHeal"])
    player.heal_p(participant_data["totalHealsOnTeammates"])
    player.team(participant_data["teamId"])
    player.win(participant_data["win"])
    player.name(participant_data["summonerName"])
    return player

def parse_lol_match_data(match_json:dict)->MatchData:
    game_type:GameType=GameType.LOL
    match_id=match_json["details"]["metadata"]["matchId"]
    players:list[PlayerMatchData]=[]
    match_mode:str=match_json["details"]["info"]["gameMode"]
    date=int(match_json["details"]["info"]["gameCreation"])
    #print(type(date))
    #print(int(date))
    for player in match_json["details"]["info"]["participants"]:
        player_data=get_player_data(player)
        #print(f"{calculate_player_score(player_data):10.3f}")
        player_data.score(calculate_player_score(player_data))
        player_data.match(match_id)
        players.append(player_data)
        #print(player_data.to_dict())
        
    return MatchData().game_type(game_type).match_id(match_id).match_mode(match_mode).players(players).date(date)
    
def calculate_player_score(pd:PlayerMatchData):
    assist_modfier=1
    PPA=25
    kills_modfier=1
    PPK=100
    damage_modfier=1
    PPD=1
    farm_modfier=1
    PPF=0.5
    gold_modfier=1
    PPG=2
    win_modfier=1.25 if pd.won_match else 0.75
    modfiers=[assist_modfier,kills_modfier,damage_modfier,farm_modfier,gold_modfier]
    assist_score=assist_modfier*PPA*pd.assists
    kills_score=kills_modfier*PPK*pd.kills
    damage_score=damage_modfier*PPD*pd.total_damage_dealt
    farm_score=farm_modfier*PPF*pd.minions_farmed
    gold_score=gold_modfier*PPG*pd.money_spent
    
    score=sum([assist_score,kills_score,damage_score,farm_score,gold_score])
    score=score*win_modfier/(sum(modfiers)/ len(modfiers))
    return score
    
def parse_player_data(pd:PlayerMatchData)->PlayerStatistics:
    ps=PlayerStatistics().deaths(pd.deaths).assists(pd.assists).kills(pd.kills)
    ps.name(pd.player).money(pd.money_spent).update_history(pd).id(pd.puuid)
    
    return ps

def add_statistics_to_leaderboard(ps:PlayerStatistics,board:Collection)->None:
    
    puuid=ps.puuid
    res=board.find_one({"puuid":puuid})
    if res is not None:
        old_ps=PlayerStatistics(res)
        old_ps.update_history(ps.history[0])
        board.replace_one({"puuid":puuid},old_ps.to_dict())
    #if ps(ps.puuid) in board -> board[ps].update_history(ps.history[0])
    #else board.append(ps)
    else:
        board.insert_one(ps.to_dict())
    return

def add_player_to_queue(ps:PlayerStatistics):
    p=Player(ps.puuid,ps.ELO_rating,ps.main_position)
    MatchmakingQueue.add_player(p)
    
def populate_leaderboard(matches:Cursor,board:Collection):
    for el in matches:
        md=parse_lol_match_data(el)
        for p in md._players:
            ps=parse_player_data(p)
            add_statistics_to_leaderboard(ps,board)
        pass

def create_pool(board:Collection):
    players=board.find({})
    for p in players:
        ps=PlayerStatistics(p)
        add_player_to_queue(ps)
    pass

def create_n_parties(n):
    for _ in range(n):
        p=Party()

def create_n_matches(n):
    for _ in range(n):
        m=Match()