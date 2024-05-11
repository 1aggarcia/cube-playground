from ursina import EditorCamera, Ursina, Vec3, Entity
from modelos.cubo3d import Cubo3d
from modelos.movimiento import Movimiento, invertir_movimiento
from modelos.operaciones import generar_scramble

from constantes.enums import Cara
from imagenes.impresora import imprimir_cubo


ESCALA_CAMARA = 3


def iniciar_app_ursina(dimension: int):
    aplicacion = Ursina()

    cubo = Cubo3d(dimension)
    teclas: set[str] = set()
    historial: list[Movimiento] = []

    escala = dimension / ESCALA_CAMARA
    camera = EditorCamera(ui_size = 1000)
    camera.scale_setter(Vec3(escala, escala, escala))

    controlador = Entity()
    controlador.input = lambda key: al_teclar(key, cubo, teclas, historial)

    aplicacion.run()


# TODO: limpiar la gestión del estado
def al_teclar(key: str, cubo: Cubo3d, teclas: set[str], historial: list[Movimiento]):
    # realizar la tarea
    if key == "space":
        cubo.cubo_2d.restaturar()
        historial.clear()

    elif key == "s":
        scramble = generar_scramble(cubo.cubo_2d.dimension)
        cubo.cubo_2d.ejecutar_algoritmo([str(mov) for mov in scramble])
        historial.extend(scramble)

    elif key == "i":
        imprimir_cubo(cubo.cubo_2d)

    elif key == "backspace" and len(historial) > 0:
        mov = historial.pop()
        cubo.cubo_2d.mover(invertir_movimiento(mov))

    elif key.upper() in Cara:
        direccion = -1 if "shift" in teclas else 1
        mov = Movimiento(Cara[key.upper()], direccion, 1, False)

        cubo.cubo_2d.mover(mov)
        historial.append(mov)

    # agregar tecla a la colección
    if " up" not in key:
        teclas.add(key)
    elif key.strip(" up") in teclas:
        teclas.remove(key.strip(" up"))
