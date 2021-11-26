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
        self.lightpath = [(-1, n) for n in range(0, 27)] + [(26, n) for n in range(0, 27)] + \
                         [(n, -1) for n in range(0, 27)] + [(n, 26) for n in range(0, 27)]
        self.direction = direction

    def move(self, fillings):
        if len(fillings) > 0:
            new_direction = min(fillings, key=fillings.get)
            new_pos = self.pos
            if new_direction == 'N':
                new_pos[1] += 1
                if new_pos in self.lightpath:
                    del fillings[new_direction]
                    self.move(fillings)
                else:
                    self.pos = new_pos

            elif new_direction == 'S':
                new_pos[1] -= 1
                if new_pos in self.lightpath:
                    del fillings[new_direction]
                    self.move(fillings)
                else:
                    self.pos = new_pos

            elif new_direction == 'W':
                new_pos[0] -= 1
                if new_pos in self.lightpath:
                    del fillings[new_direction]
                    self.move(fillings)
                else:
                    self.pos = new_pos

            elif new_direction == 'E':
                new_pos[0] += 1
                if new_pos in self.lightpath:
                    del fillings[new_direction]
                    self.move(fillings)
                else:
                    self.pos = new_pos
        else:
            self.model.grid._remove_agent(self.pos, self)
            self.model.schedule.remove(self)

    def step(self):
        self.lightpath.append(self.pos)

        if self.direction == 'N':
            left = len([n for n in self.lightpath if n[0] < self.pos[0]])
            front = len([n for n in self.lightpath if n[1] > self.pos[1]])
            right = len([n for n in self.lightpath if n[0] > self.pos[0]])
            fillings = {'W': left, 'N': front, 'E': right}

        elif self.direction == 'S':
            left = len([n for n in self.lightpath if n[0] > self.pos[0]])
            front = len([n for n in self.lightpath if n[1] < self.pos[1]])
            right = len([n for n in self.lightpath if n[0] < self.pos[0]])
            fillings = {'W': right, 'S': front, 'E': left}

        elif self.direction == 'W':
            left = len([n for n in self.lightpath if n[1] < self.pos[1]])
            front = len([n for n in self.lightpath if n[0] < self.pos[0]])
            right = len([n for n in self.lightpath if n[1] > self.pos[1]])
            fillings = {'N': right, 'W': front, 'S': left}

        else:
            left = len([n for n in self.lightpath if n[1] > self.pos[1]])
            front = len([n for n in self.lightpath if n[0] > self.pos[0]])
            right = len([n for n in self.lightpath if n[1] < self.pos[1]])
            fillings = {'S': right, 'E': front, 'N': left}

        self.move(fillings)
