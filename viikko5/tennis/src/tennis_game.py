class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1



    def get_score(self):
        result = self.m_score1 - self.m_score2

        if result == 0:
            return self.even_score(self.m_score1)

        if self.m_score1 >= 4 or self.m_score2 >=4:
            return self.over_forty(result)
        else:
            return self.under_forty()

    def even_score(self, score):
        return {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All"
        }.get(score, "Deuce")

    def over_forty(self, score):
        if score == 1:
            return "Advantage Player1"
        if score == -1:
            return "Advantage Player2"
        if score >= 2:
            return "Win for Player1"
        else:
            return "Win for Player2"

    def under_forty(self):
        dict = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }
        return f"{dict.get(self.m_score1)}-{dict.get(self.m_score2)}"

        
