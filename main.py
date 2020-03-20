# Case - study

# Tesselation.

# Developers : Daniel A.         (40%),
#              Zemtseva A.       (35%),
#              Torgasheva A.     (35%).


import turtle as t
import math


def get_num_hexagons():
    """
    Getting number of hexagons in one side.
    :return: number of hexagons
    """
    print(lc.TXT_NUMBER, end='')
    hexagon_number = int(input())
    while hexagon_number > 20 or hexagon_number < 4:
        print(lc.TXT_ERROR, end='')
        hexagon_number = int(input())
    else:
        print()
        return hexagon_number


def get_color_choice():
    """
    Getting colors of hexagons.
    :return: two colors of hexagons
    """
    print(lc.TXT_COLOR_1)
    color_names = {'красный': 'lightcoral', 'оранжевый': 'bisque', 'розовый': 'lightpink', 'фиолетовый': 'violet',
                   'голубой': 'lightsteelblue', 'синий': 'royalblue', 'зеленый': 'palegreen',
                   'red': 'lightcoral', 'orange': 'bisque', 'pink': 'lightpink', 'purple': 'violet',
                   'blue': 'lightsteelblue', 'dark blue': 'royalblue', 'green': 'palegreen'}
    list_of_colors = []
    for i in range(2):
        print(lc.TXT_COLOR, end='')
        answer = input().lower()
        while answer not in color_names:
            print('"' + answer + '"', lc.TXT_ERROR_2, end='')
            answer = input().lower()
        else:
            if answer in color_names:
                color = color_names[answer]
                list_of_colors.append(color)

    return (list_of_colors[0], list_of_colors[1])


def side_length(d):
    """
    Calculation of hexagon's side.
    :param d: hexagon's diameter
    :return: hexagon's side
    """
    side = d / 2 / math.cos(math.radians(30))
    return side


def d_length(n):
    """
    Calculation of hexagon's diameter.
    :param n: number of hexagons in one side
    :return: hexagon's diameter
    """
    d = 500 / (n + 0.5)
    return d


def draw_hexagon(x, y, side_len, color):
    """
    Drawing one hexagon.
    :param x: x coordinate
    :param y: y coordinate
    :param side_len: hexagon's side
    :param color: color of hexagon
    :return: None
    """
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
    """
    Drawing row of hexagons with interchangeable colors.
    :param x: x coordinate
    :param y: y coordinate
    :param d: hexagon's diameter
    :param s: hexagon's side
    :param number: number of hexagons in one side
    :param color_1: the first color of hexagon
    :param color_2: the second color of hexagon
    :return: None
    """
    for i in range(number):
        if i % 2 == 0:
            color = color_1
        else:
            color = color_2
        draw_hexagon(x + d / 2, y, s, color)
        x += d


def fill_space(x, y, d, s, number, color_1, color_2, ptr):
    """
    Filling space by rows of hexagons.
    :param x: x coordinate
    :param y: y coordinate
    :param d: hexagon's diameter
    :param s: hexagon's side
    :param number: number of hexagons in one side
    :param color_1: the first color of hexagon
    :param color_2: the second color of hexagon
    :param ptr: supportive variable for color rotations
    :return: None
    """
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
    color_1, color_2 = get_color_choice()
    fill_space(-250, 250, d_length(hexagon_number), side_length(d_length(hexagon_number)), hexagon_number, color_1,
               color_2, 1)
    t.done()


language = input('Choose your language:\n1. English\n2. Russian\n').lower()
while True:
    if language == 'english' or language == 'eng' or \
            language == 'e' or language == '1':
        import lc_eng as lc

        break
    elif language == 'russian' or language == 'rus' or \
            language == 'r' or language == '2':
        import lc_rus as lc

        break
    language = input('Please, choose language from proposed: ')

print()
main()
