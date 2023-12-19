from datetime import datetime
from PIL import Image, ImageDraw

from constantes.enums import Cara
from constantes import colores
from modelos.cubo import Cubo

# donde guardar las imágenes
RUTA = './imagenes/cubos'

# a qué posiciónes se empezará a dibujar las caras
OFFSETS_X = {
    Cara.U: 1, Cara.D: 1, Cara.F: 1, Cara.B: 3, Cara.R: 2, Cara.L: 0
}
OFFSETS_Y = {
    Cara.U: 0, Cara.D: 2, Cara.F: 1, Cara.B: 1, Cara.R: 1, Cara.L: 1
}

# tamaño de un cubito
BLOQUE = 50

PADDING = 2

# cuantos bloques de ancho y altura tomará la imagen
ANCHO = 4
ALTURA = 3

def imprimir_cubo(cubo: Cubo):
    """
    Dado un cubo, produce una imagen PNG con el estado del cubo en 2D.
    El archivo tendrá el nombre "cubo_{AAAAMMDD}_{HHMMSS}.png", por ejemplo
    "cubo_20231218_213301.png"
    """
    ancho = PADDING + (cubo.dimension * ANCHO)
    altura = PADDING + (cubo.dimension * ALTURA)

    ancho_px = ancho * BLOQUE
    altura_px = altura * BLOQUE

    # crear imagen
    imagen = Image.new('RGB', (ancho_px, altura_px), colores.VERDE_2)

    # dibujar el cubo en el imagen
    for cara in Cara:
        offset_x = OFFSETS_X[cara] * cubo.dimension + 1
        offset_y = OFFSETS_Y[cara] * cubo.dimension + 1
        dibujar_cara(imagen, cubo, cara, (offset_x, offset_y))

    # guardar imagen
    nombre = f'{RUTA}/cubo_{get_fecha()}.png'
    imagen.save(nombre)
    imagen.show()


def dibujar_cara(
        image: Image.Image, cubo: Cubo, cara: Cara, offset: tuple[int, int]
    ):
    """
    En la image dada, dibuja la cara dada del cubo empezando en los
    bloques indicado por el offset.
    :param offset tendrá la forma (offset_x, offset_y)
    """
    cuadrado = cubo.get_cara(cara)

    for y, fila in enumerate(cuadrado):
        for x, cubito in enumerate(fila):
            color = colores.COLORES_DE_CUBO[cubito]
            offset_x = offset[0] + x
            offset_y = offset[1] + y
            dibujar_cuadrado(image, offset_x, offset_y, color)


def dibujar_cuadrado(image: Image.Image, x: int, y: int, color):
    """
    En la image dada, dibuja un cuadrado en el bloque indicado por
    las coordenadas dadas como x, y
    """
    inicio = (x * BLOQUE, y * BLOQUE)
    fin = ((x+1) * BLOQUE, (y+1) * BLOQUE)

    draw = ImageDraw.Draw(image)
    draw.rectangle((inicio, fin), fill=color, outline='black', width=2)


def get_fecha():
    return datetime.now().strftime("%Y%m%d_%H%M%S")