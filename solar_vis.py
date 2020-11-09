# coding: utf-8
# license: GPLv3

import pygame as pg
from pygame.draw import *

"""Модуль визуализации.
Нигде, кроме этого модуля, не используются экранные координаты объектов.
Функции, создающие графические объекты и перемещающие их на экране, принимают физические координаты
"""

header_font = "Arial-16"
"""Шрифт в заголовке"""

window_width = 1400
"""Ширина окна"""

window_height = 800
"""Высота окна"""

scale_factor = 1
"""Масштабирование экранных координат по отношению к физическим.
Тип: float
Мера: количество пикселей на один метр."""


def calculate_scale_factor(max_distance):
    """Вычисляет значение глобальной переменной **scale_factor** по данной характерной длине"""
    global scale_factor
    scale_factor = 0.5 * min(window_height - 70, window_width - 70) / max_distance
    print('Scale factor:', scale_factor)


def scale_x(x):
    """Возвращает экранную **x** координату по **x** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **x** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.
    Параметры:
    **x** — x-координата модели.
    """

    return int(x * scale_factor) + window_width // 2


def scale_y(y):
    """Возвращает экранную **y** координату по **y** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **y** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.
    Направление оси развёрнуто, чтобы у модели ось **y** смотрела вверх.
    Параметры:
    **y** — y-координата модели.
    """

    return int(-y * scale_factor) + window_height // 2


if __name__ == "__main__":
    print("This module is not for direct call!")


class Drawer:
    def __init__(self, screen):
        self.screen = screen

    def update(self, figures, ui):
        self.screen.fill((0, 0, 0))
        for figure in figures:
            DrawableObject.draw_on(self.screen, figure)

        ui.blit()
        ui.update()
        pg.display.update()


class DrawableObject:
    def __init__(self, obj):
        self.obj = obj

    @staticmethod
    def draw_on(surface, object):
        circle(surface, object.color, (scale_x(object.x), scale_y(object.y)), object.R)