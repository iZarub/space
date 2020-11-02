# coding: utf-8
# license: GPLv3
import math
import time

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    for objects in space_objects - body:
        alfa = math.atan((objects.x - body.x) / (objects.y - body.y))
        distance = math.sqrt((objects.x - body.x) ** 2 + (objects.y - body.y) ** 2)
        body.Fx += gravitational_constant * (body.m * objects.m) / distance ** 2 * math.sin(alfa)
        body.Fy += gravitational_constant * (body.m * objects.m) / distance ** 2 * math.cos(alfa)

def move_space_object(body, dt):

    body.vx += Fx


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """

    pass


if __name__ == "__main__":
    print("This module is not for direct call!")
