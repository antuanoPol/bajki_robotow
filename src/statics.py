from os import path

WIDTH = 1900
HEIGHT = 1000
FPS = 60
PUNKTY = 0

LEFT = 'LEFT'
RIGHT = 'RIGHT'
UP = 'UP'
DOWN = 'DOWN'

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 247, 0)

# paths
img_dir = path.join(path.dirname(__file__), "../assets/img")
snd_dir = path.join(path.dirname(__file__), "../assets/sound")
explosions_dir = path.join(path.dirname(__file__), "../assets/img/explosions")