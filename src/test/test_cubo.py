import numpy as np
import unittest

from modelos import cubo
from modelos.partes_de_cubo import Etiqueta as et
from constantes import cubos
from constantes.enums import Cara

class ProbarCubo(unittest.TestCase):
    # métodos privados

    def test_convertirAEtiquetas(self):
        listaA = [['U1', 'L2', 'D21'], ['B14'], ['D12', 'R2']]
        listaB = [['U1', 'L2', 'D21'], ['32'], ['D12', 'R2']]
        listaC = [['U1', 'L2', 'D21'], 2]

        self.assertEqual(cubo._convertirAEtiquetas(listaA),
            [
                [et.deTexto('U1'), et.deTexto('L2'), et.deTexto('D21')],
                [et.deTexto('B14')],
                [et.deTexto('D12'), et.deTexto('R2')]
            ])
        
        self.assertRaises(KeyError, cubo._convertirAEtiquetas, listaB)
        self.assertRaises(TypeError, cubo._convertirAEtiquetas, listaC)


    def test_girarMatrizHorario(self):
        listaA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        giradaA = np.array([
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ])
        self.assertTrue((giradaA & cubo._girarMatrizHorario(listaA)).all())

        listaB = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        giradaB = np.array([
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]
        ])
        self.assertTrue((giradaB & cubo._girarMatrizHorario(listaB)).all())


    def test_girarMatrizAnihorario(self):
        listaA = [[234, 123], [65, 2], [1, 2]]
        giradaA = np.array([
            [123, 2, 2],
            [234, 65, 1]
        ])
        self.assertTrue((giradaA & cubo._girarMatrizAntihorario(listaA)).all())

        listaB = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        giradaB = np.array([
            [4, 8, 12, 16],
            [3, 7, 11, 15],
            [2, 6, 10, 14],
            [1, 5, 9, 13]
        ])
        self.assertTrue((giradaB & cubo._girarMatrizAntihorario(listaB)).all())

    # métodos de clase

    def test_str(self):
        cuboA = cubo.Cubo(
            U=[
                [et.deTexto('U1'), et.deTexto('U2')],
                [et.deTexto('U3'), et.deTexto('U4')],
            ],
            D=[
                [et.deTexto('D1'), et.deTexto('D2')],
                [et.deTexto('D3'), et.deTexto('D4')],
            ],
            L=[
                [et.deTexto('L1'), et.deTexto('L2')],
                [et.deTexto('L3'), et.deTexto('L4')],
            ],
            R=[
                [et.deTexto('R1'), et.deTexto('R2')],
                [et.deTexto('R3'), et.deTexto('R4')],
            ],
            F=[
                [et.deTexto('F1'), et.deTexto('F2')],
                [et.deTexto('F3'), et.deTexto('F4')],
            ],
            B=[
                [et.deTexto('B1'), et.deTexto('B2')],
                [et.deTexto('B3'), et.deTexto('B4')],
            ],
        )

        self.assertEqual(str(cuboA), 
            '\n'.join([
                '[U1][U2]', '[U3][U4]\n', # U
                '[D1][D2]', '[D3][D4]\n', # D
                '[F1][F2]', '[F3][F4]\n', # F
                '[B1][B2]', '[B3][B4]\n', # B
                '[L1][L2]', '[L3][L4]\n', # L
                '[R1][R2]', '[R3][R4]\n\n', # R    
            ])
        )

    def test_getCara(self):
        cuboA = cubo.crearCuboDeTexto(
            U=
                [['U1', 'D2'],
                ['U3', 'U3']],
            D=
                [['R1', 'D2'],
                ['D3', 'L4']],
            F=
                [['F1', 'F2'],
                ['B3', 'R4']],
            B=
                [['F1', 'B2'],
                ['D3', 'B4']],
            L=
                [['L1', 'L2'],
                ['L3', 'U4']],
            R=
                [['R1', 'R2'],
                ['B3', 'F4']]
        )

        self.assertEqual(cuboA.getCara(Cara.U), 
            [[et.deTexto('U1'), et.deTexto('D2')], [et.deTexto('U3'), et.deTexto('U3')]]
        )

        self.assertEqual(cuboA.getCara(Cara.R), 
            [[et.deTexto('R1'), et.deTexto('R2')], [et.deTexto('B3'), et.deTexto('F4')]]
        )

    def test_setCara(self):
        cuboA = cubo.generarCubo(2)

        caraL = [[et.deTexto('F2111'), et.deTexto('F999')]]
        cuboA._setCara(Cara.L, caraL)
        self.assertEqual(cuboA.getCara(Cara.L), caraL)

        caraB = [[et.deTexto('B2111'), et.deTexto('B999')]]
        cuboA._setCara(Cara.L, caraB)
        self.assertEqual(cuboA.getCara(Cara.L), caraB)

    # métodos públicos

    def test_copiarCubo(self):
        pass


    def test_crearCuboDeTexto(self):
        cuboA = cubo.crearCuboDeTexto(
            U=
                [['U1', 'D2'],
                ['U3', 'U3']],
            D=
                [['R1', 'D2'],
                ['D3', 'L4']],
            F=
                [['F1', 'F2'],
                ['B3', 'R4']],
            B=
                [['F1', 'B2'],
                ['D3', 'B4']],
            L=
                [['L1', 'L2'],
                ['L3', 'U4']],
            R=
                [['R1', 'R2'],
                ['B3', 'F4']]
        )

        self.assertEqual(str(cuboA), 
            '\n'.join([
                '[U1][D2]', '[U3][U3]\n', # U
                '[R1][D2]', '[D3][L4]\n', # D
                '[F1][F2]', '[B3][R4]\n', # F
                '[F1][B2]', '[D3][B4]\n', # B
                '[L1][L2]', '[L3][U4]\n', # L
                '[R1][R2]', '[B3][F4]\n\n', # R   
            ])
        )


    def test_generarCubo(self):
        cuboA = cubo.generarCubo(2)
        cuboB = cubo.generarCubo(3)

        self.assertEqual(str(cuboA), 
            '\n'.join([
                '[U1][U2]', '[U3][U4]\n', # U
                '[D1][D2]', '[D3][D4]\n', # D
                '[F1][F2]', '[F3][F4]\n', # F
                '[B1][B2]', '[B3][B4]\n', # B
                '[L1][L2]', '[L3][L4]\n', # L
                '[R1][R2]', '[R3][R4]\n\n', # R    
            ])
        )
        self.assertEqual(str(cuboB), 
            '\n'.join([
                '[U1][U2][U3]', '[U4][U5][U6]', '[U7][U8][U9]\n', # U
                '[D1][D2][D3]', '[D4][D5][D6]', '[D7][D8][D9]\n', # D
                '[F1][F2][F3]', '[F4][F5][F6]', '[F7][F8][F9]\n', # F
                '[B1][B2][B3]', '[B4][B5][B6]', '[B7][B8][B9]\n', # B
                '[L1][L2][L3]', '[L4][L5][L6]', '[L7][L8][L9]\n', # L
                '[R1][R2][R3]', '[R4][R5][R6]', '[R7][R8][R9]\n\n', # R
            ])
        )

if __name__ == '__main__':
    unittest.main()