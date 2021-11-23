from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid


class MyAgent(Agent):
    def __init__(self, name, model):
        super().__init__(name, model)
        self.name = name

    def step(self):
        print("{} activated".format(self.name))
        # Whatever else the agent does when activated


class MyModel(Model):
    def __init__(self, n_agents, max_path_length, knows_other_paths, fov):
        super().__init__()
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(10, 10, torus=True)
        for i in range(n_agents):
            a = MyAgent(i, self)
            self.schedule.add(a)
            coords = (self.random.randrange(0, 10), self.random.randrange(0, 10))
            self.grid.place_agent(a, coords)

    def step(self):
        self.schedule.step()


if __name__ == '__main__':
    model = MyModel(5, 1, 2, 3)
    model.step()
