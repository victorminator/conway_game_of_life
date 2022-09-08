from constantes import *

class Cell:
    def __init__(self, source, row, column, state):
        self.x = column
        self.y = row
        self.state = state
        self.next_state = state
        self.color = (0, 255, 0) if self.state == ALIVE else (255, 255, 255)
        self.source_array = source

    def __str__(self):
        m1 = "en vie" if self.state == ALIVE else "morte"
        m2 = "en vie" if self.state == ALIVE else "morte"
        return f"cellule ({self.x}, {self.y}) {m1}; {m2}"
    
    def trouve_voisins(self):
        cellules_voisines = []
        for x in range(-1, 2, 1):
            for y in range(-1, 2, 1):
                cell = (self.y +  y, self.x + x)
                if cell != (self.y, self.x) and cell[0] >= 0 and cell[0] < len(self.source_array) and cell[1] >= 0 and cell[1] < len(self.source_array):
                    cellules_voisines.append(cell)
        return cellules_voisines

    def compte_voisins(self):
        emplacements_voisins = self.trouve_voisins()
        voisins = [self.source_array[emp[0]][emp[1]] for emp in emplacements_voisins if self.source_array[emp[0]][emp[1]].state == ALIVE]
        return len(voisins)

    def get_new_state(self):
        nb_voisins = self.compte_voisins()
        if nb_voisins == 3:
            self.next_state = ALIVE
            if self.state == DEAD:
                self.color = (0, 255, 0)
            else:
                self.color = (0, 0, 255)
        elif nb_voisins == 2 and self.state == ALIVE:
            self.next_state = ALIVE
            self.color = (0, 0, 255)
        else:
            self.next_state = DEAD
            if self.state == ALIVE:
                self.color = (255, 0, 0)
            else:
                self.color = (255, 255, 255)

    def update_state(self):
        self.state = self.next_state