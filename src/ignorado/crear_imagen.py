import textwrap
from PIL import Image, ImageFont, ImageDraw

TAMANO = 100

ROJO = (256, 000, 000)
AZUL = (000, 000, 256)
VERDE = (000, 256, 000)
BLANCO = (256, 256, 256)
RANDOM = (24, 154, 100)
NEGRO = (0, 0, 0)

TEXTO = '39iu4r32948cru93rcu2h9384ruc98ewruc28989ur923807r2c38479293804728903'

font = ImageFont.truetype("arial.ttf", 25)

BLOQUE = 50
PADDING = 2

ANCHO = 4
ALTURA = 3

def crear_imagen(dimension: int):
    """
    Crea una imagen con el nombre 'imagen.png' para encajar un cubo con
    la dimensión dada
    """
    ancho = PADDING + (dimension * ANCHO)
    altura = PADDING + (dimension * ALTURA)

    ancho_px = ancho * BLOQUE
    altura_px = altura * BLOQUE

    # crear imagen
    imagen = Image.new('RGB', (ancho_px, altura_px), RANDOM)
    draw = ImageDraw.Draw(imagen)

    # dibujar lineas para dividir la imagen
    # lineas verticales
    for x in range(1, ancho):
        coords = (x * BLOQUE, 0, x * BLOQUE, altura_px)
        draw.line(coords, NEGRO, 1)

    # lineas horizontales
    for y in range(1, altura):
        coords = (0, y * BLOQUE, ancho_px, y * BLOQUE)
        draw.line(coords, NEGRO, 1)

    imagen.save('./imagen.png')
    imagen.show()

crear_imagen(3)
