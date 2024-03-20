class Team:
    def __init__(self, name, seed):
        self.name = name
        self.seed = seed

    def __str__(self):
        return f"{self.name}({self.seed})"
