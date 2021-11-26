import random

from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation

from agent import LightcycleAgent


def getStartingPosition(startingPositions, isRandom):
    if isRandom:
        coords = (random.randrange(0, 25), random.randrange(0, 25))
        while coords in startingPositions:
            coords = (random.randrange(0, 25), random.randrange(0, 25))
        return coords
    if len(startingPositions) % 2 == 1 or len(startingPositions) == 0:
        options = [option for option in [(1, 7), (1, 13), (1, 20), (7, 1), (13, 1), (20, 1)] if
                   option not in startingPositions]
        return random.choice(options)
    else:
        return 25 - startingPositions[-1][0], 25 - startingPositions[-1][1]


def getStartingDirection(position, isRandom):
    if isRandom:
        random.choice(['N', 'S', 'W', 'E'])
    if position[0] == 1:
        return 'E'
    if position[0] == 9:
        return 'W'
    if position[1] == 1:
        return 'N'
    if position[1] == 9:
        return 'S'


class TronModel(Model):
    def __init__(self, n_agents, max_path_length, knows_other_paths, fov, isStartingPositionRandom):
        super().__init__()
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(26, 26, torus=False)
        self.startingPositions = []

        for i in range(n_agents):
            self.startingPositions.append(getStartingPosition(self.startingPositions, isStartingPositionRandom))
            a = LightcycleAgent(i, self.startingPositions[-1],
                                getStartingDirection(self.startingPositions[-1], isStartingPositionRandom), self)
            self.schedule.add(a)
            self.grid.place_agent(a, self.startingPositions[-1])

    def step(self):
        self.schedule.step()


if __name__ == '__main__':
    model = TronModel(5, 3, False, 3, False)
    model.step()
