import pytest

import bracket_generator.team
import bracket_generator.game

__author__ = "topgolfci"
__copyright__ = "topgolfci"
__license__ = "MIT"


def test_str():
    test_team1 = bracket_generator.team.Team("team1", "1")
    test_team2 = bracket_generator.team.Team("team2", "2")
    test_game = bracket_generator.game.Game(test_team1, test_team2, 1)
    assert test_game.__str__() == "team1(1) vs team2(2) in round 1"


def test_simulate():
    test_team1 = bracket_generator.team.Team("team1", "1")
    test_team2 = bracket_generator.team.Team("team2", "2")
    test_game = bracket_generator.game.Game(test_team1, test_team2, 1)
    winner = test_game.simulate()
    assert winner.name == "team1" or winner.name == "team2"
