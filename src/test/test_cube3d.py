# deshabilitar aviso de acceder a métodos privados
# pylint: disable=W0212

import unittest
from models import cube3d

class ProbarCubo3d(unittest.TestCase):
    def test_generar_cubitos(self):
        dim = 3
        desviacion = -1

        cubitos = cube3d._generar_cubitos(dim)
        self.assertEqual(len(cubitos), dim)

        for x, cuadrado in enumerate(cubitos):
            # verificar que cubitos es NxN
            self.assertEqual(len(cuadrado), dim)
            for y, fila in enumerate(cuadrado):
                # verificar que cubitos es NxNxN
                self.assertEqual(len(fila), dim)
                for z, cubito in enumerate(fila):
                    es_borde = (
                        x in (0, dim - 1)
                        or y in (0, dim - 1)
                        or z in (0, dim - 1)
                    )
                    if not es_borde:
                        self.assertIsNone(cubito)
                        continue

                    pos = cubito.position_getter() # type: ignore

                    print("\n----------------")
                    print(f'idx = ({x}, {y}, {z})')
                    print(f'pos = ({pos.X}, {pos.Y}, {pos.Z})')

                    # verificar que la posición del cubido es lo mismo que
                    # sus indices
                    self.assertEqual(pos.X, x + desviacion)
                    self.assertEqual(pos.Y, y + desviacion)
                    self.assertEqual(pos.Z, z + desviacion)
