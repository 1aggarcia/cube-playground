import unittest

from modelos import cubo3d

class ProbarCubo3d(unittest.TestCase):
    def test_generar_cubo3d(self):
        dim = 3
        desviacion = -1

        cubitos = cubo3d.generar_cubo3d(dim).cubitos()
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

                    pos = cubito.position_getter()

                    print("\n----------------")
                    print(f'idx = ({x}, {y}, {z})')
                    print(f'pos = ({pos.X}, {pos.Y}, {pos.Z})')

                    # verificar que la posición del cubido es lo mismo que
                    # sus indices
                    self.assertEqual(pos.X, x + desviacion)
                    self.assertEqual(pos.Y, y + desviacion)
                    self.assertEqual(pos.Z, z + desviacion)
