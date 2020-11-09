# coding: utf-8
# license: GPLv3
import numpy
import pygame
from pygame.draw import *

"""Модуль визуализации.
Нигде, кроме этого модуля, не используются экранные координаты объектов.
Функции, создающие графические объекты и перемещающие их на экране, принимают физические координаты
"""

header_font = "Arial-16"
"""Шрифт в заголовке"""

window_width = 800
"""Ширина окна"""

window_height = 800
"""Высота окна"""

scale_factor = None
"""Масштабирование экранных координат по отношению к физическим.

Тип: float

Мера: количество пикселей на один метр."""


def calculate_scale_factor(max_distance):
    scale_factor = window_width / max_distance


def scale_x(x):
    """Возвращает экранную **x** координату по **x** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **x** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.

    Параметры:

    **x** — x-координата модели.
    """

    return x * scale_factor


def scale_y(y):
    """Возвращает экранную **y** координату по **y** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **y** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.

    Параметры:

    **y** — y-координата модели.
    """

    return y * scale_factor


def create_star_image(space, star):
    circle(space, star.color, (scale_x(star.x), scale_y(star.y)), star.r)



def create_planet_image(space, planet):
    """Создаёт отображаемый объект планеты.

    Параметры:

    **space** — холст для рисования.

    **planet** — объект планеты.
    """

    pass


def update_system_name(space, system_name):
    """Создаёт на холсте текст с названием системы небесных тел.
    Если текст уже был, обновляет его содержание.

    Параметры:

    **space** — холст для рисования.

    **system_name** — название системы тел.
    """
    pass


def update_object_position(space, body):
    circle(space, black, (body.x, body.y), body.r)



if __name__ == "__main__":
    print("This module is not for direct call!")
