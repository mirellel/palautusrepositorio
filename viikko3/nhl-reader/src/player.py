class Player:
    def __init__(self, name, team, goals, assists, nationality):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.nationality = nationality

        self.points = self.goals+self.assists
    
    def __str__(self):
        return f"{self.name:20} {self.team:2}  {self.goals:2} + {self.assists:2} = {self.points}"