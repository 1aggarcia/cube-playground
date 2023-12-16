import textwrap
from PIL import Image, ImageFont, ImageDraw

TAMANO = 100

ROJO = (256, 000, 000)
AZUL = (000, 000, 256)
VERDE = (000, 256, 000)
BLANCO = (256, 256, 256)
RANDOM = (134, 111, 0)
NEGRO = (0, 0, 0)

TEXTO = '39iu4r32948cru93rcu2h9384ruc98ewruc28989ur923807r2c38479293804728903'

font = ImageFont.truetype("arial.ttf", 25)

# imagen = Image.new('RGB', (700, 500))
# draw = ImageDraw.Draw(imagen)

# imagen.paste(BLANCO, (0, 0, 700, 500))

# # cuadrato 2x2
# draw.rectangle((20, 20, 40, 40), VERDE, NEGRO)
# draw.rectangle((20, 40, 40, 60), VERDE, NEGRO)
# draw.rectangle((40, 20, 60, 40), VERDE, NEGRO)
# draw.rectangle((40, 40, 60, 60), VERDE, NEGRO)

# draw.text((5, 5), "\n".join(textwrap.wrap(TEXTO, width=2)), NEGRO, font)

# imagen.save('./imagen.png')
# imagen.show()

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
    imagen = Image.new('RGB', (ancho_px, altura_px))
    imagen.paste(RANDOM, (0, 0, ancho_px, altura_px))
    draw = ImageDraw.Draw(imagen)

    # dibujar lineas para dividir la imagen
    for i in range(1, ancho):
        coords = (i * BLOQUE, 0, i * BLOQUE, altura_px)
        draw.line(coords, NEGRO, 1)

    for i in range(1, altura_px):
        coords = (0, i * BLOQUE, ancho_px, i * BLOQUE)
        draw.line(coords, NEGRO, 1)

    imagen.save('./imagen.png')
    #imagen.show()

crear_imagen(3)
