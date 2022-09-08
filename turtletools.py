import turtle

class SuperTurtle(turtle.Turtle):
    def __init__(self, visible=False):
        super().__init__(visible=visible)
        self.speed(0)
    
    def move(self, x, y):
        self.pu()
        self.goto(x, y)
        self.pd()

    def ligne(self, x1, y1, x2, y2):
        self.move(x1, y1)
        self.goto(x2, y2)

    def triangle_eq(self, longueur, pos=(0, 0), initial_angle=0):
        self.move(pos[0], pos[1])
        self.setheading(initial_angle)
        self.pd()
        for _ in range(3):
            self.fd(longueur)
            self.left(120)
    
    def carre(self, origine, longueur_cote, fill=(), initial_angle=0):
        self.move(origine[0], origine[1])
        self.seth(initial_angle)
        if fill:
            original_color = self.fillcolor()
            self.fillcolor(fill)
            self.begin_fill()
        for _ in range(4):
            self.fd(longueur_cote)
            self.left(90)
        if fill:
            self.end_fill()
            self.fillcolor(original_color)
    
    def croix(self, coord, cote):
        for i in range(5):
            self.move(coord[0], coord[1])
            self.setheading(45 + 90 * i)
            self.forward(cote)
    
    def rectangle(self, pos, longueur, largeur):
        self.move(pos)
        for i in range(4):
            if i % 2 == 0:
                self.fd(longueur)
            else:
                self.fd(largeur)
            self.left(90)
        


if __name__ == "__main__":
    scr = turtle.Screen()
    pn = SuperTurtle()
    pn.carre((-50, -50), 100)
    scr.exitonclick()
