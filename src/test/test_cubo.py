import unittest
import numpy as np

from modelos import cubo
from modelos.partes_de_cubo import etiqueta_de_texto
from constantes.enums import Cara

class ProbarCubo(unittest.TestCase):
    # métodos privados

    def test_convertir_a_etiquetas(self):
        lista_a = [['U1', 'L2', 'D21'], ['B14'], ['D12', 'R2']]
        lista_b = [['U1', 'L2', 'D21'], ['32'], ['D12', 'R2']]
        lista_c = [['U1', 'L2', 'D21'], 2]

        self.assertEqual(cubo._convertir_a_etiquetas(lista_a),
            [
                [etiqueta_de_texto('U1'), etiqueta_de_texto('L2'), etiqueta_de_texto('D21')],
                [etiqueta_de_texto('B14')],
                [etiqueta_de_texto('D12'), etiqueta_de_texto('R2')]
            ])
        
        self.assertRaises(KeyError, cubo._convertir_a_etiquetas, lista_b)
        self.assertRaises(TypeError, cubo._convertir_a_etiquetas, lista_c)


    def test_girar_matriz_horario(self):
        lista_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        girada_a = np.array([
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ])
        self.assertTrue((girada_a & cubo._girar_matriz_horario(lista_a)).all())

        lista_b = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        girada_b = np.array([
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]
        ])
        self.assertTrue((girada_b & cubo._girar_matriz_horario(lista_b)).all())


    def test_girar_matriz_antihorario(self):
        lista_a = [[234, 123], [65, 2], [1, 2]]
        girada_a = np.array([
            [123, 2, 2],
            [234, 65, 1]
        ])
        self.assertTrue((girada_a & cubo._girar_matriz_antihorario(lista_a)).all())

        lista_b = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        girada_b = np.array([
            [4, 8, 12, 16],
            [3, 7, 11, 15],
            [2, 6, 10, 14],
            [1, 5, 9, 13]
        ])
        self.assertTrue((girada_b & cubo._girar_matriz_antihorario(lista_b)).all())

    # métodos de clase

    def test_str(self):
        cubo_a = cubo.Cubo(
            u=[
                [etiqueta_de_texto('U1'), etiqueta_de_texto('U2')],
                [etiqueta_de_texto('U3'), etiqueta_de_texto('U4')],
            ],
            d=[
                [etiqueta_de_texto('D1'), etiqueta_de_texto('D2')],
                [etiqueta_de_texto('D3'), etiqueta_de_texto('D4')],
            ],
            l=[
                [etiqueta_de_texto('L1'), etiqueta_de_texto('L2')],
                [etiqueta_de_texto('L3'), etiqueta_de_texto('L4')],
            ],
            r=[
                [etiqueta_de_texto('R1'), etiqueta_de_texto('R2')],
                [etiqueta_de_texto('R3'), etiqueta_de_texto('R4')],
            ],
            f=[
                [etiqueta_de_texto('F1'), etiqueta_de_texto('F2')],
                [etiqueta_de_texto('F3'), etiqueta_de_texto('F4')],
            ],
            b=[
                [etiqueta_de_texto('B1'), etiqueta_de_texto('B2')],
                [etiqueta_de_texto('B3'), etiqueta_de_texto('B4')],
            ],
        )

        self.assertEqual(str(cubo_a),
            '\n'.join([
                '[U1][U2]', '[U3][U4]\n', # U
                '[D1][D2]', '[D3][D4]\n', # D
                '[F1][F2]', '[F3][F4]\n', # F
                '[B1][B2]', '[B3][B4]\n', # B
                '[L1][L2]', '[L3][L4]\n', # L
                '[R1][R2]', '[R3][R4]\n\n', # R    
            ])
        )

    def test_get_cara(self):
        cubo_a = cubo.crear_cubo_de_texto(
            u=
                [['U1', 'D2'],
                ['U3', 'U3']],
            d=
                [['R1', 'D2'],
                ['D3', 'L4']],
            f=
                [['F1', 'F2'],
                ['B3', 'R4']],
            b=
                [['F1', 'B2'],
                ['D3', 'B4']],
            l=
                [['L1', 'L2'],
                ['L3', 'U4']],
            r=
                [['R1', 'R2'],
                ['B3', 'F4']]
        )

        self.assertEqual(cubo_a.get_cara(Cara.U),
            [[etiqueta_de_texto('U1'), etiqueta_de_texto('D2')],
             [etiqueta_de_texto('U3'), etiqueta_de_texto('U3')]]
        )

        self.assertEqual(cubo_a.get_cara(Cara.R),
            [[etiqueta_de_texto('R1'), etiqueta_de_texto('R2')],
             [etiqueta_de_texto('B3'), etiqueta_de_texto('F4')]]
        )

    def test_set_cara(self):
        cubo_a = cubo.generar_cubo(2)

        cara_l = [[etiqueta_de_texto('F2111'), etiqueta_de_texto('F999')]]
        cubo_a._set_cara(Cara.L, cara_l)
        self.assertEqual(cubo_a.get_cara(Cara.L), cara_l)

        cara_b = [[etiqueta_de_texto('B2111'), etiqueta_de_texto('B999')]]
        cubo_a._set_cara(Cara.L, cara_b)
        self.assertEqual(cubo_a.get_cara(Cara.L), cara_b)

    # métodos públicos

    def test_copiar_cubo(self):
        pass


    def test_crear_cubo_de_texto(self):
        cubo_a = cubo.crear_cubo_de_texto(
            u=
                [['U1', 'D2'],
                ['U3', 'U3']],
            d=
                [['R1', 'D2'],
                ['D3', 'L4']],
            f=
                [['F1', 'F2'],
                ['B3', 'R4']],
            b=
                [['F1', 'B2'],
                ['D3', 'B4']],
            l=
                [['L1', 'L2'],
                ['L3', 'U4']],
            r=
                [['R1', 'R2'],
                ['B3', 'F4']]
        )

        self.assertEqual(str(cubo_a),
            '\n'.join([
                '[U1][D2]', '[U3][U3]\n', # U
                '[R1][D2]', '[D3][L4]\n', # D
                '[F1][F2]', '[B3][R4]\n', # F
                '[F1][B2]', '[D3][B4]\n', # B
                '[L1][L2]', '[L3][U4]\n', # L
                '[R1][R2]', '[B3][F4]\n\n', # R   
            ])
        )


    def test_generar_cubo(self):
        cubo_a = cubo.generar_cubo(2)
        cubo_b = cubo.generar_cubo(3)

        self.assertEqual(str(cubo_a),
            '\n'.join([
                '[U1][U2]', '[U3][U4]\n', # U
                '[D1][D2]', '[D3][D4]\n', # D
                '[F1][F2]', '[F3][F4]\n', # F
                '[B1][B2]', '[B3][B4]\n', # B
                '[L1][L2]', '[L3][L4]\n', # L
                '[R1][R2]', '[R3][R4]\n\n', # R    
            ])
        )
        self.assertEqual(str(cubo_b),
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
