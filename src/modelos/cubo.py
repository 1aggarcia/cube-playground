import numpy as np

from constantes.enums import Cara
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
        return self._estado[cara]

    def _set_cara(self, cara: Cara, matriz: np.ndarray):
        self._estado[cara] = matriz

    def movimiento_u(self, horario: bool):
        orientacion = 1 if horario else -1

        cara_girado = op.girar_matriz(self.get_cara(Cara.U), orientacion)
        self._set_cara(Cara.U, cara_girado)
        self._estado = op.cotar_horizontalmente(self._estado, 0, horario)

        print('U') if horario else print("U'")

    def movimiento_d(self, horario: bool):
        orientacion = 1 if horario else -1

        cara_girado = op.girar_matriz(self.get_cara(Cara.D), orientacion)
        self._set_cara(Cara.D, cara_girado)
        self._estado = op.cotar_horizontalmente(
            self._estado, self.dimension - 1, not horario)

        print('D') if horario else print("D'")

    def movimiento_r(self, horario: bool):
        orientacion = 1 if horario else -1

        cara_girado = op.girar_matriz(self.get_cara(Cara.R), orientacion)
        self._set_cara(Cara.R, cara_girado)
        self._estado = op.cotar_verticalmente(
            self._estado, self.dimension - 1, not horario)

        print('R') if horario else print("R'")

    def movimiento_l(self, horario: bool):
        orientacion = 1 if horario else -1

        cara_girado = op.girar_matriz(self.get_cara(Cara.L), orientacion)
        self._set_cara(Cara.L, cara_girado)
        self._estado = op.cotar_verticalmente(self._estado, 0, horario)

        print('L') if horario else print("L'")

    def movimiento_f(self, horario: bool):
        orientacion = 1 if horario else -1

        cara_girado = op.girar_matriz(self.get_cara(Cara.F), orientacion)
        self._set_cara(Cara.F, cara_girado)
        self._estado = op.cortar_frontera(self._estado, 0, horario)

        print('F') if horario else print("F'")

    def movimiento_b(self, horario: bool):
        orientacion = 1 if horario else -1

        cara_girado = op.girar_matriz(self.get_cara(Cara.B), orientacion)
        self._set_cara(Cara.B, cara_girado)
        self._estado = op.cortar_frontera(
            self._estado, self.dimension - 1, not horario)

        print('F') if horario else print("F'")


# métodos públicos

def copiar_cubo(cubo: Cubo):
    """
    Genera una copia del cubo
    """
    return Cubo(
        u = cubo.get_cara(Cara.U).copy(),
        d = cubo.get_cara(Cara.D).copy(),
        f = cubo.get_cara(Cara.F).copy(),
        b = cubo.get_cara(Cara.B).copy(),
        l = cubo.get_cara(Cara.L).copy(),
        r = cubo.get_cara(Cara.R).copy(),
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
