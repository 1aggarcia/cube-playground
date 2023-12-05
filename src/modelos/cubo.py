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
                U: list[list[str]], 
                D: list[list[str]], 
                F: list[list[str]], 
                B: list[list[str]], 
                L: list[list[str]], 
                R: list[list[str]]
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
            for i in range(self.dimension):
                resultado += str(cara[i]) + '\n'
            resultado += '\n'

        return resultado

    # métodos

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
    
    def generar(dimension: int):
        'Genera cubo nxnxn resuelto de la dimension dado'
        caras = {'U':[], 'D':[], 'F':[], 'B':[], 'L':[], 'R':[],}

        for key in caras:
            x = 1
            cara = []
            for i in range(dimension):
                fila = []
                for j in range(dimension):
                    fila.append(f'{key}{x}')
                    x += 1
                cara.append(fila)
            caras[key] = cara

        return Cubo(
            U=caras['U'],
            D=caras['D'],
            F=caras['F'],
            B=caras['B'],
            L=caras['L'],
            R=caras['R'],
        )