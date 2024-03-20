import bracket_generator.team
import bracket_generator.game
import logging
import yaml

_logger = logging.getLogger(__name__)


class Bracket:
    def __init__(self, config):
        self.config = config

    def __str__(self):
        config_dump = yaml.dump(self.config)
        return config_dump

    def simulate(self):
        # Create all the team and game objects
        round1 = []
        for region in self.config:
            for game in self.config[region]:
                # _logger.debug(game)
                round1.append(
                    bracket_generator.game.Game(
                        bracket_generator.team.Team(game["team1"], game["seed1"]),
                        bracket_generator.team.Team(game["team2"], game["seed2"]),
                        1,
                    )
                )

        round2 = []
        team1 = None
        for game in round1:
            if team1 is None:
                team1 = game.simulate()
            else:
                round2.append(bracket_generator.game.Game(team1, game.simulate(), 2))
                team1 = None

        _logger.debug("ROUND 2:")
        for game in round2:
            _logger.debug(game)

        round3 = []
        team1 = None
        for game in round2:
            if team1 is None:
                team1 = game.simulate()
            else:
                round3.append(bracket_generator.game.Game(team1, game.simulate(), 3))
                team1 = None

        _logger.debug("ROUND 3:")
        for game in round3:
            _logger.debug(game)

        round4 = []
        team1 = None
        for game in round3:
            if team1 is None:
                team1 = game.simulate()
            else:
                round4.append(bracket_generator.game.Game(team1, game.simulate(), 4))
                team1 = None

        _logger.debug("ROUND 4:")
        for game in round4:
            _logger.debug(game)

        round5 = []
        team1 = None
        for game in round4:
            if team1 is None:
                team1 = game.simulate()
            else:
                round5.append(bracket_generator.game.Game(team1, game.simulate(), 5))
                team1 = None

        _logger.debug("ROUND 5:")
        for game in round5:
            _logger.debug(game)

        round6 = []
        team1 = None
        for game in round5:
            if team1 is None:
                team1 = game.simulate()
            else:
                round6.append(bracket_generator.game.Game(team1, game.simulate(), 6))
                team1 = None

        _logger.debug("ROUND 6:")
        for game in round6:
            _logger.debug(game)

        _logger.debug("ROUND 7:")
        winner = round6[0].simulate()

        _logger.debug("WINNER:")
        _logger.debug(winner)
