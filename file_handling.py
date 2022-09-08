from os import path

def supprime_caracteres(chaine, caractere, start=0, end=-1):
    if chaine:
        copie = ""
        source = chaine[start:end]
        for char in source:
            if char != caractere:
                copie += char
        return copie
    return ""

def different_char_index(chaine, char, start=0, end=-1, step=1):
    if end == -1:
        end = len(chaine)
    if end > len(chaine) or start > len(chaine):
        return -1
    for i in range(start, end, step):
        if chaine[i] != char:
            return i
    return -1

def no_leftspaces_filename(filename):
    indice_fin = different_char_index(filename, " ")
    new_nm = supprime_caracteres(filename, " ", end=indice_fin)
    return new_nm

def is_valid_filename(source):
    if not source or source[-1] == ".":
        return False
    forbidden_chars = ["*", "/", "\\", "?", "|", ":", '"', "<", ">"]
    for char in source:
        if char in forbidden_chars:
            return False
    return True

def text_file_conversion(filename_path, data):
    text_file = open(filename_path, mode="w")
    for array in data:
        for char in array:
            text_file.write(char)
        text_file.write("\n")

def count_char(chaine, target_char):
    q = 0
    for char in chaine:
        if char == target_char:
            q += 1
    return q

def filename_if_exists(filename):
    number_suffix = ""
    number = 0
    new_name = filename
    while path.exists(new_name):
        number += 1
        number_suffix = f"({number})"
        new_name = filename + number_suffix
    return new_name