# coding: utf-8
# license: GPLv3
import math
import time

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Рассчитываем суммарную силу на тело"""
    for objects in space_objects:
        if objects == body:
            continue
        r = ((body.x - objects.x) ** 2 + (body.y - objects.y) ** 2) ** 0.5
        r = max(r, body.R + objects.R)  # обработка аномалий при прохождении одного тела сквозь другое
        body.Fx += -gravitational_constant * objects.m * body.m * (body.x - objects.x) / r ** 3
        body.Fy += -gravitational_constant * objects.m * body.m * (body.y - objects.y) / r ** 3


def move_space_object(body, dt):
    """Задаём новые координаты тела, изменяем скорость с частотой dt"""
    ax = body.Fx/body.m
    body.x += body.Vx*dt + ax*dt**2/2
    body.Vx += ax*dt
    ay = body.Fy/body.m
    body.y += body.Vy*dt + ay*dt**2/2
    body.Vy += ay*dt


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """
    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
