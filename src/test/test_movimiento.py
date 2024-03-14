# deshabilitar aviso de chequear x == x
# pylint: disable=R0124

import unittest

import modelos.movimiento as mv
from constantes.enums import Cara

class ProbarMovimiento(unittest.TestCase):

    def test_eq(self):
        x = mv.Movimiento(Cara.D, 1, 1, False)
        y = mv.Movimiento(Cara.D, 1, 1, False)
        z = mv.Movimiento(Cara.D, 1, 1, False)
        diferente = mv.Movimiento(Cara.U, 2, 4, True)

        # Deben ser reflexivos
        self.assertTrue(x == x)
        self.assertTrue(y == y)

        # Deben ser simétricos
        # Iguales
        self.assertTrue(x == y)
        self.assertTrue(y == x)
        # No iguales
        self.assertFalse(x == diferente)
        self.assertFalse(diferente == x)

        # Deben ser transitivos
        # Igual
        self.assertTrue(x == z)
        # No igual
        self.assertFalse(diferente == z)

    def test_str(self):
        # nivel = 1
        mov_corto = mv.Movimiento(Cara.U, 1, 1, False)
        self.assertEqual(str(mov_corto), "U")

        mov_primo = mv.Movimiento(Cara.D, -1, 1, False)
        self.assertEqual(str(mov_primo), "D'")

        mov_doble = mv.Movimiento(Cara.B, 2, 1, False)
        self.assertEqual(str(mov_doble), "B2")

        # nivel = 1 y ancho
        mov_ancho = mv.Movimiento(Cara.U, 1, 1, True)
        self.assertEqual(str(mov_ancho), "Uw")

        mov_ancho_primo = mv.Movimiento(Cara.D, -1, 1, True)
        self.assertEqual(str(mov_ancho_primo), "Dw'")

        mov_ancho_doble = mv.Movimiento(Cara.B, 2, 1, True)
        self.assertEqual(str(mov_ancho_doble), "Bw2")

        # nivel > 1
        mov_largo = mv.Movimiento(Cara.U, 1, 2, False)
        self.assertEqual(str(mov_largo), "2U")

        mov_largo_primo = mv.Movimiento(Cara.D, -1, 3, False)
        self.assertEqual(str(mov_largo_primo), "3D'")

        mov_largo_doble = mv.Movimiento(Cara.B, 2, 99, False)
        self.assertEqual(str(mov_largo_doble), "99B2")

        # nivel > 1 y ancho
        mov_largo_ancho = mv.Movimiento(Cara.U, 1, 34, True)
        self.assertEqual(str(mov_largo_ancho), "34Uw")

        mov_largo_ancho_primo = mv.Movimiento(Cara.D, -1, 4, True)
        self.assertEqual(str(mov_largo_ancho_primo), "4Dw'")

        mov_largo_ancho_doble = mv.Movimiento(Cara.B, 2, 2, True)
        self.assertEqual(str(mov_largo_ancho_doble), "2Bw2")

    def test_movimiento_de_texto(self):
        # SIN NIVEL
        # len = 1
        self.assertEqual(
            mv.movimiento_de_texto('U'),
            mv.Movimiento(Cara.U, 1, 1, False)
        )

        # len = 2: Uw, U', U2
        self.assertEqual(
            mv.movimiento_de_texto('Dw'),
            mv.Movimiento(Cara.D, 1, 1, True)
        )
        self.assertEqual(
            mv.movimiento_de_texto("L'"),
            mv.Movimiento(Cara.L, -1, 1, False)
        )
        self.assertEqual(
            mv.movimiento_de_texto('R2'),
            mv.Movimiento(Cara.R, 2, 1, False)
        )

        # len = 3: Uw', Uw2
        self.assertEqual(
            mv.movimiento_de_texto("Dw'"),
            mv.Movimiento(Cara.D, -1, 1, True)
        )
        self.assertEqual(
            mv.movimiento_de_texto('Rw2'),
            mv.Movimiento(Cara.R, 2, 1, True)
        )

        # CON NIVEL
        # len = n + 1: 99U
        self.assertEqual(
            mv.movimiento_de_texto('99U'),
            mv.Movimiento(Cara.U, 1, 99, False)
        )

        # len = n + 2: 4Uw, 99U', 99U2
        self.assertEqual(
            mv.movimiento_de_texto('4Dw'),
            mv.Movimiento(Cara.D, 1, 4, True)
        )
        self.assertEqual(
            mv.movimiento_de_texto("22B'"),
            mv.Movimiento(Cara.B, -1, 22, False)
        )
        self.assertEqual(
            mv.movimiento_de_texto('4L2'),
            mv.Movimiento(Cara.L, 2, 4, False)
        )

        # len = n + 3: 99Uw', 99Uw2
        self.assertEqual(
            mv.movimiento_de_texto("5923Fw'"),
            mv.Movimiento(Cara.F, -1, 5923, True)
        )
        self.assertEqual(
            mv.movimiento_de_texto('5Uw2'),
            mv.Movimiento(Cara.U, 2, 5, True)
        )

    def test_invertir_movimiento(self):
        mov_a = mv.Movimiento(Cara.D, 1, 1, True)
        mov_a_invertida = mv.Movimiento(Cara.D, -1, 1, True)

        self.assertEqual(mov_a_invertida, mv.invertir_movimiento(mov_a))
        self.assertEqual(mov_a, mv.invertir_movimiento(mov_a_invertida))

        mov_b = mv.Movimiento(Cara.F, 2, 32, False)

        self.assertEqual(mov_b, mv.invertir_movimiento(mov_b))
