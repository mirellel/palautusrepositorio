import unittest
from statistics import Statistics, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_return_correct_player(self):
        semenko = self.statistics.search("Semenko")

        self.assertAlmostEqual(self.statistics.search("Semenko"), semenko)
    
    def test_return_correct_team(self):
        edm = self.statistics.team("EDM")

        self.assertAlmostEqual(edm, self.statistics.team("EDM"))


    def test_return_none_when_player_nonexixtent(self):

        self.assertAlmostEqual(None, self.statistics.search("Mirelle"))

    def test_return_top_player_by_assists(self):
        top_scores = self.statistics.top(3, SortBy.ASSISTS)

        self.assertAlmostEqual(top_scores, self.statistics.top(3, SortBy.ASSISTS))

    def test_return_top_player_by_goals(self):
        top_scores = self.statistics.top(3, SortBy.GOALS)

        self.assertEqual(top_scores, self.statistics.top(3, SortBy.GOALS))

    def test_return_top_player_by_points(self):
        top_scores = self.statistics.top(3, SortBy.POINTS)

        self.assertAlmostEqual(top_scores, self.statistics.top(3, SortBy.POINTS))

    


    
    