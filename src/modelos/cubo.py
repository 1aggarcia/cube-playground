import copy
import numpy as np

from constantes.enums import Cara
from modelos.movimiento import Movimiento, movimiento_de_texto
import modelos.cubo_operaciones as op
# from modelos.validador_de_cubo import validar_caras

class Cubo:
    """
    Modelo para un cubo de Rubik con 6 caras.
    No se recomienda crear directamente con el constructor.
    Use generar_cubo() o crear_cubo_de_texto().
    Las caras son:
    * U (up) - de arriba
    * D (down) - de abajo
    * F (front) - el frente
    * B (back) - el reverso
    * L (left) - la izquerda
    * R (right) - la derecha
    """
    # constructor
    def __init__(self,
                u: np.ndarray,
                d: np.ndarray,
                f: np.ndarray,
                b: np.ndarray,
                l: np.ndarray,
                r: np.ndarray
            ):
        # validar_caras(u, d, f, b, l, r)
        self.dimension = len(u)
        self._estado = {
            Cara.U: u,
            Cara.D: d,
            Cara.F: f,
            Cara.B: b,
            Cara.L: l,
            Cara.R: r
        }

    # métodos sobrescritos

    def __str__(self):
        resultado = ""
        for cuadrado in self._estado.values():
            # vuelta nxn
            for fila in cuadrado:
                for columna in fila:
                    resultado += f'[{columna.value}]'
                resultado += '\n'
            resultado += '\n'

        return resultado

    # métodos

    def get_cara(self, cara: Cara):
        """
        Retorna una copia de la cara espesificada en el cubo
        """
        return copy.deepcopy(self._estado[cara])

    def get_estado(self):
        """
        Retorna una copia del estado de cubo
        """
        return copy.deepcopy(self._estado)

    def _set_cara(self, cara: Cara, matriz: np.ndarray):
        self._estado[cara] = matriz

    def ejecutar_algoritmo(self, algorithmo: list[str]):
        """
        Dado una lista de texto representando movimientos,
        ejecuta cada movimiento en el cubo.
        * requiere que cada elemento sea una representación válida de un movimiento
        """
        for mov in algorithmo:
            self.mover(movimiento_de_texto(mov))

    def mover(self, mov: Movimiento):
        if mov.nivel == 1:
            # solo giramos la cara si nivel = 1
            cara_girado = op.girar_matriz(self._estado[mov.cara], mov.direccion)
            self._set_cara(mov.cara, cara_girado)

        horario = bool(mov.direccion == 1)
        direccion = mov.direccion
        linea = mov.nivel - 1
        if mov.cara in [Cara.D, Cara.B, Cara.R]:
            # estas caras giran con la orden de referencia
            horario = not horario
            linea = self.dimension - mov.nivel
            if direccion != 2:
                # para evitar -2 como dirección
                direccion = mov.direccion * -1

        if mov.cara in [Cara.U, Cara.D]:
            # caras horizontales
            self._estado = op.cotar_horizontalmente(
                self._estado, linea, direccion)
        elif mov.cara in [Cara.L, Cara.R]:
            # caras verticales
            self._estado = op.cotar_verticalmente(
                self._estado, linea, direccion)
        else:
            # caras fronterizas
            self._estado = op.cortar_frontera(
                self._estado, linea, direccion)


# métodos públicos

def copiar_cubo(cubo: Cubo):
    """
    Genera una copia del cubo
    """
    return Cubo(
        u = cubo.get_cara(Cara.U),
        d = cubo.get_cara(Cara.D),
        f = cubo.get_cara(Cara.F),
        b = cubo.get_cara(Cara.B),
        l = cubo.get_cara(Cara.L),
        r = cubo.get_cara(Cara.R),
    )


def crear_cubo_de_texto(
            u: list[list[str]],
            d: list[list[str]],
            f: list[list[str]],
            b: list[list[str]],
            l: list[list[str]],
            r: list[list[str]]
        ):
    """
    Crear un cubo dado matrices de tipo str
    * requiere que cada str sea una Etiqueta válida
    """
    return Cubo(
        u = _convertir_a_caras(u),
        d = _convertir_a_caras(d),
        f = _convertir_a_caras(f),
        b = _convertir_a_caras(b),
        r = _convertir_a_caras(r),
        l = _convertir_a_caras(l),
    )


def generar_cubo(dimension: int):
    """
    Genera cubo nxnxn resuelto de la dimension dado
    """
    caras = {}

    for c in Cara:
        caras[c] = np.full((dimension, dimension), c)

    return Cubo(
        u=caras[Cara.U],
        d=caras[Cara.D],
        f=caras[Cara.F],
        b=caras[Cara.B],
        l=caras[Cara.L],
        r=caras[Cara.R],
    )


def generar_matriz_de_cara(cara: Cara, dimension: int):
    """
    crea un matriz nxn llenada con la cara dada
    * param dimension - n
    * requiere que dimension >= 2
    """
    if dimension < 2:
        raise ValueError(f'dimension < 2: {dimension}')

    return np.full((dimension, dimension), cara)


# métodos privados

def _convertir_a_caras(lista: list[list[str]]):
    """
    Dado una matriz de cadenas de str,
    devolver una matriz de tipo Cara
    * requiere que cada str sea una Cara válida con dimensión nxn
    """
    dimension = len(lista)
    resultado = np.full((dimension, dimension), None)

    # popular resultado con la traducción str -> Etiqueta
    for x, fila in enumerate(lista):
        if len(fila) != dimension:
            raise ValueError('matriz no tiene dimensiones nxn')
        for y, texto_cara in enumerate(fila):
            resultado[x, y] = Cara[texto_cara]

    return resultado
