# deshabilitar aviso de acceder a métodos privados
# pylint: disable=W0212

import unittest
import numpy as np

from modelos import cubo
from constantes.enums import Cara

class ProbarCubo(unittest.TestCase):
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
