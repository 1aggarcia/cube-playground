import unittest
import numpy as np

from modelos import cubo
from constantes.enums import Cara

class ProbarCubo(unittest.TestCase):
    # métodos privados

    def test_convertir_a_caras(self):
        lista_a = [['U', 'L'], ['B', 'D']]
        lista_b = [['U', 'L'], ['32', '23'], ['D', 'R']]
        lista_c = [['U', 'L', 'D'], ['D', 'F', 'R'], ['B', 'L', 2]]

        self.assertTrue(
            np.array_equal(cubo._convertir_a_caras(lista_a),
            [[Cara.U, Cara.L],[Cara.B, Cara.D]])
        )
        
        self.assertRaises(ValueError, cubo._convertir_a_caras, lista_b)
        self.assertRaises(KeyError, cubo._convertir_a_caras, lista_c)


    def test_girar_matriz_horario(self):
        lista_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        girada_a = np.array([
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ])
        self.assertTrue(np.array_equal(girada_a, cubo._girar_matriz_horario(lista_a)))

        lista_b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        girada_b = np.array([
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]
        ])
        self.assertTrue(np.array_equal(girada_b, cubo._girar_matriz_horario(lista_b)))


    def test_girar_matriz_antihorario(self):
        lista_a = np.array([[234, 123], [65, 2], [1, 2]])
        girada_a = np.array([
            [123, 2, 2],
            [234, 65, 1]
        ])
        self.assertTrue(np.array_equal(girada_a, cubo._girar_matriz_antihorario(lista_a)))

        lista_b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        girada_b = np.array([
            [4, 8, 12, 16],
            [3, 7, 11, 15],
            [2, 6, 10, 14],
            [1, 5, 9, 13]
        ])
        self.assertTrue(np.array_equal(girada_b, cubo._girar_matriz_antihorario(lista_b)))

    # métodos de clase

    def test_str(self):
        cubo_a = cubo.Cubo(
            u = np.array([[Cara.U, Cara.B], [Cara.D, Cara.R]]),
            d = np.array([[Cara.L, Cara.U], [Cara.R, Cara.D]]),
            f = np.array([[Cara.L, Cara.B], [Cara.U, Cara.F]]),
            b = np.array([[Cara.L, Cara.F], [Cara.B, Cara.D]]),
            l = np.array([[Cara.U, Cara.D], [Cara.L, Cara.R]]),
            r = np.array([[Cara.R, Cara.F], [Cara.F, Cara.B]]),
        )

        self.assertEqual(str(cubo_a),
            '\n'.join([
                '[U][B]', '[D][R]\n', # U
                '[L][U]', '[R][D]\n', # D
                '[L][B]', '[U][F]\n', # F
                '[L][F]', '[B][D]\n', # B
                '[U][D]', '[L][R]\n', # L
                '[R][F]', '[F][B]\n\n', # R    
            ])
        )

    def test_get_cara(self):
        cubo_a = cubo.crear_cubo_de_texto(
            u = [['U', 'D'], ['U', 'U']],
            d = [['R', 'D'], ['D', 'L']],
            f = [['F', 'F'], ['B', 'R']],
            b = [['F', 'B'], ['D', 'B']],
            l = [['L', 'L'], ['L', 'U']],
            r = [['R', 'R'], ['B', 'F']]
        )

        self.assertTrue(np.array_equal(cubo_a.get_cara(Cara.U),
            [[Cara.U, Cara.D], [Cara.U, Cara.U]]
        ))

        self.assertTrue(np.array_equal(cubo_a.get_cara(Cara.R),
            [[Cara.R, Cara.R], [Cara.B, Cara.F]]
        ))

    def test_set_cara(self):
        cubo_a = cubo.generar_cubo(2)

        cara_l = np.array([[Cara.F, Cara.D], [Cara.U, Cara.U]])
        cubo_a._set_cara(Cara.L, cara_l)
        self.assertTrue(np.array_equal(cubo_a.get_cara(Cara.L), cara_l))

        cara_b = np.array([[Cara.U, Cara.U], [Cara.D, Cara.B]])
        cubo_a._set_cara(Cara.L, cara_b)
        self.assertTrue(np.array_equal(cubo_a.get_cara(Cara.L), cara_b))

    # métodos públicos

    def test_copiar_cubo(self):
        pass


    def test_crear_cubo_de_texto(self):
        cubo_a = cubo.crear_cubo_de_texto(
            u = [['U', 'D'], ['U', 'U']],
            d = [['R', 'D'], ['D', 'L']],
            f = [['F', 'F'], ['B', 'R']],
            b = [['F', 'B'], ['D', 'B']],
            l = [['L', 'L'], ['L', 'U']],
            r = [['R', 'R'], ['B', 'F']]
        )

        self.assertEqual(str(cubo_a),
            '\n'.join([
                '[U][D]', '[U][U]\n', # U
                '[R][D]', '[D][L]\n', # D
                '[F][F]', '[B][R]\n', # F
                '[F][B]', '[D][B]\n', # B
                '[L][L]', '[L][U]\n', # L
                '[R][R]', '[B][F]\n\n', # R    
            ])
        )


    def test_generar_cubo(self):
        cubo_a = cubo.generar_cubo(2)
        cubo_b = cubo.generar_cubo(3)

        self.assertEqual(str(cubo_a),
            '\n'.join([
                '[U][U]', '[U][U]\n', # U
                '[D][D]', '[D][D]\n', # D
                '[F][F]', '[F][F]\n', # F
                '[B][B]', '[B][B]\n', # B
                '[L][L]', '[L][L]\n', # L
                '[R][R]', '[R][R]\n\n', # R    
            ])
        )
        self.assertEqual(str(cubo_b),
            '\n'.join([
                '[U][U][U]', '[U][U][U]', '[U][U][U]\n', # U
                '[D][D][D]', '[D][D][D]', '[D][D][D]\n', # D
                '[F][F][F]', '[F][F][F]', '[F][F][F]\n', # F
                '[B][B][B]', '[B][B][B]', '[B][B][B]\n', # B
                '[L][L][L]', '[L][L][L]', '[L][L][L]\n', # L
                '[R][R][R]', '[R][R][R]', '[R][R][R]\n\n', # R
            ])
        )

    def test_generar_matriz_de_cara(self):
        self.assertTrue(np.array_equal(
            cubo.generar_matriz_de_cara(Cara.U, 2),
            np.array([
                [Cara.U, Cara.U],
                [Cara.U, Cara.U],
            ])
        ))

        self.assertTrue(np.array_equal(
            cubo.generar_matriz_de_cara(Cara.R, 5),
            np.array([
                [Cara.R, Cara.R, Cara.R, Cara.R, Cara.R],
                [Cara.R, Cara.R, Cara.R, Cara.R, Cara.R],
                [Cara.R, Cara.R, Cara.R, Cara.R, Cara.R],
                [Cara.R, Cara.R, Cara.R, Cara.R, Cara.R],
                [Cara.R, Cara.R, Cara.R, Cara.R, Cara.R],
            ])
        ))

if __name__ == '__main__':
    unittest.main()
