# import unittest
# import numpy as np

# from constantes.enums import Cara
# from modelos import cubo
# from modelos.partes_de_cubo import Etiqueta, etiqueta_de_texto, Pegatina, crear_matriz_de_pegatinas

# class ProbarPartesDeCubo(unittest.TestCase):

#     def test_etiqueta_eq(self):
#         x = Etiqueta(Cara.D, 3)
#         y = Etiqueta(Cara.D, 3)
#         z = Etiqueta(Cara.D, 3)
#         diferente = Etiqueta(Cara.F, 1)

#         # Deben ser reflexivos
#         self.assertTrue(x == x)
#         self.assertTrue(y == y)

#         # Deben ser simétricos
#         # Iguales
#         self.assertTrue(x == y)
#         self.assertTrue(y ==x )
#         # No iguales
#         self.assertFalse(x == diferente)
#         self.assertFalse(diferente == x)

#         # Deben ser transitivos
#         # Igual
#         self.assertTrue(x == z)
#         # No igual
#         self.assertFalse(diferente == z)

#     def test_etiqueta_str(self):
#         prueba1 = Etiqueta(Cara.F, 23)
#         self.assertEqual('F23', str(prueba1))

#         prueba2 = Etiqueta(Cara.R, 49129345)
#         self.assertEqual('R49129345', str(prueba2))

#     def test_etiqueta_de_texto(self):
#         prueba1 = etiqueta_de_texto('U2')
#         self.assertEqual(Etiqueta(Cara.U, 2), prueba1)

#         prueba2 = etiqueta_de_texto('D543')
#         self.assertEqual(Etiqueta(Cara.D, 543), prueba2)

#     def test_pegatina_str(self):
#         self.assertEqual(
#             str(Pegatina(Cara.B, 3, 5)),
#             '[cara: Cara.B, profundidad: 3, posicion: 5]'
#         )

#         self.assertEqual(
#             str(Pegatina(Cara.D, 0, 24)),
#             '[cara: Cara.D, profundidad: 0, posicion: 24]'
#         )

#     def test_pegatina_eq(self):
#         x = Pegatina(Cara.D, 3, 14)
#         y = Pegatina(Cara.D, 3, 14)
#         z = Pegatina(Cara.D, 3, 14)
#         diferente = Pegatina(Cara.F, 11, 34)

#         # Deben ser reflexivos
#         self.assertTrue(x == x)
#         self.assertTrue(y == y)

#         # Deben ser simétricos
#         # Iguales
#         self.assertTrue(x == y)
#         self.assertTrue(y == x)
#         # No iguales
#         self.assertFalse(x == diferente)
#         self.assertFalse(diferente == x)

#         # Deben ser transitivos
#         # Igual
#         self.assertTrue(x == z)
#         # No igual
#         self.assertFalse(diferente == z)

#     def test_crear_matriz_de_pegatinas(self):
#         # matrices pares, es decir sin centro
#         matriz_par_a = cubo.generar_matriz_de_cara(Cara.F, 2)
#         self.assertTrue(np.array_equal(
#             crear_matriz_de_pegatinas(matriz_par_a),
#             np.array([
#                 [Pegatina(Cara.F, 0, 0), Pegatina(Cara.F, 0, 0)],
#                 [Pegatina(Cara.F, 0, 0), Pegatina(Cara.F, 0, 0)],
#             ])
#         ))

#         matriz_par_b = cubo.generar_matriz_de_cara(Cara.D, 4)
#         self.assertTrue(np.array_equal(
#             crear_matriz_de_pegatinas(matriz_par_b),
#             np.array([
#                 [Pegatina(Cara.D, 0, 0), Pegatina(Cara.D, 0, 1),
#                     Pegatina(Cara.D, 0, 2), Pegatina(Cara.D, 0, 0)],
#                 [Pegatina(Cara.D, 0, 2), Pegatina(Cara.D, 1, 0),
#                     Pegatina(Cara.D, 1, 0), Pegatina(Cara.D, 0, 1)],
#                 [Pegatina(Cara.D, 0, 1), Pegatina(Cara.D, 1, 0),
#                     Pegatina(Cara.D, 1, 0), Pegatina(Cara.D, 0, 2)],
#                 [Pegatina(Cara.D, 0, 0), Pegatina(Cara.D, 0, 2),
#                     Pegatina(Cara.D, 0, 1), Pegatina(Cara.D, 0, 0)],
#             ])
#         ))

#     # matrices impares, es decir con centro
#         matriz_impar_a = cubo.generar_matriz_de_cara(Cara.L, 3)
#         self.assertTrue(np.array_equal(
#             crear_matriz_de_pegatinas(matriz_impar_a),
#             np.array([
#                 [Pegatina(Cara.L, 0, 0), Pegatina(Cara.L, 0, 1),
#                     Pegatina(Cara.L, 0, 0)],
#                 [Pegatina(Cara.L, 0, 1), Pegatina(Cara.L, 1, 0),
#                     Pegatina(Cara.L, 0, 1)],
#                 [Pegatina(Cara.L, 0, 0), Pegatina(Cara.L, 0, 1),
#                     Pegatina(Cara.L, 0, 0)],
#             ])
#         ))

#         matriz_impar_b = cubo.generar_matriz_de_cara(Cara.D, 7)
#         self.assertTrue(np.array_equal(
#             crear_matriz_de_pegatinas(matriz_impar_b),
#             np.array([
#                 [Pegatina(Cara.D, 0, 0), Pegatina(Cara.D, 0, 1),
#                     Pegatina(Cara.D, 0, 2), Pegatina(Cara.D, 0, 3),
#                         Pegatina(Cara.D, 0, 4), Pegatina(Cara.D, 0, 5),
#                             Pegatina(Cara.D, 0, 0)],
#                 [Pegatina(Cara.D, 0, 5), Pegatina(Cara.D, 1, 0),
#                     Pegatina(Cara.D, 1, 1), Pegatina(Cara.D, 1, 2),
#                         Pegatina(Cara.D, 1, 3), Pegatina(Cara.D, 1, 0),
#                             Pegatina(Cara.D, 0, 1)],
#                 [Pegatina(Cara.D, 0, 4), Pegatina(Cara.D, 1, 3),
#                     Pegatina(Cara.D, 2, 0), Pegatina(Cara.D, 2, 1),
#                         Pegatina(Cara.D, 2, 0), Pegatina(Cara.D, 1, 1),
#                             Pegatina(Cara.D, 0, 2)],
#                 [Pegatina(Cara.D, 0, 3), Pegatina(Cara.D, 1, 2),
#                     Pegatina(Cara.D, 2, 1), Pegatina(Cara.D, 3, 0),
#                         Pegatina(Cara.D, 2, 1), Pegatina(Cara.D, 1, 2),
#                             Pegatina(Cara.D, 0, 3)],
#                 [Pegatina(Cara.D, 0, 2), Pegatina(Cara.D, 1, 1),
#                     Pegatina(Cara.D, 2, 0), Pegatina(Cara.D, 2, 1),
#                         Pegatina(Cara.D, 2, 0), Pegatina(Cara.D, 1, 3),
#                             Pegatina(Cara.D, 0, 4)],
#                 [Pegatina(Cara.D, 0, 1), Pegatina(Cara.D, 1, 0),
#                     Pegatina(Cara.D, 1, 3), Pegatina(Cara.D, 1, 2),
#                         Pegatina(Cara.D, 1, 1), Pegatina(Cara.D, 1, 0),
#                             Pegatina(Cara.D, 0, 5)],
#                 [Pegatina(Cara.D, 0, 0), Pegatina(Cara.D, 0, 5),
#                     Pegatina(Cara.D, 0, 4), Pegatina(Cara.D, 0, 3),
#                         Pegatina(Cara.D, 0, 2), Pegatina(Cara.D, 0, 1),
#                             Pegatina(Cara.D, 0, 0)],
#             ])
#         ))


# if __name__ == '__main__':
#     unittest.main()
