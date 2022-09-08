from random import randint
import turtle
from turtletools import SuperTurtle
from file_handling import *
from constantes import *
from support import square_pos

def ask_number(prompt):
    entree = turtle.textinput("Format grille", prompt)
    while not entree.isdigit():
        entree = turtle.textinput("Format grille", "Erreur : veuillez entrer un nombre entier positif")
    return int(entree)

def app_shutdown():
    nom_fichier = turtle.textinput("Sauvegarder fichier", "Donner un nom au nouveau fichier")
    while nom_fichier == None or not is_valid_filename(nom_fichier):
        nom_fichier = turtle.textinput("Sauvegarder fichier", "Erreur : donner un nom valide")
    nom_fichier = filename_if_exists(nom_fichier)
    text_file_conversion(nom_fichier + ".txt", grille)
    ecran.bye()

def leaving_instructions():
    pen.move(0, -280)
    pen.write("Press 's' or 'q' when you're finished", align="center", font=("Arial", 17, "bold"))

def get_location(x, y):
    fixed_y = y - ORIGINE[1]
    fixed_x = x - ORIGINE[0]
    if fixed_y > 0 or fixed_x < 0 or fixed_x > ORIGINE[0] * -2 or fixed_y < ORIGINE[1] * -2:
        return -1, -1
    row = abs(fixed_y) // cote_cell
    column = fixed_x // cote_cell
    return int(row), int(column)

def swap_status(row, column):
    statut = grille[row][column] = "1" if grille[row][column] == "0" else "0"
    return statut

def cell_change(row, column):
    statut = swap_status(row, column)
    put_square(statut, row, column)

def location_click(x, y):
    row, column = get_location(x, y) 
    if row == -1:
        return
    cell_change(row, column)
    changes.append((row, column))
    ecran.update()

def put_square(statut, row, column):
    pos = square_pos(cote_cell, column, row)
    remplissage = (255, 255, 255) if statut == "0" else (0, 255, 0)
    pen.carre(pos, cote_cell, fill=remplissage, initial_angle=270)

def random_config():
    changes.append(genuine_copy(grille))
    for i in range(dimension_format):
        for j in range(dimension_format):
            statut = grille[i][j] = str(randint(0, 1))
            put_square(statut, i, j)
    ecran.update()

def genuine_copy(list_of_lists):
    new_list = []
    for ls in list_of_lists:
        new_list.append(ls.copy())
    return new_list

def reset_config():
    if changes:
        changes.append(genuine_copy(grille))
    for y in range(dimension_format):
        for x in range(dimension_format):
            put_square("0", y, x)
            grille[y][x] = "0"
    ecran.update()

def undo():
    if changes:
        last_change = changes.pop(-1)
        if len(last_change) == 2:
            row, column = last_change
            cell_change(row, column)
        else:
            for y in range(dimension_format):
                for x in range(dimension_format):
                    put_square(last_change[y][x], y, x)
        ecran.update()
        undone.append(last_change)

def redo():
    if undone:
        last_change = undone.pop(-1)
        if len(last_change) == 2:
            row, column = last_change
            cell_change(row, column)
        else:
            for y in range(dimension_format):
                for x in range(dimension_format):
                    put_square(last_change[y][x], y, x)
        ecran.update()
        changes.append(last_change)

def swap_configuration():
    for y in range(dimension_format):
        for x in range(dimension_format):
            cell_change(y, x)
    ecran.update()

ecran = turtle.Screen()
turtle.colormode(255)
turtle.tracer(0)
pen = SuperTurtle()
ecran.bgcolor("grey")

changes = []
undone = []

dimension_format = ask_number("Entrez la longueur du tableau")
while dimension_format > MAX_FORMAT or dimension_format < MIN_FORMAT:
    text_prompt = f"Erreur : la valeur excède {MAX_FORMAT}" if dimension_format > MAX_FORMAT else f"Erreur : la valeur est inférieure à {MIN_FORMAT}"
    dimension_format = ask_number(text_prompt)

cote_cell = DIMENSION_TABLEAU / dimension_format

grille = []
for _ in range(dimension_format):
    grille.append([""]*dimension_format)

reset_config()
leaving_instructions()
turtle.listen()
ecran.onclick(location_click)
ecran.onkey(app_shutdown, key="s")
ecran.onkey(app_shutdown, key="q")
ecran.onkey(random_config, key="$")
ecran.onkey(reset_config, key="d")
ecran.onkey(redo, "y")
ecran.onkey(undo, "z")
ecran.onkey(swap_configuration, key="space")
ecran.mainloop()

