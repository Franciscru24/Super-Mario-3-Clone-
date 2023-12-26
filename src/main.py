from const import *
import arcade as arc

""" 
Clase principal del Juego 
"""


class superMarioGame(arc.Window):
    """
    Función de inicialización
    """

    def __init__(self):
        # Constructor de la ventana
        super().__init__(ANCHO_VENTANA, ALTO_VENTANA, TITULO_VENTANA)
        arc.set_background_color(arc.csscolor.CORNFLOWER_BLUE)

        # Inicialización de la variable para el motor de fisica
        self.motor_de_fisicas = None

        # Inicialización de la scena que contendran las sprites y objetos de colisión
        self.sprites = None

        # Inicialización de una camara para seguir al personaje
        self.camera = None

    """
    Función de configuración
    """

    def setup(self):
        # Definiendo la cámara
        self.camera = arc.Camera(self.width, self.height)

        # Definiendp los atributos
        self.sprites = arc.Scene()

        # Definiendo el sprite del jugador
        self.sprite_jugador = arc.Sprite(JUGADOR, ESCALA_PERSONAJE)
        self.sprite_jugador.center_x = 280
        self.sprite_jugador.center_y = 550
        self.sprites.add_sprite("Jugador", self.sprite_jugador)

        # Definiendo la posición de los tubos
        for pos in POSICION_TUBOS:
            tubo = arc.Sprite(TUBO, ESCALA_TUBO)
            tubo.position = pos
            self.sprites.add_sprite("Paredes", tubo)

        # Definiendo la posición del piso
        for i in range(0, 1000, 500):
            piso = arc.Sprite(PISO, ESCALA_PISO)
            piso.center_x = i
            piso.center_y = 200
            self.sprites.add_sprite("Paredes", piso)

        # Definiendo un motor de fisicas simple
        self.motor_de_fisicas = arc.PhysicsEnginePlatformer(
            self.sprite_jugador,
            gravity_constant=GRAVEDAD,
            walls=self.sprites["Paredes"],
        )

        # Bandera sobre el estado de las teclas presionadas
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    """
    Función de renderizado
    """

    def on_draw(self):
        # Limpia la ventana
        self.clear()

        # Activación de la cámara
        self.camera.use()

        # Dibuja los sprites en la ventana
        self.sprites.draw()

    """
    Funciones para controlar el movimiento del jugador
    """

    def actualiza_movimiento_jugador(self):
        self.sprite_jugador.change_x = 0
        self.sprite_jugador.change_y = 0

        if self.up_pressed and not self.down_pressed:
            # self.sprite_jugador.change_y = VELOCIDAD_MOVIMIENTO_JUGADOR
            if self.motor_de_fisicas.can_jump():
                self.sprite_jugador.change_y = VELOCIDAD_SALTO_JUGADOR
        elif self.down_pressed and not self.up_pressed:
            self.sprite_jugador.change_y = -VELOCIDAD_MOVIMIENTO_JUGADOR
        elif self.right_pressed and not self.left_pressed:
            self.sprite_jugador.change_x = VELOCIDAD_MOVIMIENTO_JUGADOR
        elif self.left_pressed and not self.right_pressed:
            self.sprite_jugador.change_x = -VELOCIDAD_MOVIMIENTO_JUGADOR

    def on_key_press(self, key, modifiers):
        if key == arc.key.UP or key == arc.key.W:
            self.up_pressed = True
            self.actualiza_movimiento_jugador()
        elif key == arc.key.DOWN or key == arc.key.S:
            self.down_pressed = True
            self.actualiza_movimiento_jugador()
        elif key == arc.key.RIGHT or key == arc.key.D:
            self.right_pressed = True
            self.actualiza_movimiento_jugador()
        elif key == arc.key.LEFT or key == arc.key.A:
            self.left_pressed = True
            self.actualiza_movimiento_jugador()

    def on_key_release(self, key, modifiers):
        if key == arc.key.UP or key == arc.key.W:
            self.up_pressed = False
            self.actualiza_movimiento_jugador()
        elif key == arc.key.DOWN or key == arc.key.S:
            self.down_pressed = False
            self.actualiza_movimiento_jugador()
        elif key == arc.key.RIGHT or key == arc.key.D:
            self.right_pressed = False
            self.actualiza_movimiento_jugador()
        elif key == arc.key.LEFT or key == arc.key.A:
            self.left_pressed = False
            self.actualiza_movimiento_jugador()

    """
    Función que actualiza la camara del juego
    """

    def centrar_camara(self):
        centro_camara_x = self.sprite_jugador.center_x - (
            self.camera.viewport_width / 2
        )
        centro_camara_y = self.sprite_jugador.center_y - (
            self.camera.viewport_height / 2
        )

        # Verifica que la camara no salga de las dimensiones de la ventana
        if centro_camara_x < 0:
            centro_camara_x = 0
        if centro_camara_y < 0:
            centro_camara_y = 0

        centro_camara = [centro_camara_x, centro_camara_y]

        self.camera.move_to(centro_camara)

    """
    Función que actualiza el motor de fisicas
    """

    def on_update(self, delta_time):
        # Establece y actualiza el motor de físicas
        self.motor_de_fisicas.update()

        # Establece y actualiza la camara del jugador
        self.centrar_camara()


"""
Función principal
"""


def main():
    ventana = superMarioGame()
    ventana.setup()
    arc.run()


"""
Validación de ejecución de programa
"""

if __name__ == "__main__":
    main()
