from mesa import Agent
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector
from main import MyModel

class LightcycleAgent(Agent):
    """
    Lightcycle driver agent
    """

    def __init__(self, pos, direction, model):
        """
        Create a new Lightcycle agent.

        Args:
           x, y: Agent initial location.
        """
        super().__init__(pos, model)
        self.pos = pos
        self.lightpath = []
        self.direction = direction

    def step(self):
        new_direction = ''
        self.lightpath.append(self.pos)

        if self.direction == 'N':
            left = len([n for n in self.lightpath if n[0] < self.pos[0]])
            front = len([n for n in self.lightpath if n[1] > self.pos[1]])
            right = len([n for n in self.lightpath if n[0] > self.pos[0]])
            fillings = {'W': left, 'N': front, 'E': right}
            new_direction = min(fillings, key=fillings.get)

        elif self.direction == 'S':
            left = len([n for n in self.lightpath if n[0] > self.pos[0]])
            front = len([n for n in self.lightpath if n[1] < self.pos[1]])
            right = len([n for n in self.lightpath if n[0] < self.pos[0]])
            fillings = {'W': right, 'S': front, 'E': left}
            new_direction = min(fillings, key=fillings.get)

        elif self.direction == 'W':
            left = len([n for n in self.lightpath if n[1] < self.pos[1]])
            front = len([n for n in self.lightpath if n[0] < self.pos[0]])
            right = len([n for n in self.lightpath if n[1] > self.pos[1]])
            fillings = {'N': right, 'W': front, 'S': left}
            new_direction = min(fillings, key=fillings.get)

        else:
            left = len([n for n in self.lightpath if n[1] > self.pos[1]])
            front = len([n for n in self.lightpath if n[0] > self.pos[0]])
            right = len([n for n in self.lightpath if n[1] < self.pos[1]])
            fillings = {'S': right, 'E': front, 'N': left}
            new_direction = min(fillings, key=fillings.get)

        if new_direction == 'N':
            self.pos[1] += 1
        elif new_direction == 'S':
            self.pos[1] -= 1
        elif new_direction == 'W':
            self.pos[0] -= 1
        else:
            self.pos[0] += 1

