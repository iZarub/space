import numpy
import pygame
from pygame.draw import *

from solar_objects import *
from solar_vis import *

pygame.init()

# Константы
G = 6.667e-11  # гравитационная постоянная, м^3 кг^-1 с^-2
MS = 1.9885e30  # масса Солнца, кг
ME = 5.97e24  # масса Земли, кг
MM = 7.348e22  # масса Луны, кг
RSE = 1.496e11  # среднее расстояние от Солнца до Земли, метры
REM = 384.4e6  # расстояние от Земли до Луны
FPS = 60

red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
black = (0, 0, 0)

star = Star()
star.m = 1.98892E30
star.color = 'red'
star.r = 30
star.x = 0
star.y = 0
star.vx = 0
star.vy = 0

earth = Planet()
earth.m = 1.98892E30
earth.color = 'green'
earth.r = 5
earth.x = 149.60E9
earth.y = 0
earth.vx = 0
earth.vy = 29.76E3

objects = []


def main():
    screen = pygame.display.set_mode((window_width, window_width))
    clock = pygame.time.Clock()




main()
