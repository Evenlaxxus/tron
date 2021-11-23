from mesa import Agent
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector
from main import MyModel

class LightcycleAgent(Agent):
    """
    Lightcycle driver agent
    """

    def __init__(self, pos, model):
        """
        Create a new Lightcycle agent.

        Args:
           x, y: Agent initial location.
        """
        super().__init__(pos, model)
        self.pos = pos

    def step(self):



