# Case - study

# This program

# Developers : Daniel A.         (%),
#              Zemtseva A.       (%),
#              Torgasheva A.     (%).

# Tasks:
#       НАСТЯ
#   - меню: цвет (get_color_choice), количество 6-угольников (get_num_hexagons) !!! Учесть возможность ошибки ввода
#   - локализация
#
#       АЛИНА
#   - нарисовать один шестиугольник, размещение шестигольников - в одной функции draw_hexagon
#
#       АЛЁНА
#   - вычислить длинну стороны шестиугольника, а также величину d (см на картинке у Минака с формулами)
#   - оформление программы (код ревью, комменты и т.д.)



from turtle import *
import math


def get_num_hexagons():
    return 1


def get_color_choice():
    return


def side_length(d):
    side = d / 2 / math.cos(math.radians(30))
    return side


def d_length(n):
    d = 500 / (n + 0.5)
    return d


def draw_hexagon(x, y, side_len, color):
    pass


def main():
    hexagon_number = get_num_hexagons()
    d = d_length(hexagon_number)
    side = side_length(d)


main()
