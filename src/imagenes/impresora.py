from PIL import Image, ImageDraw

from constantes.enums import Cara
from constantes import colores
from modelos.cubo import Cubo

OFFSETS_X = {
    Cara.U: 1, Cara.D: 1, Cara.F: 1, Cara.B: 3, Cara.R: 2, Cara.L: 0
}
OFFSETS_Y = {
    Cara.U: 0, Cara.D: 2, Cara.F: 1, Cara.B: 1, Cara.R: 1, Cara.L: 1
}

BLOQUE = 50
PADDING = 2

ANCHO = 4
ALTURA = 3

def imprimir_cubo(cubo: Cubo):
    ancho = PADDING + (cubo.dimension * ANCHO)
    altura = PADDING + (cubo.dimension * ALTURA)

    ancho_px = ancho * BLOQUE
    altura_px = altura * BLOQUE

    # crear imagen
    imagen = Image.new('RGB', (ancho_px, altura_px), colores.VERDE_2)
    draw = ImageDraw.Draw(imagen)

    # dibujar el cubo en el imagen
    for cara in Cara:
        offset_x = OFFSETS_X[cara] * cubo.dimension + 1
        offset_y = OFFSETS_Y[cara] * cubo.dimension + 1
        dibujar_cara(draw, cubo, cara, offset_x, offset_y)

    # guardar imagen
    imagen.save('./imagenes/a.png')
    imagen.show()


def dibujar_cara(
        image_draw: ImageDraw.ImageDraw, cubo: Cubo, cara: Cara, offset_x: int, offset_y: int
    ):
    cuadrado = cubo.get_cara(cara)

    for y, fila in enumerate(cuadrado):
        for x, cubito in enumerate(fila):
            color = colores.COLORES_DE_CUBO[cubito]
            dibujar_cuadrado(image_draw, x + offset_x, y + offset_y, color)


def dibujar_cuadrado(image_draw: ImageDraw.ImageDraw, x: int, y: int, color):
    inicio = (x * BLOQUE, y * BLOQUE)
    fin = ((x+1) * BLOQUE, (y+1) * BLOQUE)

    image_draw.rectangle((inicio, fin), fill=color, outline='black', width=2)

