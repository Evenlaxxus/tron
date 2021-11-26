import random

from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation

from agent import LightcycleAgent


def getStartingPosition(startingPositions, isRandom=False):
    if isRandom:
        coords = (random.randrange(0, 10), random.randrange(0, 10))
        while coords in startingPositions:
            coords = (random.randrange(0, 10), random.randrange(0, 10))
        return coords
    if len(startingPositions) % 2 == 1:
        options = [option for option in [(1, 7), (1, 5), (1, 3), (7, 1), (5, 1), (3, 1)] if
                   option not in startingPositions]
        return random.choice(options)
    else:
        return 10 - startingPositions[-1][0], 10 - startingPositions[-1][1]


def getStartingDirection(position, isRandom=False):
    if isRandom:
        random.choice(['n', 's', 'w', 'e'])
    if position[0] == 1:
        return 'e'
    if position[0] == 9:
        return 'w'
    if position[1] == 1:
        return 'n'
    if position[1] == 9:
        return 's'


class TronModel(Model):
    def __init__(self, n_agents, max_path_length, knows_other_paths, fov):
        super().__init__()
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(10, 10, torus=False)
        self.startingPositions = []

        for i in range(n_agents):
            self.startingPositions.insert(-1, getStartingPosition(self.startingPositions))
            a = LightcycleAgent(self.startingPositions[-1], getStartingDirection(self.startingPositions[-1]), self)
            self.schedule.add(a)
            self.grid.place_agent(a, self.startingPositions[-1])

    def step(self):
        self.schedule.step()


if __name__ == '__main__':
    model = TronModel(5, 1, 2, 3)
    model.step()
