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
            np.array([[Cara.U, Cara.L],[Cara.B, Cara.D]]))
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

    def test_cortar_horizontalmente(self):
        cubo_a = cubo.crear_cubo_de_texto(
            u = [['B', 'U'], ['U', 'D']],
            d = [['D', 'R'], ['U', 'D']],
            f = [['F', 'R'], ['F', 'B']],
            b = [['R', 'L'], ['L', 'B']],
            l = [['U', 'L'], ['R', 'L']],
            r = [['F', 'F'], ['D', 'B']]
        )
        resultado_a = cubo._cotar_horizontalmente(
            cubo_a, 0, True)
        esperado_a = {
            Cara.F: np.array([[Cara.F, Cara.F], [Cara.F, Cara.B]]),
            Cara.L: np.array([[Cara.F, Cara.R], [Cara.R, Cara.L]]),
            Cara.B: np.array([[Cara.U, Cara.L], [Cara.L, Cara.B]]),
            Cara.R: np.array([[Cara.R, Cara.L], [Cara.D, Cara.B]]),
            Cara.U: cubo_a.get_cara(Cara.U),
            Cara.D: cubo_a.get_cara(Cara.D),
        }

        for cara in Cara:
            self.assertTrue(np.array_equal(resultado_a[cara],
                                           esperado_a[cara]))

        resultado_b = cubo._cotar_horizontalmente(
            cubo_a, 1, False)
        esperado_b = {
            Cara.R: np.array([[Cara.F, Cara.F], [Cara.F, Cara.B]]),
            Cara.F: np.array([[Cara.F, Cara.R], [Cara.R, Cara.L]]),
            Cara.L: np.array([[Cara.U, Cara.L], [Cara.L, Cara.B]]),
            Cara.B: np.array([[Cara.R, Cara.L], [Cara.D, Cara.B]]),
            Cara.U: cubo_a.get_cara(Cara.U),
            Cara.D: cubo_a.get_cara(Cara.D),
        }

        for cara in Cara:
            self.assertTrue(np.array_equal(resultado_b[cara],
                                           esperado_b[cara]))

    def test_cortar_horizontalmente_horario(self):
        cubo_a = cubo.generar_cubo(4)
        resultado_a = cubo._cotar_horizontalmente_horario(cubo_a, 2)
        esperado_a = cubo._cotar_horizontalmente(
            cubo_a, 2, True)

        for cara in Cara:
            self.assertTrue(np.array_equal(resultado_a[cara],
                                           esperado_a[cara]))

    def test_cortar_horizontalmente_antihorario(self):
        cubo_a = cubo.generar_cubo(17)
        resultado_a = cubo._cotar_horizontalmente_antihorario(cubo_a, 10)
        esperado_a = cubo._cotar_horizontalmente(
            cubo_a, 10, False)

        for cara in Cara:
            self.assertTrue(np.array_equal(resultado_a[cara],
                                           esperado_a[cara]))

    def test_cortar_verticalmente(self):
        cubo_a = cubo.crear_cubo_de_texto(
            u = [['B', 'U'], ['U', 'D']],
            d = [['D', 'R'], ['U', 'D']],
            f = [['F', 'R'], ['F', 'B']],
            b = [['R', 'L'], ['L', 'B']],
            l = [['U', 'L'], ['R', 'L']],
            r = [['F', 'F'], ['D', 'B']]
        )
        resultado_a = cubo._cotar_verticalmente(
            cubo_a, 0, False)
        esperado_a = {
            Cara.F: np.array([[Cara.D, Cara.R], [Cara.U, Cara.B]]),
            Cara.U: np.array([[Cara.F, Cara.U], [Cara.F, Cara.D]]),
            Cara.B: np.array([[Cara.R, Cara.U], [Cara.L, Cara.B]]),
            Cara.D: np.array([[Cara.B, Cara.R], [Cara.L, Cara.D]]),
            Cara.R: cubo_a.get_cara(Cara.R),
            Cara.L: cubo_a.get_cara(Cara.L),
        }

        for cara in Cara:
            self.assertTrue(np.array_equal(resultado_a[cara],
                                           esperado_a[cara]))

    # métodos de clase

    def test_str(self):
        cubo_a = cubo.Cubo(
            u = np.array([[Cara.U, Cara.R], [Cara.D, Cara.B]]),
            d = np.array([[Cara.U, Cara.F], [Cara.U, Cara.U]]),
            f = np.array([[Cara.B, Cara.R], [Cara.B, Cara.D]]),
            b = np.array([[Cara.D, Cara.R], [Cara.F, Cara.F]]),
            l = np.array([[Cara.B, Cara.L], [Cara.L, Cara.L]]),
            r = np.array([[Cara.D, Cara.F], [Cara.L, Cara.R]]),
        )

        self.assertEqual(str(cubo_a),
            '\n'.join([
                '[U][R]', '[D][B]\n', # U
                '[U][F]', '[U][U]\n', # D
                '[B][R]', '[B][D]\n', # F
                '[D][R]', '[F][F]\n', # B
                '[B][L]', '[L][L]\n', # L
                '[D][F]', '[L][R]\n\n', # R    
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
            np.array([[Cara.U, Cara.D], [Cara.U, Cara.U]])
        ))

        self.assertTrue(np.array_equal(cubo_a.get_cara(Cara.R),
            np.array([[Cara.R, Cara.R], [Cara.B, Cara.F]])
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
