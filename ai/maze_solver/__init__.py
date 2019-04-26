import turtle
import time

from ai.maze_solver.a_star import AStar
from ai.maze_solver.draw_pen import Pen

wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Maze')
wn.setup(700, 700)

blocked = list()
unblocked = list()
open_list = list()
closed_list = list()
source = (1, 0)
destination = (22, 22)
a_star_list = list()

object_dict = dict()

all_data = list()

test =list()

_maze = [
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "                      X",
    "XX XXXX XXXXXXXXXXXXX X",
    "XX XXXX XXXXXXXXXXXXX X",
    "XX XXXX     XXXXXXXXX X",
    "XX XXXX XXX XXXXXXXXX X",
    "XX XXXX XXX XXXXXXXXX X",
    "XX XXXX XXX XXXXXXXXX X",
    "XX XXXX XXX      XXXX X",
    "XX XXXX XXXXXXXXX XXX X",
    "XX XXXX XXXXXXXXX XXX X",
    "XX XXXX XXXXXXXXX XXX X",
    "XX XXXX XXXXXXXXX XXX X",
    "XX XXXX XXXXXXXXX XXX X",
    "XX XXXX XXXXXXXXX XXX X",
    "XX XXXX XXXXXXXXX XXX X",
    "XX XXXX       XXX XXX X",
    "XX XXXX XXXXXX XX XXX X",
    "XX XXXX XXXXXX XX XXX X",
    "XX XXXX XXXXXX XX XXX X",
    "XX XXXX XXXXXX XX XXX X",
    "XX XXXX XXXXXX XX XXX X",
    "XXX    X               ",
    "XXXXXXXXXXXXXXXXXXXXXXX"
]


def setup_maze(level):
    for y in range(len(level[0])):
        for x in range(len(level)):
            character = level[x][y]
            screen_x = -288 + (y * 24)
            screen_y = 288 - (x * 24)
            all_data.append(str(x) + ' ' + str(y))
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                blocked.append(str(x) + ' ' + str(y))
            else:
                unblocked.append(str(x) + ' ' + str(y))
                a_star_obj = AStar(x, y)
                a_star_obj.calculate_h_value(destination[0], destination[1])
                a_star_list.append(a_star_obj)
                object_dict.update({str(x) + ' ' + str(y): a_star_obj})


def find_successors(x, y):
    adj_matrix_ = list()

    right_x = x
    right_y = y + 1

    adj_matrix_.append(str(right_x) + ' ' + str(right_y))

    # if str(right_x) + ' ' + str(right_y) in unblocked:
    #     screen_x = -288 + (right_y * 24)
    #     screen_y = 288 - (right_x * 24)
    #     pen.goto(screen_x, screen_y)
    #     pen.color('red')
    #     pen.stamp()

    left_x = x
    left_y = y - 1

    adj_matrix_.append(str(left_x) + ' ' + str(left_y))

    up_x = x - 1
    up_y = y

    adj_matrix_.append(str(up_x) + ' ' + str(up_y))

    down_x = x + 1
    down_y = y

    adj_matrix_.append(str(down_x) + ' ' + str(down_y))

    return adj_matrix_


def traverse(x, y):
    print('Moving to (' + str(x) + ',' + str(y) + ')')

    temp = list()

    screen_x = -288 + (int(y) * 24)
    screen_y = 288 - (int(x) * 24)
    pen.goto(screen_x, screen_y)
    pen.color('blue')
    pen.stamp()
    time.sleep(0.25)

    closed_list.append(object_dict.get(str(x) + ' ' + str(y)))

    if object_dict.get(str(x) + ' ' + str(y)) in open_list:
        while object_dict.get(str(x) + ' ' + str(y)) in open_list:
            open_list.remove(object_dict.get(str(x) + ' ' + str(y)))

    adj_matrix = find_successors(int(x), int(y))

    for data in adj_matrix:
        if data in unblocked and object_dict.get(data) not in closed_list:
            temp.append(data)

    for data in temp:
        object_dict.get(data).calculate_g_value(10)
        object_dict.get(data).calculate_f_value()
        open_list.append(object_dict.get(data))

    smallest_f = get_smallest(open_list)

    if int(x) == destination[0] and int(y) == destination[1]:
        # turtle.penup()
        # turtle.goto(-150, 300)
        # turtle.color('white')
        # turtle.write("MAZE SLOVED", move=False, font=("Arial", 30, "normal"))
        # turtle.hideturtle()

        return

    return traverse(smallest_f.x, smallest_f.y)


def get_smallest(f_value_matrix):
    min_value = f_value_matrix[0].f
    index = 0
    for i in range(1, len(f_value_matrix)):
        if min_value > f_value_matrix[i].f:
            min_value = f_value_matrix[i].f
            index = i
    return f_value_matrix[index]


if __name__ == '__main__':

    pen_obj = Pen()
    pen = pen_obj.get_pen()

    setup_maze(_maze)
    traverse(source[0], source[1])

    turtle.done()
    while True:
        pass
