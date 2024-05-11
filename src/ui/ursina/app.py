from ursina import EditorCamera, Ursina, Vec3, Entity
from modelos.cubo3d import Cubo3d
from modelos.movimiento import Movimiento, invertir_movimiento
from modelos.estado_ursina import EstadoUrsina
from util.scrambles import generar_scramble

from constantes.enums import Cara
from imagenes.impresora import imprimir_cubo


ESCALA_CAMARA = 3


def iniciar_app_ursina(dimension: int):
    aplicacion = Ursina()

    cubo = Cubo3d(dimension)

    estado = EstadoUrsina(cubo)

    escala = dimension / ESCALA_CAMARA
    camera = EditorCamera(ui_size = 1000)
    camera.scale_setter(Vec3(escala, escala, escala))

    controlador = Entity()
    controlador.input = lambda key: al_teclar(key, estado)

    aplicacion.run()


# TODO: limpiar la gestión del estado
def al_teclar(key: str, estado: EstadoUrsina):
    cubo_2d = estado.cubo.cubo_2d

    # realizar la tarea
    if key == "space":
        estado.cubo.cubo_2d.restaturar()
        estado.historial.clear()

    elif key == "s":
        scramble = generar_scramble(cubo_2d.dimension)
        cubo_2d.ejecutar_algoritmo([str(mov) for mov in scramble])
        estado.historial.extend(scramble)

    elif key == "i":
        imprimir_cubo(cubo_2d)

    elif key == "backspace" and len(estado.historial) > 0:
        mov = estado.historial.pop()
        cubo_2d.mover(invertir_movimiento(mov))

    elif key.upper() in Cara:
        direccion = -1 if "shift" in estado.teclas else 1
        mov = Movimiento(Cara[key.upper()], direccion, 1, False)

        cubo_2d.mover(mov)
        estado.historial.append(mov)

    # agregar tecla a la colección
    if " up" not in key:
        estado.teclas.add(key)
    elif key.strip(" up") in estado.teclas:
        estado.teclas.remove(key.strip(" up"))
