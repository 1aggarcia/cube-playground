import numpy as np

def validar_caras(
                u: np.ndarray,
                d: np.ndarray,
                f: np.ndarray,
                b: np.ndarray,
                l: np.ndarray,
                r: np.ndarray
            ):
    '''
    Verifica que las caras dadas representan un cubo de rubik legal
    '''

    _validar_dimensiones(u, d, f, b, l, r)
    #_validarPegatinas(U, D, F, B, L, R)
    #_validarPedazos(U, D, F, B, L, R)

    return True


def _validar_dimensiones(
                u: np.ndarray,
                d: np.ndarray,
                f: np.ndarray,
                b: np.ndarray,
                l: np.ndarray,
                r: np.ndarray
            ):
    '''
    Verifica que cada cara tiene las mismas dimensiones nxnxn, donde n = len(U)
    * tira exepción si hay una cara que no tiene dimensiones nxn
    '''
    dimension = len(u)
    if dimension < 2:
        raise ValueError(f'dimension es < 2: {dimension}')
    for cara in [u, d, f, b, l, r]:
        if len(cara) != dimension:
            raise ValueError(f'dimensiones inexactas: {dimension}, {len(cara)}')
        for i in range(dimension):
            if len(cara[i]) != dimension:
                raise ValueError(f'dimensiones inexactas: {dimension}, {len(cara[i])}')

    return True


def _validar_pegatinas(u, d, f, b, l, r):
    raise NotImplementedError()


def _validar_pedazos(u, d, f, b, l, r):
    raise NotImplementedError()
