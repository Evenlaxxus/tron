import random

from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid

from main import TronModel

number_of_colors = 12

color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]

def tronPortrayal(agent):
    if agent is None:
        return
    if agent.unique_id == 0:
        portrayal = {"Shape": "circle",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": color[0],
                     "r": 0.5
                     }
    elif agent.unique_id == 1:
        portrayal = {"Shape": "circle",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": color[1],
                     "r": 0.5
                     }
    elif agent.unique_id == 2:
        portrayal = {"Shape": "circle",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": color[2],
                     "r": 0.5
                     }
    elif agent.unique_id == 3:
        portrayal = {"Shape": "circle",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": color[3],
                     "r": 0.5
                     }
    elif agent.unique_id == 4:
        portrayal = {"Shape": "circle",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": color[4],
                     "r": 0.5
                     }
    elif agent.unique_id == 5:
        portrayal = {"Shape": "circle",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": color[5],
                     "r": 0.5
                     }
    elif agent.unique_id == 6:
        portrayal = {"Shape": "circle",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": color[6],
                     "r": 0.5
                     }
    elif agent.unique_id == 7:
        portrayal = {"Shape": "circle",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": color[7],
                     "r": 0.5
                     }
    elif agent.unique_id == 8:
        portrayal = {"Shape": "circle",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": color[8],
                     "r": 0.5
                     }
    elif agent.unique_id == 9:
        portrayal = {"Shape": "circle",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": color[9],
                     "r": 0.5
                     }
    elif agent.unique_id == 10:
        portrayal = {"Shape": "circle",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": color[10],
                     "r": 0.5
                     }
    else:
        portrayal = {"Shape": "circle",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": color[11],
                     "r": 0.5
                     }

    return portrayal


grid = CanvasGrid(tronPortrayal, 26, 26, 500, 500)

server = ModularServer(TronModel,
                       [grid],
                       "dupa",
                       {
                           "n_agents": 3,
                           "max_path_length": 3,
                           "knows_other_paths": False,
                           "fov": 3,
                           "isStartingPositionRandom": False
                       }
                       )
server.port = 8521
server.launch()
