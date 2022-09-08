def max_length(str_list):
    longueur_max = 0
    for elt in str_list:
        if len(elt) > longueur_max:
            longueur_max = len(elt)
    return longueur_max

def filled_line(chaine, char, length):
    new_str = chaine + char * length
    return new_str

def filled_structure(str_list, char):
    plus_longue = max_length(str_list)
    for i in range(len(str_list)):
        len_diff = plus_longue - len(str_list[i])
        str_list[i] = filled_line(str_list[i], char, len_diff)

def rectangle_to_square(config, char):
    nb_rangees = len(config)
    nb_colonnes = len(config[0])
    if nb_rangees != nb_colonnes:
        chosen_len = nb_rangees if nb_rangees > nb_colonnes else nb_colonnes
        diff = abs(nb_colonnes - nb_rangees)
        if chosen_len == nb_rangees:
            for i in range(chosen_len):
                config[i] += char*diff
        else:
            for _ in range(diff):
                config.append(char*nb_colonnes)

def cut_last_character(chaine):
    new_string = chaine[:-1]
    return new_string

def remove_linejumps(str_list):
    for i in range(len(str_list)):
        if str_list[i][-1] == "\n":
            str_list[i] = cut_last_character(str_list[i]) # Supprime les \n : valide

def ajuste_structure(structure, char):
    remove_linejumps(structure)
    filled_structure(structure, char)
    rectangle_to_square(structure, char)