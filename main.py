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


import turtle as t
import math


def get_num_hexagons():
    hexagon_number = int(input())
    return hexagon_number


def get_color_choice():
    return ('pink', 'lavender')


def side_length(d):
    side = d / 2 / math.cos(math.radians(30))
    return side


def d_length(n):
    d = 500 / (n + 0.5)
    return d


def draw_hexagon(x, y, side_len, color):
    t.up()
    t.goto(x, y)
    t.down()
    t.right(30)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(6):
        t.forward(side_len)
        t.right(60)
    t.left(30)
    t.end_fill()


def draw_row(x, y, d, s, number, color_1, color_2):
    for i in range(number):
        if i % 2 == 0:
            color = color_1
        else:
            color = color_2
        draw_hexagon(x + d / 2, y, s, color)
        x += d


def fill_space(x, y, d, s, number, color_1, color_2, ptr):
    for i in range(number):
        if ptr == 2:
            ptr = 0
            color_1, color_2 = color_2, color_1
        if i % 2 == 1:
            draw_row(x + d / 2, y - s * 1.5 * i, d, s, number, color_1, color_2)
            ptr += 1
        else:
            draw_row(x, y - s * 1.5 * i, d, s, number, color_1, color_2)
            ptr += 1


def main():
    hexagon_number = get_num_hexagons()
    t.speed(10.5)
    color_1,color_2 = get_color_choice()
    fill_space(-250, 250, d_length(hexagon_number), side_length(d_length(hexagon_number)), hexagon_number, color_1, color_2, 1)
    t.done()


main()
