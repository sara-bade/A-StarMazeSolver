import math


# noinspection PyAttributeOutsideInit
class AStar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = 0

    def set_heuristic(self, h):
        self.h = h

    def set_g_value(self, g):
        self.g = g

    def calculate_f_value(self):
        self.f = self.g + self.h

    def calculate_g_value(self, next_value):
        self.g += + next_value

    def calculate_h_value(self, destination_x, destination_y):
        x = self.x
        y = self.y
        self.h = math.sqrt((x - destination_x) ** 2 + (y - destination_y) ** 2)
