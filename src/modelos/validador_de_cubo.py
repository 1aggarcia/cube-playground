from .partes_de_cubo import Etiqueta

def validarCaras(
                U: list[list[Etiqueta]], 
                D: list[list[Etiqueta]], 
                F: list[list[Etiqueta]], 
                B: list[list[Etiqueta]], 
                L: list[list[Etiqueta]], 
                R: list[list[Etiqueta]]
            ):
    '''
    Verifica que las caras dadas representan un cubo de rubik legal
    '''

    _validarDimensiones(U, D, F, B, L, R)
    #_validarPegatinas(U, D, F, B, L, R)
    #_validarPedazos(U, D, F, B, L, R)

    return True

def _validarDimensiones(
                U: list[list[Etiqueta]], 
                D: list[list[Etiqueta]], 
                F: list[list[Etiqueta]], 
                B: list[list[Etiqueta]], 
                L: list[list[Etiqueta]], 
                R: list[list[Etiqueta]]
            ):
    '''
    Verifica que cada cara tiene las mismas dimensiones nxnxn, donde n = len(U)
    * tira exepción si hay una cara que no tiene dimensiones nxn
    '''
    dimension = len(U)
    if dimension < 2:
        raise ValueError(f'dimension es < 2: {dimension}')
    for cara in [U, D, F, B, L, R]:
        if len(cara) != dimension:
            raise ValueError(f'dimensiones inexactas: {dimension}, {len(cara)}')
        for i in range(dimension):
            if len(cara[i]) != dimension:
                raise ValueError(f'dimensiones inexactas: {dimension}, {len(cara[i])}')

    return True

def _validarPegatinas(U, D, F, B, L, R):
    raise Exception('método no implmementado')

def _validarPedazos(U, D, F, B, L, R):
    raise Exception('método no implmementado')