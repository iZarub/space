# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet

colors = {
    'red': (255, 0, 0),
    'blue': (0, 0, 255),
    'green': (31, 168, 31),
    'orange': (241, 178, 64),
    'gray': (191, 191, 191),
    'yellow': (255, 255, 0),
    'white': (255, 255, 255),
    'cyan': (0, 255, 255),
}


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов
    Параметры:
    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем

            object_type = line.split()[0].lower()
            if object_type == "planet" or object_type == 'star':
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    tokens = line.split()
    assert len(tokens) == 8
    planet.type = tokens[0]
    planet.R = int(tokens[1])
    planet.color = colors[tokens[2]]
    planet.m = float(tokens[3])
    planet.x = float(tokens[4])
    planet.y = float(tokens[5])
    planet.Vx = float(tokens[6])
    planet.Vy = float(tokens[7])


def write_space_objects_data_to_file(output_filename, space_objects, time):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Параметры:
    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'a') as out_file:
        for obj in space_objects:
            if obj.type == 'Planet':
                print(obj.type, obj.R, get_key(obj.color, colors), obj.m, obj.x, obj.y, "{:f}".format((obj.x**2 + obj.y**2)**0.5),
                      time, file=out_file)


def get_key(val, dictionary):
    for key, value in dictionary.items():
        if val == value:
            return key


if __name__ == "__main__":
    print("This module is not for direct call!")
