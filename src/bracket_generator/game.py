import bracket_generator.team
import random
import logging

_logger = logging.getLogger(__name__)


class Game:
    # TODO: come up with a better odds calculation
    # This is a matrix of round x seed diff where each
    # value represents the odds of an upset
    odds = [
        [],
        [0, 50, 49, 45, 42, 40, 38, 37, 34, 30, 25, 21, 16, 10, 6, 2],  # Round 1
        [0, 52, 46, 41, 36, 34, 31, 28, 26, 24, 21, 18, 14, 10, 6, 2],  # Round 2
        [0, 54, 47, 42, 37, 35, 32, 29, 27, 25, 22, 19, 15, 12, 8, 3],  # Sweet 16
        [0, 55, 48, 44, 40, 38, 36, 34, 31, 28, 25, 22, 19, 14, 10, 5],  # Elite 8
        [0, 55, 50, 47, 44, 42, 40, 38, 35, 32, 28, 24, 20, 15, 12, 7],  # Final 4
        [0, 55, 53, 51, 49, 47, 45, 44, 43, 42, 41, 40, 38, 35, 33, 30],  # Championship
    ]

    def __init__(self, team1, team2, round):
        self.team1 = team1
        self.team2 = team2
        self.round = round

    def __str__(self):
        return f"{self.team1} vs {self.team2} in round {self.round}"

    def simulate(self):
        diff = abs(self.team1.seed - self.team2.seed)
        if random.randrange(0, 100) > self.odds[self.round][diff]:
            return self.team1
        else:
            return self.team2
