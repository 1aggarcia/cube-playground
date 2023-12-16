import textwrap
from PIL import Image, ImageFont, ImageDraw

TAMANO = 100

ROJO = (256, 000, 000)
AZUL = (000, 000, 256)
VERDE = (000, 256, 000)
BLANCO = (256, 256, 256)
NEGRO = (0, 0, 0)

TEXTO = '39iu4r32948cru93rcu2h9384ruc98ewruc28989ur923807r2c38479293804728903'

font = ImageFont.truetype("arial.ttf", 25)

imagen = Image.new('RGB', (700, 500))
draw = ImageDraw.Draw(imagen)

imagen.paste(BLANCO, (0, 0, 700, 500))

# cuadrato 2x2
draw.rectangle((20, 20, 40, 40), VERDE, NEGRO)
draw.rectangle((20, 40, 40, 60), VERDE, NEGRO)
draw.rectangle((40, 20, 60, 40), VERDE, NEGRO)
draw.rectangle((40, 40, 60, 60), VERDE, NEGRO)

draw.text((5, 5), "\n".join(textwrap.wrap(TEXTO, width=2)), NEGRO, font)

imagen.save('./imagen.png')
imagen.show()
