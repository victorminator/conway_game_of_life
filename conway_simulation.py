import turtle
from cellclass import Cell
from constantes import *
from datafixing import ajuste_structure   
from support import square_pos
from turtletools import SuperTurtle 

CHOSEN_FILE = "exemple.txt"

def draw_config(length, first_config=False):
    crayon.clear()
    for y in range(length):
        rangee = []
        for x in range(length):
            pos = square_pos(cote_cell, x, y)
            if first_config:
                cellule_actuelle = Cell(grille, y, x, int(game_configuration[y][x]))
            else:    
                cellule_actuelle = grille[y][x]
            remplissage = cellule_actuelle.color
            crayon.carre(pos, cote_cell, initial_angle=270, fill=remplissage)
            if first_config:
                rangee.append(cellule_actuelle)
        if first_config:
            grille.append(rangee.copy())
            rangee.clear()
    screen.update()
            

with open(CHOSEN_FILE) as fic_desc:
    game_configuration = fic_desc.readlines() # Valid

ajuste_structure(game_configuration, str(DEAD))

grille = []
len_grille = len(game_configuration)
cote_cell = DIMENSION_TABLEAU / len_grille

screen = turtle.Screen()
crayon = SuperTurtle()
turtle.tracer(0)
turtle.colormode(255)

draw_config(len_grille, first_config=True)

while True:
    for cell_list in grille:
        for cell_object in cell_list:
            cell_object.get_new_state()
    for cell_list in grille:
        for cell_object in cell_list:
            cell_object.update_state()
    draw_config(len_grille)