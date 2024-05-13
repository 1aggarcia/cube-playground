# deshabilitar aviso de acceder a métodos privados
# pylint: disable=W0212

import unittest
from ursina import Ursina

from ui.ursina import app
from modelos.cube import generar_cubo
from modelos.cube3d import Cubo3d
from modelos.move import movimiento_de_texto
from modelos.ursina_state import EstadoUrsina

class ProbarUrsina(unittest.TestCase):
    def test_al_teclar(self):
        Ursina(window_type='none')

        estado = EstadoUrsina(Cubo3d(3))
        cubo_modelo = generar_cubo(3)

        def _validar_igualdad():
            self.assertEqual(cubo_modelo, estado.cubo.cubo_2d)

        # movimientos básicos
        app.al_teclar("u", estado)
        cubo_modelo.mover(movimiento_de_texto("U"))
        _validar_igualdad()

        app.al_teclar("d", estado)
        app.al_teclar("b", estado)
        app.al_teclar("d", estado)
        app.al_teclar("f", estado)
        cubo_modelo.mover(movimiento_de_texto("D"))
        cubo_modelo.mover(movimiento_de_texto("B"))
        cubo_modelo.mover(movimiento_de_texto("D"))
        cubo_modelo.mover(movimiento_de_texto("F"))
        _validar_igualdad()

        # teclas irrelevantes
        app.al_teclar("d up", estado)
        _validar_igualdad()

        app.al_teclar("u hold", estado)
        app.al_teclar("t", estado)
        _validar_igualdad()

        # restatuar
        app.al_teclar("space", estado)
        cubo_modelo.restaturar()
        _validar_igualdad()

        # mezclar
        app.al_teclar("s", estado)
        self.assertNotEqual(cubo_modelo, estado.cubo.cubo_2d)
