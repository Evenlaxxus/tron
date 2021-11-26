from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid

from main import TronModel


def tronPortrayal(agent):
    if agent is None:
        return

    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "red",
                 "r": 0.5
                 }
    return portrayal


grid = CanvasGrid(tronPortrayal, 26, 26, 500, 500)

server = ModularServer(TronModel,
                       [grid],
                       "dupa",
                       {
                           "n_agents": 5,
                           "max_path_length": 3,
                           "knows_other_paths": False,
                           "fov": 3,
                           "isStartingPositionRandom": False
                       }
                       )
server.port = 8521
server.launch()
