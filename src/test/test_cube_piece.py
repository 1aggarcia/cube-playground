# deshabilitar aviso de acceder a métodos privados
# pylint: disable=W0212

import unittest

from ursina import Entity, Ursina, color
from constants.enums import Cara
from models import cube_piece as c

ROSADO = '#FFC0CB'
BLANCO = '#FFFFFF'
VERDE = '#00FF00'

class ProbarCubito(unittest.TestCase):
    def test_crear_plano(self):
        Ursina(window_type='none')
        entity = Entity()

        plano_a = c._crear_plano(entity, Cara.L, BLANCO)
        self.assertEqual(plano_a.parent, entity)
        self.assertEqual(plano_a.origin_y, -0.5)
        self.assertEqual(plano_a.color_getter(), color.hex(BLANCO))

        plano_b = c._crear_plano(entity, Cara.L, VERDE)
        self.assertEqual(plano_b.parent, entity)
        self.assertEqual(plano_b.origin_y, -0.5)
        self.assertEqual(plano_b.color_getter(), color.hex(VERDE))

    def test_colorar(self):
        Ursina(window_type='none')
        cubito = c.Cubito(0, 0, 0)

        self.assertNotEqual(
            cubito.planos[Cara.U].color_getter(),
            color.hex(ROSADO)
        )
        # cambiar el color por rosado
        cubito.colorar(Cara.U, ROSADO)
        self.assertEqual(
            cubito.planos[Cara.U].color_getter(),
            color.hex(ROSADO)
        )

        # intentarlo otra vez
        cubito.colorar(Cara.U, VERDE)
        self.assertEqual(
            cubito.planos[Cara.U].color_getter(),
            color.hex(VERDE)
        )
