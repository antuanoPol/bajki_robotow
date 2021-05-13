#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path

# BASIC
WIDTH = 1800
HEIGHT = 960
FPS = 60

# DIRECTIONS
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

# PATHS
img_dir = path.join(path.dirname(__file__), "assets/img")
snd_dir = path.join(path.dirname(__file__), "assets/sound")
explosions_dir = path.join(path.dirname(__file__), "assets/img/explosions")
robot_animation_dir = path.join(path.dirname(__file__), "assets/img/robot")
doors_animation_dir = path.join(path.dirname(__file__), "assets/img/animated_door")
boss_animation_dir = path.join(path.dirname(__file__), "assets/img/boss")
terminal_dir = img_dir
