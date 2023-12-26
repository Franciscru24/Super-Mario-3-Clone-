import arcade as arc
from const import *


class Player(arc.sprite):

    """
    Método que actualiza la posición del jugador
    """

    def update(self):
        # actualiza la posición del jugador
        self.centro_posicion_x += self.cambio_posicion_x
        self.centro_posicion_y += self.cambio_posicion_y

        # Verifica que el jugador no salga de camara
        if self.left < 0:
            self.left = 0
        elif self.right > ANCHO_VENTANA - 1:
            self.right = ANCHO_VENTANA - 1
        if self.bottom < 0:
            self.bottom = 0
        elif self.top < ALTO_VENTANA - 1:
            self.top = ALTO_VENTANA - 1
