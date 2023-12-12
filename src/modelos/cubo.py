import copy
import numpy as np

from constantes.enums import Cara
from modelos.validador_de_cubo import validar_caras

from .partes_de_cubo import Etiqueta, etiqueta_de_texto

CARAS_VERTICALES = [Cara.F, Cara.L, Cara.B, Cara.R]

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

    # # Una referencia para poder saber cuáles caras están al lado de otras
    # MAPA_DE_CARAS = {
    #     'U': MapaDeCara(superior='B', inferior='F', izquierda='L', derecha='R'),
    #     'D': MapaDeCara(superior='F', inferior='B', izquierda='L', derecha='R'),
    #     'F': MapaDeCara(superior='U', inferior='D', izquierda='L', derecha='R'),
    #     'B': MapaDeCara(superior='U', inferior='D', izquierda='R', derecha='L'),
    #     'L': MapaDeCara(superior='U', inferior='D', izquierda='B', derecha='F'),
    #     'R': MapaDeCara(superior='U', inferior='D', izquierda='F', derecha='B'),
    # }

    # constructor

    def __init__(self,
                u: list[list[Etiqueta]],
                d: list[list[Etiqueta]],
                f: list[list[Etiqueta]],
                b: list[list[Etiqueta]],
                l: list[list[Etiqueta]],
                r: list[list[Etiqueta]]
            ):
        validar_caras(u, d, f, b, l, r)
        self.dimension = len(u)
        self.estado = {
            'U': u,
            'D': d,
            'F': f,
            'B': b,
            'L': l,
            'R': r
        }

    # métodos sobrescritos

    def __str__(self):
        resultado = ""
        for cara in self.estado.values():
            # vuelta nxn
            for fila in cara:
                for columna in fila:
                    resultado += f'[{columna}]'
                resultado += '\n'
            resultado += '\n'

        return resultado

    # métodos

    def get_cara(self, cara: Cara):
        return self.estado[cara.value]

    def _set_cara(self, cara: Cara, matriz: list[list[Etiqueta]]):
        self.estado[cara.value] = matriz

    def movimiento_u(self):
        cara_girado = _girar_matriz_horario(self.get_cara(Cara.U))
        self._set_cara(Cara.U, cara_girado)
        self.estado = _cotar_verticalmente_horario(self, 0)

    def movimiento_u_prima(self):
        cara_girado = _girar_matriz_antihorario(self.get_cara(Cara.U))
        self._set_cara(Cara.U, cara_girado)
        self.estado = _cotar_verticalmente_antihorario(self, 0)


# métodos públicos

def copiar_cubo(cubo: Cubo):
    """
    Genera una copia del cubo
    """
    return Cubo(
        u = cubo.estado['U'].copy(),
        d = cubo.estado['D'].copy(),
        f = cubo.estado['F'].copy(),
        b = cubo.estado['B'].copy(),
        r = cubo.estado['R'].copy(),
        l = cubo.estado['L'].copy(),
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
        u = _convertir_a_etiquetas(u),
        d = _convertir_a_etiquetas(d),
        f = _convertir_a_etiquetas(f),
        b = _convertir_a_etiquetas(b),
        r = _convertir_a_etiquetas(r),
        l = _convertir_a_etiquetas(l),
    )


def generar_cubo(dimension: int):
    """
    Genera cubo nxnxn resuelto de la dimension dado
    """
    caras = {}

    for c in Cara:
        posicion = 1
        cara = []
        for _ in range(dimension):
            fila = []
            for _ in range(dimension):
                fila.append(Etiqueta(c, posicion))
                posicion += 1
            cara.append(fila)
        caras[c] = cara

    return Cubo(
        u=caras[Cara.U],
        d=caras[Cara.D],
        f=caras[Cara.F],
        b=caras[Cara.B],
        l=caras[Cara.L],
        r=caras[Cara.R],
    )


# métodos privados

def _convertir_a_etiquetas(lista: list[list[str]]):
    """
    Dado una matriz de cadenas de str,
    devolver una matriz de Etiquetas
    * requiere que cada str sea una Etiqueta válida
    """
    resultado: list[list[Etiqueta]] = []

    # popular resultado con la traducción str -> Etiqueta
    for f in lista:
        fila: list[Etiqueta] = []
        for c in f:
            columna = etiqueta_de_texto(c)
            fila.append(columna)
        resultado.append(fila)

    return resultado


# los métodos que giran las matrices

def _girar_matriz_horario(matriz: list[list]):
    numpy_matriz = np.array(matriz)
    return np.fliplr(numpy_matriz.transpose())


def _girar_matriz_antihorario(matriz: list[list]):
    numpy_matriz = np.array(matriz)
    return np.flipud(numpy_matriz.transpose())


def _cotar_verticalmente_horario(cubo: Cubo, fila: int) -> dict[str, list[list]]:
    """
    rotar la capa en la fila espesificada verticalmente, en direción horaria
    * returns nuevo estado de cubo con la fila rotada
    """
    return _cotar_verticalmente(cubo, fila, True)


def _cotar_verticalmente_antihorario(cubo: Cubo, fila: int) -> dict[str, list[list]]:
    """
    rotar la capa en la fila espesificada verticalmente, en direción antihoraria
    * returns nuevo estado de cubo con la fila rotada
    """
    return _cotar_verticalmente(cubo, fila, False)


def _cotar_verticalmente(cubo: Cubo, fila: int, horario: bool) -> dict[str, list[list]]:
    """
    rotar la capa en la fila espesificada verticalmente.
    * Si horario = True, la rotación será horaria, Si no, será antihoraria
    * returns nuevo estado de cubo con la fila rotada
    """
    estado_nuevo = copy.deepcopy(cubo.estado)

    # la orden en la que copiaremos las caras
    orden = CARAS_VERTICALES
    if horario:
        # una copa de la lista al revés
        orden = CARAS_VERTICALES[::-1]
    primera_fila = copy.deepcopy(cubo.estado[orden[0].value][fila])

    # copiar filas en la orden dado para hacer una rotación
    for destino, fuente in zip(orden, orden[1:]):
        fila_fuente = copy.deepcopy(estado_nuevo[fuente.value][fila])
        estado_nuevo[destino.value][fila] = fila_fuente

    estado_nuevo[orden[-1].value][fila] = primera_fila

    return estado_nuevo
