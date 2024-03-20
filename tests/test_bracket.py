import os
import pytest
import yaml

import bracket_generator.team
import bracket_generator.game
import bracket_generator.bracket

__author__ = "topgolfci"
__copyright__ = "topgolfci"
__license__ = "MIT"


def test_str():
    path = os.path.realpath(__file__)
    dir = os.path.dirname(path)
    with open(f"{dir}/data/test_bracket_str.yaml", "r") as file:
        test_config = yaml.safe_load(file)

    test_bracket = bracket_generator.bracket.Bracket(test_config)
    assert test_bracket.__str__() == "- team1\n- team2\n"


# def test_simulate():
#     path = os.path.realpath(__file__)
#     dir = os.path.dirname(path)
#     with open(f"{dir}/data/test_bracket.yaml", "r") as file:
#         test_config = yaml.safe_load(file)

#     test_bracket = bracket_generator.bracket.Bracket(test_config)
#     assert test_bracket.__str__() == "- team1\n- team2\n"
