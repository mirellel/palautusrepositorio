import requests
from player import Player
from datetime import datetime

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = []
    def get_players(self):
        response = requests.get(self.url).json()
         
        for player_dict in response:
            player = Player(
            player_dict['name'],
            player_dict['team'],
            player_dict['goals'],
            player_dict['assists'],
            player_dict['nationality'])
            self.players.append(player)
        
        self.players.sort(key=lambda p: p.points, reverse=True)
        
        return self.players

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = self.reader.get_players()
        self.players_by_nat = []
    
    def top_scores_by_nationality(self, nationality):
        for player in self.players:
            if str(player.nationality) == nationality:
                self.players_by_nat.append(player)
        return self.players_by_nat

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scores_by_nationality("FIN")
    
    for player in players:
        print(player)

if __name__ == "__main__":
    main()
