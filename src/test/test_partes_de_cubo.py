import unittest
from constantes.enums import Cara
from modelos.partes_de_cubo import Etiqueta, MapaDeCara

class ProbarPartesDeCubo(unittest.TestCase):

    def test_Etiqueta_eq(self):
        x = Etiqueta(Cara.D, 3)
        y = Etiqueta(Cara.D, 3)
        z = Etiqueta(Cara.D, 3)
        diferente = Etiqueta(Cara.F, 1)
        
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
        
    def test_Etiqueta_str(self):
        prueba1 = Etiqueta(Cara.F, 23)
        self.assertEqual('F23', str(prueba1))

        prueba2 = Etiqueta(Cara.R, 49129345)
        self.assertEqual('R49129345', str(prueba2))

    def test_Etiqueta_deTexto(self):
        prueba1 = Etiqueta.deTexto('U2')
        self.assertEqual(Etiqueta(Cara.U, 2), prueba1)

        prueba2 = Etiqueta.deTexto('D543')
        self.assertEqual(Etiqueta(Cara.D, 543), prueba2)

if __name__ == '__main__':
    unittest.main()