import copy
import numpy as np

from constantes.enums import Cara
# from modelos.validador_de_cubo import validar_caras

# el ciclo que siguen las caras al hacer el movimiento U
CARAS_HORIZONTALES = [Cara.F, Cara.L, Cara.B, Cara.R]

# el ciclo que siguen las caras al hacer el movimiento L
CARAS_VERTICALES = [Cara.F, Cara.D, Cara.B, Cara. U]

# el ciclo que siguen las caras al hacer el movimiento F
CARAS_FRONTERIZAS = [Cara.U,  Cara.R, Cara.D, Cara.L]

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

    def movimiento_u(self):
        cara_girado = _girar_matriz_horario(self.get_cara(Cara.U))
        self._set_cara(Cara.U, cara_girado)
        self._estado = _cotar_horizontalmente(self, 0, True)

    def movimiento_u_prima(self):
        cara_girado = _girar_matriz_antihorario(self.get_cara(Cara.U))
        self._set_cara(Cara.U, cara_girado)
        self._estado = _cotar_horizontalmente(self, 0, False)

    def movimiento_l(self):
        cara_girado = _girar_matriz_horario(self.get_cara(Cara.L))
        self._set_cara(Cara.L, cara_girado)
        self._estado = _cotar_verticalmente_horario(self, 0)

    def movimiento_l_prima(self):
        cara_girado = _girar_matriz_antihorario(self.get_cara(Cara.L))
        self._set_cara(Cara.L, cara_girado)
        self._estado = _cotar_verticalmente_antihorario(self, 0)


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


# los métodos que giran las matrices

def _girar_matriz_horario(matriz: np.ndarray):
    #return np.fliplr(matriz.transpose())
    return np.rot90(matriz, axes=(1, 0))


def _girar_matriz_antihorario(matriz: np.ndarray):
    #return np.flipud(matriz.transpose())
    return np.rot90(matriz, axes=(0, 1))


def _cotar_horizontalmente_horario(cubo: Cubo, fila: int) -> dict[Cara, np.ndarray]:
    return _cotar_horizontalmente(cubo, fila, True)


def _cotar_horizontalmente_antihorario(cubo: Cubo, fila: int) -> dict[Cara, np.ndarray]:
    return _cotar_horizontalmente(cubo, fila, False)


def _cotar_verticalmente_horario(cubo: Cubo, fila: int) -> dict[Cara, np.ndarray]:
    return _cotar_verticalmente(cubo, fila, True)


def _cotar_verticalmente_antihorario(cubo: Cubo, fila: int) -> dict[Cara, np.ndarray]:
    return _cotar_verticalmente(cubo, fila, False)


def _cotar_horizontalmente(cubo: Cubo, fila: int, horario: bool) -> dict[Cara, np.ndarray]:
    """
    rotar la capa en la fila espesificada horizontalmente.
    * Si horario = True, la rotación será horaria, Si no, será antihoraria
    * returns nuevo estado de cubo con la fila rotada
    """
    # la orden en la cual copiaremnos las caras horariamente
    orden = CARAS_HORIZONTALES
    if horario:
        # ponerla al revés para copiar antihorariamente
        orden = CARAS_HORIZONTALES[::-1]

    estado_nuevo = copy.deepcopy(cubo._estado)
    primera_fila = copy.deepcopy(cubo._estado[orden[0]][fila])

    # copiar filas en la orden dado para hacer una rotación
    for destino, fuente in zip(orden, orden[1:]):
        copia_de_fila = copy.deepcopy(estado_nuevo[fuente][fila])
        estado_nuevo[destino][fila] = copia_de_fila

    estado_nuevo[orden[-1]][fila] = primera_fila

    return estado_nuevo


def _cotar_verticalmente(cubo: Cubo, columna: int, horario: bool) -> dict[Cara, np.ndarray]:
    """
    rotar la capa en la columna espesificada verticalmente.
    * Si horario = True, la rotación será horaria, Si no, será antihoraria
    * returns nuevo estado de cubo con la fila rotada
    """
    # la orden en la cual copiaremnos las caras horariamente
    orden = CARAS_VERTICALES
    if horario:
        # ponerla al revés para copiar antihorariamente
        orden = CARAS_VERTICALES[::-1]

    estado_nuevo = copy.deepcopy(cubo._estado)
    primera_columna = copy.deepcopy(cubo._estado[orden[0]][0:, columna])

    # copiar filas en la orden dado para hacer una rotación
    for destino, fuente in zip(orden, orden[1:]):
        copia_de_columna = copy.deepcopy(estado_nuevo[fuente][0:, columna])
        estado_nuevo[destino][0:, columna] = copia_de_columna

    estado_nuevo[orden[-1]][0:, columna] = primera_columna

    return estado_nuevo
