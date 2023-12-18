from constantes.enums import Cara

class Movimiento:
    """
    Objeto que define un movimiento del cubo. No se debería modificar.
    El movimiento es definido por:
    * cara - la cara que girará
    * direccion - número de rotaciones de 90 degrados de capa.
        Debe ser 1 por un movimiento en sentido horario, -1 por uno en
        sentido antihorario, o 2 para uno doble
    * nivel - cuantas capas de profundidad quieres girar. 1 es solo la cara.
        Debe ser menos de la dimension del cubo
    * ancho - True si quieres girar cada capa entre la cara y el nivel,
        False si solo quieres girar la capa al nivel dado.
    """
    def __init__(self, cara: Cara, direccion: int, nivel: int, ancho: bool):
        if (direccion != 1 and direccion != -1 and direccion != 2):
            raise ValueError('direccion no es ni 1, ni -1, ni 2')

        self.cara = cara
        self.direccion = direccion
        self.nivel = nivel
        self.ancho = ancho

    def __eq__(self, __value: object) -> bool:
        return (
            isinstance(__value, Movimiento) and
            self.cara == __value.cara and
            self.direccion == __value.direccion and
            self.ancho == __value.ancho
        )

    def __str__(self):
        resultado = self.cara.value

        if self.ancho:
            # un movimiento ancho: U -> Uw
            resultado += 'w'

        if self.direccion == -1:
            # un movimiento primo: U -> U' o Uw -> Uw'
            resultado += "'"
        elif self.direccion == 2:
            # un movimiento doble: U -> U2 o Uw -> Uw2
            resultado += "2"

        if self.nivel > 1:
            # un movimiento de múltiples capas: U -> 3U o Uw' -> 3Uw' etc.
            resultado = str(self.nivel) + resultado

        return resultado
