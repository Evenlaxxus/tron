import random
from mesa import Agent


class LightcycleAgent(Agent):
    """
    Lightcycle driver agent
    """

    def __init__(self, unique_id, pos, direction, model):
        """
        Create a new Lightcycle agent.

        Args:
           x, y: Agent initial location.
        """
        super().__init__(pos, model)
        self.unique_id = unique_id
        self.pos = pos
        self.lightpath = set()
        self.boundries = [(-1, n) for n in range(0, 27)] + [(26, n) for n in range(0, 27)] + \
                         [(n, -1) for n in range(0, 27)] + [(n, 26) for n in range(0, 27)]
        self.direction = direction
        self.first_move = True

    def move(self, fillings):
        new_direction = ''
        new_pos = self.pos
        while len(fillings) > 0:
            if self.first_move:
                new_direction = random.choice(list(fillings.keys()))
                self.first_move = False
            else:
                new_direction = min(fillings, key=fillings.get)
            new_pos = list(self.pos)
            if new_direction == 'N':
                new_pos[1] += 1
                if tuple(new_pos) in self.lightpath or tuple(new_pos) in self.boundries:
                    del fillings[new_direction]
                else:
                    break

            elif new_direction == 'S':
                new_pos[1] -= 1
                if tuple(new_pos) in self.lightpath or tuple(new_pos) in self.boundries:
                    del fillings[new_direction]
                else:
                    break

            elif new_direction == 'W':
                new_pos[0] -= 1
                if tuple(new_pos) in self.lightpath or tuple(new_pos) in self.boundries:
                    del fillings[new_direction]
                else:
                    break

            elif new_direction == 'E':
                new_pos[0] += 1
                if tuple(new_pos) in self.lightpath or tuple(new_pos) in self.boundries:
                    del fillings[new_direction]
                else:
                    break

        if new_pos == self.pos:
            self.model.grid._remove_agent(self.pos, self)
            self.model.schedule.remove(self)
        else:
            self.model.grid.place_agent(self, tuple(new_pos))
            self.direction = new_direction
            self.pos = tuple(new_pos)

    def observation(self):
        for agent in self.model.schedule.agents:
            self.lightpath = set.union(self.lightpath, agent.lightpath)
            self.lightpath.add(agent.pos)

    def step(self):
        self.lightpath.add(self.pos)

        self.observation()

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
