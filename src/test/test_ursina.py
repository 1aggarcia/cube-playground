# deshabilitar aviso de acceder a métodos privados
# pylint: disable=W0212

import unittest
from ursina import Ursina

from ui.ursina import app
from modelos.cubo import generar_cubo
from modelos.movimiento import movimiento_de_texto

class ProbarUrsina(unittest.TestCase):
    def test_al_teclar(self):
        Ursina(window_type='none')

        cubo_prueba = generar_cubo(3)
        cubo_modelo = generar_cubo(3)

        # movimientos básicos
        app.al_teclar("u", cubo_prueba)
        cubo_modelo.mover(movimiento_de_texto("U"))
        self.assertEqual(cubo_modelo, cubo_prueba)

        app.al_teclar("d", cubo_prueba)
        app.al_teclar("b", cubo_prueba)
        app.al_teclar("d", cubo_prueba)
        app.al_teclar("f", cubo_prueba)
        cubo_modelo.mover(movimiento_de_texto("D"))
        cubo_modelo.mover(movimiento_de_texto("B"))
        cubo_modelo.mover(movimiento_de_texto("D"))
        cubo_modelo.mover(movimiento_de_texto("F"))
        self.assertEqual(cubo_modelo, cubo_prueba)

        # teclas irrelevantes
        app.al_teclar("d up", cubo_prueba)
        self.assertEqual(cubo_modelo, cubo_prueba)

        app.al_teclar("u hold", cubo_prueba)
        app.al_teclar("t", cubo_prueba)
        self.assertEqual(cubo_modelo, cubo_prueba)

        # restatuar
        app.al_teclar("space", cubo_prueba)
        cubo_modelo.restaturar()
        self.assertEqual(cubo_modelo, cubo_prueba)

        # mezclar
        app.al_teclar("s", cubo_prueba)
        self.assertNotEqual(cubo_modelo, cubo_prueba)
