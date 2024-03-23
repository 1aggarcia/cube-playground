# deshabilitar aviso de acceder a métodos privados
# pylint: disable=W0212

import unittest

from ursina import Entity, Ursina
from constantes.enums import Cara
from modelos import cubito

class ProbarCubito(unittest.TestCase):
    def test_crear_plano(self):
        # hace falta chequear el color, modelo, textura y rotación
        Ursina(window_type='none')
        entity = Entity()

        plano_a = cubito._crear_plano(entity, Cara.L, Cara.U)
        self.assertEqual(plano_a.parent, entity)
        self.assertEqual(plano_a.origin_y, -0.5)

        plano_b = cubito._crear_plano(entity, Cara.L, Cara.F)
        self.assertEqual(plano_b.parent, entity)
        self.assertEqual(plano_b.origin_y, -0.5)
        self.assertNotEqual(plano_b.color, plano_a.color)
