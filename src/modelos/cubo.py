import numpy as np

from .partes_de_cubo import Etiqueta, MapaDeCara
from constantes.enums import Cara
from modelos.validador_de_cubo import validarCaras

class Cubo:
    '''
    Modelo para un cubo de Rubik con 6 caras.
    Se recomienda crear con Cubo.generar(n) y no el constructor para cubos resueltos,
    a no ser que quieras crear un cubo con un estado espesífico. Las caras son:
    * U (up) - de arriba
    * D (down) - de abajo
    * F (front) - el frente
    * B (back) - el reverso
    * L (left) - la izquerda
    * R (right) - la derecha
    '''

    # Una referencia para poder saber cuáles caras están al lado de otras
    MAPA_DE_CARAS = {
        'U': MapaDeCara(superior='B', inferior='F', izquierda='L', derecha='R'),
        'D': MapaDeCara(superior='F', inferior='B', izquierda='L', derecha='R'),
        'F': MapaDeCara(superior='U', inferior='D', izquierda='L', derecha='R'),
        'B': MapaDeCara(superior='U', inferior='D', izquierda='R', derecha='L'),
        'L': MapaDeCara(superior='U', inferior='D', izquierda='B', derecha='F'),
        'R': MapaDeCara(superior='U', inferior='D', izquierda='F', derecha='B'),
    }

    # constructor

    def __init__(self,
                U: list[list[Etiqueta]], 
                D: list[list[Etiqueta]], 
                F: list[list[Etiqueta]], 
                B: list[list[Etiqueta]], 
                L: list[list[Etiqueta]], 
                R: list[list[Etiqueta]]
            ):
        validarCaras(U, D, F, B, L, R)
        self.dimension = len(U)
        self.estado = {
            'U': U,
            'D': D,
            'F': F,
            'B': B,
            'L': L,
            'R': R
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

    def girarMatrizHorario(self, cara: Cara):
        matriz = np.array(self.estado[cara.value])
        self.estado[cara] = np.fliplr(matriz.transpose())

    def girarMatrizAntihorario(self, cara: Cara):
        matriz = np.array(self.estado[cara.value])
        self.estado[cara.value] = np.flipud(matriz.transpose())

    def copiar(self):
        'Genera una copia del cubo'
        return Cubo(
            U = self.estado['U'].copy(),
            D = self.estado['D'].copy(),
            F = self.estado['F'].copy(),
            B = self.estado['B'].copy(),
            R = self.estado['R'].copy(),
            L = self.estado['L'].copy(),
        )
    
    def _convertirAEtiquetas(lista: list[list[str]]):
        '''
        Dado una matriz de cadenas de str,
        devolver una matriz de Etiquetas
        * requiere que cada str sea una Etiqueta válida
        '''
        resultado: list[list[Etiqueta]] = []

        # popular resultado con la traducción str -> Etiqueta
        for f in lista:
            fila: list[Etiqueta] = []
            for c in f:
                columna = Etiqueta.deTexto(c)
                fila.append(columna)
            resultado.append(fila)

        return resultado

    
    def crearDeTexto(
                U: list[list[str]], 
                D: list[list[str]], 
                F: list[list[str]], 
                B: list[list[str]], 
                L: list[list[str]], 
                R: list[list[str]]
            ):
        '''
        Crear un cubo dado matrices de tipo str
        * requiere que cada str sea una Etiqueta válida
        '''
        return Cubo(
            U = Cubo._convertirAEtiquetas(U),
            D = Cubo._convertirAEtiquetas(D),
            F = Cubo._convertirAEtiquetas(F),
            B = Cubo._convertirAEtiquetas(B),
            R = Cubo._convertirAEtiquetas(R),
            L = Cubo._convertirAEtiquetas(L),            
        )
    
    def generar(dimension: int):
        'Genera cubo nxnxn resuelto de la dimension dado'
        caras = {}

        for c in Cara:
            posicion = 1
            cara = []
            for i in range(dimension):
                fila = []
                for j in range(dimension):
                    fila.append(Etiqueta(c, posicion))
                    posicion += 1
                cara.append(fila)
            caras[c] = cara

        return Cubo(
            U=caras[Cara.U],
            D=caras[Cara.D],
            F=caras[Cara.F],
            B=caras[Cara.B],
            L=caras[Cara.L],
            R=caras[Cara.R],
        )