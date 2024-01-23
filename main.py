# Devina Kachorin et Julieta María Fonseca Nava
# 9 janvier 2024
# TP4 - Arcade

import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Les couleurs pour les formes
COLORS = [arcade.color.BABY_BLUE_EYES, arcade.color.BANANA_MANIA, arcade.color.BRILLIANT_LAVENDER, arcade.color.CELADON,
          arcade.color.COTTON_CANDY, arcade.color.DEEP_PEACH]

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.balle = []
        self.rectangle = []

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        for i in self.balle:
            i.on_draw()
        for i in self.rectangle:
            i.on_draw()

    def on_update(self, delta_time: float):
        for i in self.balle:
            i.on_update()
        for i in self.rectangle:
            i.on_update()

    # Une fonction qui gère les événements qui se déroule lors d'un clic d'une souris
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            ball = balle(random.randint(50, 750), random.randint(50, 550), 3, 3)
            self.balle.append(ball)

        if button == arcade.MOUSE_BUTTON_RIGHT:
            rect = rectangle(random.randint(100, 750), random.randint(100, 550), 5, 5, 100, 50)
            self.rectangle.append(rect)


# La classe de la balle
class balle():
    def __init__(self, posx, posy, change_x, change_y):
        self.posy = posx
        self.posx = posy
        self.change_x = change_x
        self.change_y = change_y
        self.rayon = random.randint(10, 30)
        self.color = COLORS[random.randint(0, 5)]

    def on_update(self):
        # Le déplacement de la balle dans l’écran
        self.posx += self.change_x
        self.posy += self.change_y

        # Vérifier si la balle sort des limites de la fenêtre
        if self.posx < self.rayon:
            self.change_x *= -1
        if self.posx > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1
        if self.posy < self.rayon:
            self.change_y *= -1
        if self.posy > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1

    # Dessiner la balle
    def on_draw(self):
        arcade.draw_circle_filled(self.posx, self.posy, self.rayon, self.color)


# La classe du rectangle
class rectangle():
    def __init__(self, posx, posy, change_x, change_y, largeur, hauteur):
        self.posy = posy
        self.posx = posx
        self.change_x = change_x
        self.change_y = change_y
        self.width = largeur
        self.height = hauteur
        self.color = COLORS[random.randint(0, 5)]
        self.angle = 5.5

    def on_update(self):
        # Le déplacement du rectangle sur l’écran
        self.posx += self.change_x
        self.posy += self.change_y

        # Vérifier si le rectangle sort des limites de la fenêtre
        if self.posx < (self.width / 2):
            self.change_x *= -1
        if self.posx > SCREEN_WIDTH - (self.width / 2):
            self.change_x *= -1
        if self.posy < (self.height / 2):
            self.change_y *= -1
        if self.posy > SCREEN_HEIGHT - (self.height / 2):
            self.change_y *= -1

    # Dessiner le rectangle
    def on_draw(self):
        arcade.draw_rectangle_filled(self.posx, self.posy, self.width, self.height, self.color)

# La fonction principale pour exécuter du jeu
def main():
    my_game = MyGame()
    my_game.setup()
    arcade.run()

# Un appel à la fonction principale
main()
