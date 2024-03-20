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
        [0, 50, 45, 42, 40, 39, 38, 37, 34, 30, 25, 20, 15, 10, 5, 0],
        [0, 50, 45, 40, 35, 33, 30, 27, 25, 23, 20, 18, 15, 10, 5, 0],
        [0, 50, 45, 40, 35, 33, 30, 27, 25, 23, 20, 18, 15, 10, 5, 0],
        [0, 50, 45, 42, 40, 39, 38, 37, 34, 30, 25, 20, 15, 10, 5, 0],
        [0, 50, 45, 42, 40, 39, 38, 37, 34, 30, 25, 20, 15, 10, 5, 0],
        [0, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 30, 31, 30],
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
