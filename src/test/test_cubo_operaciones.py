# pylint: disable=W0212

import unittest
import numpy as np

from modelos.cubo import crear_cubo_de_texto
from constantes.enums import Cara
import modelos.cubo_operaciones as op


class ProbarOperaciones(unittest.TestCase):
    def test_generar_scramble(self):
        # 2x2
        scramble = op.generar_scramble(2)

        print("2x2: Verificando la longitud del scramble")
        self.assertEqual(op._longitud_de_scramble(2), len(scramble))

        print("2x2: Verificando que cada par de caras es diferente")
        for mov_a, mov_b in zip(scramble, scramble[1:]):
            self.assertNotEqual(mov_a.cara, mov_b.cara)

        # 4x4
        scramble = op.generar_scramble(4)

        print("4x4: Verificando la longitud del scramble")
        self.assertEqual(op._longitud_de_scramble(4), len(scramble))

        print("4x4: Verificando que cada par de caras es diferente")
        for mov_a, mov_b in zip(scramble, scramble[1:]):
            self.assertNotEqual(mov_a.cara, mov_b.cara)

        print("Abrobado: generar_scramble")

    def test_girar_matriz(self):
        # 90 degrados (sentido horario)
        lista_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        girada_a = np.array([
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ])
        self.assertTrue(np.array_equal(girada_a, op.girar_matriz(lista_a, 1)))

        lista_b = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ])
        girada_b = np.array([
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]
        ])
        self.assertTrue(np.array_equal(girada_b, op.girar_matriz(lista_b, 1)))

        # 270 degrados (sentido antihorario)
        lista_c = np.array(
            [[234, 123],
             [65, 2],
             [1, 2]]
        )
        girada_c = np.array([
            [123, 2, 2],
            [234, 65, 1]
        ])
        self.assertTrue(np.array_equal(girada_c, op.girar_matriz(lista_c, 3)))

        lista_d = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ])
        girada_d = np.array([
            [4, 8, 12, 16],
            [3, 7, 11, 15],
            [2, 6, 10, 14],
            [1, 5, 9, 13]
        ])
        self.assertTrue(np.array_equal(girada_d, op.girar_matriz(lista_d, 3)))

    def test_cortar_horizontalmente(self):
        cubo_a = crear_cubo_de_texto(
            u = [['B', 'U'], ['U', 'D']],
            d = [['D', 'R'], ['U', 'D']],
            f = [['F', 'R'], ['F', 'B']],
            b = [['R', 'L'], ['L', 'B']],
            l = [['U', 'L'], ['R', 'L']],
            r = [['F', 'F'], ['D', 'B']]
        )
        resultado_a = op.cotar_horizontalmente(cubo_a.get_estado(), 0, 1)
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

        resultado_b = op.cotar_horizontalmente(cubo_a.get_estado(), 1, -1)
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

        resultado_c = op.cotar_horizontalmente(cubo_a.get_estado(), 0, 2)
        esperado_c = {
            Cara.F: np.array([[Cara.R, Cara.L], [Cara.F, Cara.B]]),
            Cara.B: np.array([[Cara.F, Cara.R], [Cara.L, Cara.B]]),
            Cara.L: np.array([[Cara.F, Cara.F], [Cara.R, Cara.L]]),
            Cara.R: np.array([[Cara.U, Cara.L], [Cara.D, Cara.B]]),
            Cara.U: cubo_a.get_cara(Cara.U),
            Cara.D: cubo_a.get_cara(Cara.D),
        }

        for cara in Cara:
            self.assertTrue(np.array_equal(resultado_c[cara],
                                           esperado_c[cara]))

    def test_cortar_verticalmente(self):
        cubo_a = crear_cubo_de_texto(
            u = [['B', 'U'], ['U', 'D']],
            d = [['D', 'R'], ['U', 'D']],
            f = [['F', 'R'], ['F', 'B']],
            b = [['R', 'L'], ['L', 'B']],
            l = [['U', 'L'], ['R', 'L']],
            r = [['F', 'F'], ['D', 'B']]
        )
        resultado_a = op.cotar_verticalmente(cubo_a.get_estado(), 0, -1)
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

        resultado_b = op.cotar_verticalmente(cubo_a.get_estado(), 1, 1)
        esperado_b = {
            Cara.U: np.array([[Cara.B, Cara.L], [Cara.U, Cara.R]]),
            Cara.B: np.array([[Cara.D, Cara.L], [Cara.R, Cara.B]]),
            Cara.D: np.array([[Cara.D, Cara.R], [Cara.U, Cara.B]]),
            Cara.F: np.array([[Cara.F, Cara.U], [Cara.F, Cara.D]]),
            Cara.R: cubo_a.get_cara(Cara.R),
            Cara.L: cubo_a.get_cara(Cara.L),
        }

        for cara in Cara:
            self.assertTrue(np.array_equal(resultado_b[cara],
                                           esperado_b[cara]))

        resultado_c = op.cotar_verticalmente(cubo_a.get_estado(), 0, 2)
        esperado_c = {
            Cara.U: np.array([[Cara.D, Cara.U], [Cara.U, Cara.D]]),
            Cara.D: np.array([[Cara.B, Cara.R], [Cara.U, Cara.D]]),
            Cara.F: np.array([[Cara.B, Cara.R], [Cara.L, Cara.B]]),
            Cara.B: np.array([[Cara.R, Cara.F], [Cara.L, Cara.F]]),
            Cara.R: cubo_a.get_cara(Cara.R),
            Cara.L: cubo_a.get_cara(Cara.L),
        }

        for cara in Cara:
            self.assertTrue(np.array_equal(resultado_c[cara],
                                           esperado_c[cara]))

    def test_cortar_frontera(self):
        cubo_a = crear_cubo_de_texto(
            u = [['D', 'L'], ['U', 'U']],
            d = [['D', 'R'], ['U', 'D']],
            f = [['F', 'R'], ['L', 'D']],
            b = [['B', 'B'], ['F', 'R']],
            l = [['R', 'L'], ['F', 'B']],
            r = [['B', 'U'], ['F', 'L']]
        )
        resultado_a = op.cortar_frontera(cubo_a.get_estado(), 0, 1)
        esperado_a = {
            Cara.L: np.array([[Cara.R, Cara.D], [Cara.F, Cara.R]]),
            Cara.U: np.array([[Cara.D, Cara.L], [Cara.B, Cara.L]]),
            Cara.R: np.array([[Cara.U, Cara.U], [Cara.U, Cara.L]]),
            Cara.D: np.array([[Cara.F, Cara.B], [Cara.U, Cara.D]]),
            Cara.F: cubo_a.get_cara(Cara.F),
            Cara.B: cubo_a.get_cara(Cara.B),
        }

        for cara in Cara:
            self.assertTrue(np.array_equal(resultado_a[cara],
                                           esperado_a[cara]))

        resultado_b = op.cortar_frontera(cubo_a.get_estado(), 1, -1)
        esperado_b = {
            Cara.D: np.array([[Cara.D, Cara.R], [Cara.R, Cara.F]]),
            Cara.L: np.array([[Cara.L, Cara.L], [Cara.D, Cara.B]]),
            Cara.U: np.array([[Cara.U, Cara.L], [Cara.U, Cara.U]]),
            Cara.R: np.array([[Cara.B, Cara.D], [Cara.F, Cara.U]]),
            Cara.F: cubo_a.get_cara(Cara.F),
            Cara.B: cubo_a.get_cara(Cara.B),
        }

        for cara in Cara:
            self.assertTrue(np.array_equal(resultado_b[cara],
                                           esperado_b[cara]))

        resultado_c = op.cortar_frontera(cubo_a.get_estado(), 0, 2)
        esperado_c = {
            Cara.U: np.array([[Cara.D, Cara.L], [Cara.R, Cara.D]]),
            Cara.D: np.array([[Cara.U, Cara.U], [Cara.U, Cara.D]]),
            Cara.L: np.array([[Cara.R, Cara.F], [Cara.F, Cara.B]]),
            Cara.R: np.array([[Cara.B, Cara.U], [Cara.L, Cara.L]]),
            Cara.F: cubo_a.get_cara(Cara.F),
            Cara.B: cubo_a.get_cara(Cara.B),
        }

        for cara in Cara:
            self.assertTrue(np.array_equal(resultado_c[cara],
                                           esperado_c[cara]))

    def test_longitud_de_scramble(self):
        for i, v in enumerate(op.LONGITUD_DE_SCRAMBLES[2:], start=2):
            self.assertEqual(v, op._longitud_de_scramble(i))

        self.assertEqual(130, op._longitud_de_scramble(11))
        self.assertEqual(510, op._longitud_de_scramble(49))


if __name__ == '__main__':
    unittest.main()
