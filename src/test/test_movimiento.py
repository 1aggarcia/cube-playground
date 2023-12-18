import unittest

import modelos.movimiento as mv
from constantes.enums import Cara

class ProbarCubo(unittest.TestCase):

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
        self.assertTrue(y ==x )
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
