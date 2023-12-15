from PIL import Image

TAMANO = 100

ROJO = (256, 000, 000)
AZUL = (000, 256, 000)
VERDE = (000, 000, 256)
BLANCO = (256, 256, 256)

imagen = Image.new('RGB', (700, 500))

imagen.paste(BLANCO, (0, 0, 700, 500))

imagen.paste(VERDE, (TAMANO, TAMANO, TAMANO * 2, TAMANO * 2))
imagen.paste(ROJO, (TAMANO * 2, TAMANO * 2, TAMANO * 3, TAMANO * 3))
imagen.paste(AZUL, (TAMANO * 3, TAMANO * 3, TAMANO * 4, TAMANO * 4))

imagen.save('./imagen.png')
imagen.show()

