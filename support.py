from constantes import ORIGINE

def square_pos(length, column, row):
    pos_x = ORIGINE[0] + length * column
    pos_y = ORIGINE[1] - length * row
    return pos_x, pos_y