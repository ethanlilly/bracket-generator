import pytest

import bracket_generator.team

__author__ = "topgolfci"
__copyright__ = "topgolfci"
__license__ = "MIT"


def test_str():
    test_team = bracket_generator.team.Team("team1", "1")
    assert test_team.__str__() == "team1(1)"
