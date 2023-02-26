from enum import IntEnum
from datetime import datetime
import uuid

class PlayerMatchData:   
    def obj(self):
        return self 
    def to_dict(self)->dict:
        d={
            "assists":self.assists,
            "character_name":self.character_name,
            "total_damage_dealt":self.total_damage_dealt,
            "damage_taken":self._damage_taken,
            "deaths":self.deaths,
            "double_kills":self.double_kills,
            "triple_kills":self.triple_kills,
            "quadra_kills":self.quadra_kills,
            "penta_kills":self.penta_kills,
            "position":self.position,
            "money_spent":self.money_spent,
            "main_role":self.main_role,
            "minions_farmed":self.minions_farmed,
            "heal_taken":self.heal_taken,
            "heal_performed":self.heal_performed,
            "puuid":self.puuid,
            "team_id":self.team_id,
            "won_match":self.won_match,
            "lane":self._lane,
            "kills":self.kills,
            "score": self.battle_score,
            "match_id":self.match_id,
            "summoner_name":self.player, 
        }
        return d
    
    def load(self,data:dict):
        self.assists = data["assists"]
        self.character_name = data["character_name"]
        self.total_damage_dealt = data["total_damage_dealt"]
        self._damage_taken = data["damage_taken"]
        self.deaths = data["deaths"]
        self.double_kills = data["double_kills"]
        self.triple_kills = data["triple_kills"]
        self.quadra_kills = data["quadra_kills"]
        self.penta_kills = data["penta_kills"]
        self.position = data["position"]
        self.money_spent = data["money_spent"]
        self.main_role = data["main_role"]
        self.minions_farmed = data["minions_farmed"]
        self.heal_taken = data["heal_taken"]
        self.heal_performed = data["heal_performed"]
        self.puuid = data["puuid"]
        self.team_id = data["team_id"]
        self.won_match = data["won_match"]
        self._lane = data["lane"]
        self.kills = data["kills"]
        self.battle_score = data["score"]
        self.match_id = data["match_id"]
        self.player = data["summoner_name"] 
    
    def __repr__(self) -> str:
        return f"player {self.puuid}"
        pass
    
    def __init__(self,data:dict=None) -> None:
        self.assists:int=None
        self.character_name:str=None
        self.total_damage_dealt:int=None
        self._damage_taken:int=None
        self.deaths:int=None
        self.double_kills:int=None
        self.triple_kills:int=None
        self.quadra_kills:int=None
        self.penta_kills:int=None
        self.position:str=None
        self.money_spent:int=None
        self.main_role:str=None
        self.minions_farmed:int=None
        self.heal_taken:int=None
        self.heal_performed:int=None
        self.puuid:str=None
        self.team_id:int=None
        self.won_match:bool=None
        self._lane:str=None
        self.kills:int=None
        self.battle_score:int=None
        self.match_id:str=None
        self.player:str=None
        if (data is not None):
            self.load(data)
        
        return
    
    def assist(self,v:int):
        self.assists=v
        return self
    
    def character(self,v:str):
        self.character_name=v
        return self
    
    def damage_dealt(self,v:int):
        self.total_damage_dealt=v
        return self
    
    def damage_taken(self,v:int):
        self._damage_taken=v
        return self
    
    def death(self,v:int):
        self.deaths=v
        return self
    def kills1(self,v:int):
        self.kills=v
    def kills2(self,v:int):
        self.double_kills=v
        return self
    
    def kills3(self,v:int):
        self.triple_kills=v
        return self
    
    def kills4(self,v:int):
        self.quadra_kills=v
        return self
    def kills5(self, v:int):
        self.penta_kills=v
        return self
    def pos(self,v:str):
        self.position=v
        return self
    def money(self,v:int):
        self.money_spent=v
        return self
    def role(self,v:str):
        self.main_role=v
        return self
    def farm(self,v:int):
        self.minions_farmed=v
        return self
    def heal_t(self,v:int):
        self.heal_taken=v
        return self
    def heal_p(self,v:int):
        self.heal_performed=v
        return self
    def id(self,v:str):
        self.puuid=v
        return self
    def team(self,v:int):
        self.team_id=v
        return self
    def win(self,v:bool):
        self.won_match=v
        return self
    def lane(self,v:str):
        self._lane=v
    def score(self,v:int):
        self.battle_score=v
        return self
    def match(self,v:str):
        self.match_id=v
        return self
    def name(self,v:str):
        self.player=v
        return self

    
class PlayerStatistics:
    #TODO: improve to update based on the new entry
    def to_dict(self)->dict:
        d={
            "summoner_name":self.in_game_name,
            "ELO": self.ELO_rating,
            "history": [el.to_dict() for el in self.history],
            "season": [el.to_dict() for el in self.season_history],
            "classification": self.classification,
            "position": self.main_position,
            "main":self.main_char,
            "char_usage":self.char_usage,
            "wins":self.total_wins,
            "games":self.total_games,
            "kills":self.total_kills,
            "deaths":self.total_deaths,
            "assists":self.total_assists,
            "gold": self.gold,
            "puuid":self.puuid,
            "season_size":self.season_size,
            "win_rate":self.win_rate,
            
            
        }
        return d
    def load(self,data:dict):
            self.in_game_name = data["summoner_name"]
            self.ELO_rating = data["ELO"] 
            self.history= [PlayerMatchData(el)for el in data["history"]]
            self.season_history= [PlayerMatchData(el) for el in data["season"]]
            self.classification = data["classification"] 
            self.main_position = data["position"] 
            self.main_char = data["main"]
            self.char_usage = data["char_usage"]
            self.total_wins = data["wins"]
            self.total_games = data["games"]
            self.total_kills = data["kills"]
            self.total_deaths = data["deaths"]
            self.total_assists = data["assists"]
            self.gold = data["gold"] 
            self.puuid = data["puuid"]
            self.season_size=data["season_size"]
            self.win_rate=data["win_rate"]
   
    def __init__(self,data:dict=None) -> None:
        self.in_game_name:str=None
        self.ELO_rating=None
        self.classification:int=None
        self.main_position=None
        self.main_char=None
        self.char_usage:dict[str,int]=None
        self.total_wins:int=None
        self.total_games:int=None
        self.history:"list[PlayerMatchData]"=None
        self.season_history:"list[PlayerMatchData]"=None#best n matches in the timeframe
        self.total_kills:int=None
        self.total_deaths:int=None
        self.total_assists:int=None
        self.gold:int=None
        self.puuid:int=None
        self.season_size:int=None
        self.win_rate:float=None
        if (data is not None):
            self.load(data)
        pass
    def set_season_size(self,v):
        self.season_size=v
    def update_total_games(self):
        self.total_games=len(self.history)
        pass
    def update_total_wins(self):
        temp=0
        for m in self.history:
            if m.won_match:
                temp+=1
        self.total_wins=temp
        self.win_rate=self.total_wins/self.total_games
    def update_elo(self):
        #TODO fix this
        elo=0
        for m in self.season_history:
            elo+=m.battle_score
        elo/=len(self.season_history)
        self.ELO_rating=elo
        pass
    def update_season(self):
        if self.season_history is None:
            self.season_history=[]
        if self.season_size is None:
            self.set_season_size(10)
        temp = sorted(self.history, key=lambda d: d.battle_score,reverse=True) 
        self.season_history=temp[:min(len(temp),self.season_size)]
        #if better than worse in season replace worst in season
        
        pass
    def update_main_position(self):
        char_usage=dict()
        for m in self.history:
            champ=m.position
            if champ in char_usage.keys():
                char_usage[champ]+=1
            else:
                char_usage[champ]=1
        self.main_position=sorted(char_usage.items(),key=lambda x: x[1],reverse=True)[0][0]
        pass
    def update_char_usage(self):
        char_usage:dict[str,int]=dict()
        for m in self.history:
            champ:str=m.character_name
            if champ in char_usage.keys():
                char_usage[champ]+=1
            else:
                char_usage[champ]=1
        self.char_usage=char_usage
        self.main_char=sorted(char_usage.items(),key=lambda x: x[1],reverse=True)[0][0]
    def update_match_statistics(self):
        k,d,a,g=0,0,0,0
        for m in self.history:
            k+=m.kills
            d+=m.deaths
            a+=m.assists
            g+=m.money_spent
        self.total_kills=k
        self.total_deaths=d
        self.total_assists=a
        self.gold=g
        pass
    def update_history(self,new_data:PlayerMatchData):
        if self.history is None:
            self.history=[]
        self.history.append(new_data)
        
        self.update_season()
        self.update_total_games()
        self.update_total_wins()
        self.update_match_statistics()
        self.update_main_position()
        self.update_char_usage()
        self.update_elo()
        return self
    def name(self,v:str):
        self.in_game_name=v
        return self
    def kills(self,v):
        self.total_kills=v
        return self
    def deaths(self,v):
        self.total_deaths=v
        return self
    def assists(self,v):
        self.total_assists=v
        return self
    def money(self,v):
        self.gold=v
        return self
    def id(self,v):
        self.puuid=v
        return self
    
class GameType(IntEnum):
    LOL=1
    CSGO=2
    PUBG=3
    TFT=4
    VALORANT=5
     
    
class TeamMatchData:
    pass

class MatchData:
    
    def to_dict(self)->dict:
        d={
            "game_type": int(self._game_type),
            "match_id": self._match_id,
            "players": [el.to_dict() for el in self._players],
            "match_mode": self._match_mode,
            "date": self._date,
        }
        return d
    
    def __repr__(self) -> str:
        return f"match {self._match_id} played with {self._players}"
    def __init__(self) -> None:
        self._game_type:GameType=None
        self._match_id:str=None
        self._players:list[PlayerMatchData]=None
        self._match_mode:str=None
        self._date:datetime=None
        pass
    
    def game_type(self,v:GameType):
        self._game_type=v
        return self
    def match_id(self,v:str):
        self._match_id=v
        return self
    def players(self,v:'list[PlayerMatchData]'):
        self._players=v
        return self
    def match_mode(self,v:str):
        self._match_mode=v
        return self
    def date(self,v:int):
        self._date=datetime.fromtimestamp(v/1000)
        return self

class Player:
    
    def __init__(self,puuid=None,elo=None,position=None) -> None:
        self.puuid:str=puuid
        self.elo:int=elo
        self.position:str=position    
    def __str__(self) -> str:
        return f"{self.puuid} with {self.elo} playing {self.position}"

class Party:
    max_disparity=50000
    def __init__(self) -> None:
        
        self.puuid:str=None
        self.player_pos:dict[str,Player]={
            "TOP":None,
            "MIDDLE":None,
            "UTILITY":None,
            "JUNGLE":None,
            "BOTTOM":None,
        }
        self.players:list[Player]=None
        self.party_strength:int=None
        res=self.create_party()
        if res:
            self.puuid=uuid.uuid4().hex
            print(self.party_strength)
            print(self.puuid)
            MatchmakingQueue.add_party(self)
            
        
            
    def create_party(self)->bool:
        print("creating party")
        self.find_top()
        self.find_mid()
        self.find_uti()
        self.find_jun()
        self.find_bot()
        for pos,player in self.player_pos.items():
            if player is not None:
                continue
            res=self.find_complete(pos)
            if not res:
                self.destroy_party()
                return res
        return True
        
    
    def destroy_party(self):
        print ("destroying party")
        for p in self.players:
            MatchmakingQueue.add_player(p)
        self.players=None
        self.player_pos=None
        pass
    
    def filter_based_on_elo(self,target_elo:int=None)->list[Player]:
        mmq=MatchmakingQueue.players
        if target_elo is None:
            return mmq
        mmq=list(filter(lambda x: target_elo+self.max_disparity>x.elo>target_elo-self.max_disparity,mmq ))
        return mmq
        
    def update_strenght(self):
        te=sum([e.elo for e in self.players ])
        self.party_strength=te/len(self.players)
        
    def add_player(self,p:Player,pos:str=None):
        if pos is None:
            pos=p.position
        if self.players is None:
            self.players=[]
        self.players.append(p)
        if self.party_strength is None:
            self.party_strength=0
        self.update_strenght()
        self.player_pos[pos]=p
        MatchmakingQueue.remove_player(p)
        print(f"added {p.puuid} as {pos}")
    
    def find_player_by_pos(self,pos:str):
        mmq=self.filter_based_on_elo(self.party_strength)
        players=list(filter(lambda x: x.position==pos,mmq))
        if len(players)>0:
            self.add_player(players[0],pos)
        pass
    
    def find_top(self):
        self.find_player_by_pos("TOP")
    
    def find_mid(self):
        self.find_player_by_pos("MIDDLE")
    
    def find_uti(self):
        self.find_player_by_pos("UTILITY")
    
    def find_jun(self):
        self.find_player_by_pos("JUNGLE")
    
    def find_bot(self):
        self.find_player_by_pos("BOTTOM")
    
    def find_complete(self,pos)->bool:
        mmq=self.filter_based_on_elo(self.party_strength)
        if len(mmq)==0:
            print("Not enough similar players, no one is filling",pos)
            return False
        self.add_player(mmq[0],pos)
    
   
class MatchmakingQueue:
    players:list[Player]=None
    parties:list[Party]=None
    
    @staticmethod
    def add_player(p:Player):
        
        if MatchmakingQueue.players is None:
            MatchmakingQueue.players=[]
        if not any(pl.puuid == p.puuid for pl in MatchmakingQueue.players):
            MatchmakingQueue.players.append(p)
            print(f"adding {p.puuid} to queue,{len(MatchmakingQueue.players)} on queue")
    
    @staticmethod
    def remove_player(p:Player):
        for el in MatchmakingQueue.players:
            if el.puuid==p.puuid:
                MatchmakingQueue.players.remove(el)
                print(f"removing {p.puuid} from queue,{len(MatchmakingQueue.players)} on queue")
        if len(MatchmakingQueue.players)==0:
            MatchmakingQueue.players=None
                
    def add_party(p:Party):
        if MatchmakingQueue.parties is None:
            MatchmakingQueue.parties=[]
        if not any(pl.puuid == p.puuid for pl in MatchmakingQueue.parties):
            MatchmakingQueue.parties.append(p)
            print(f"adding {p.puuid} to queue,{len(MatchmakingQueue.parties)} on queue")
    
    @staticmethod
    def remove_party(p:Party):
        for el in MatchmakingQueue.parties:
            if el.puuid==p.puuid:
                MatchmakingQueue.parties.remove(el)
                print(f"removing {p.puuid} from queue,{len(MatchmakingQueue.parties)} on queue")
        if len(MatchmakingQueue.parties)==0:
            MatchmakingQueue.parties=None
    
   
class Match:
    max_disparity=50000
    def __init__(self) -> None:
        
        self.puuid:str=None
    
        self.parties:list[Party]=None
        self.parties_pos:dict[str,Party]={
            "RED":None,
            "BLUE":None,
        }
        self.match_strength:int=None
        res=self.create_match()
        if res:
            self.puuid=uuid.uuid4().hex
            print(self.parties)
            print(self.puuid)            
        
            
    def create_match(self)->bool:
        print("creating match")
        res=self.find_blue()
        res=res and self.find_red()
        if not res:
            self.destroy_match()
        return res
        pass
        
    
    def find_blue(self)->bool:
        return self.find_enemy("BLUE")
    
    def find_red(self)->bool:
        return self.find_enemy("RED")
    
    def destroy_match(self):
        print("Destroying match")
        for p in self.parties:
            MatchmakingQueue.add_party(p)
        self.parties=None
        self.parties_pos=None
        pass
    
    def filter_based_on_elo(self,target_elo:int=None)->list[Party]:
        mmq=MatchmakingQueue.parties
        if target_elo is None:
            return mmq
        mmq=list(filter(lambda x: target_elo+self.max_disparity>x.party_strength >target_elo-self.max_disparity,mmq ))
        return mmq
        
    def update_strenght(self):
        te=sum([e.party_strength for e in self.parties ])
        self.party_strength=te/len(self.parties)
        
    def add_party(self,p:Party,pos:str):
        if self.parties is None:
            self.parties=[]
        self.parties.append(p)
        if self.match_strength is None:
            self.match_strength=0
        self.update_strenght()
        self.parties_pos[pos]=p
        MatchmakingQueue.remove_party(p)
        print(f"added {p.puuid} to match as {pos} team")
    
    def find_enemy(self,pos:str)->bool:
        mmq=self.filter_based_on_elo(self.match_strength)
        if self.match_strength is None:
            #self.match_strength=0
            self.add_party(mmq[0],pos)
            return True
        parties=sorted(mmq,key=lambda x: abs(self.match_strength-x.party_strength))
        if len(parties)>0:
            self.add_party(parties[0],pos)
            return True
        return False
        pass
    
    
    