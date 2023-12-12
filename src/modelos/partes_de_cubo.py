from constantes.enums import Cara

class Etiqueta:
    '''
    Representa una etiqueta con la cara donde pertenece y su posición, entre 1-n^2
    '''
    def __init__(self, cara: Cara, posicion: int):
        self.cara = cara
        self.posicion = posicion

    def __str__(self):
        return f'{self.cara.value}{self.posicion}'

    def __eq__(self, __value: object) -> bool:
        return (
            isinstance(__value, Etiqueta) and
            self.cara == __value.cara and
            self.posicion == __value.posicion
        )


def etiqueta_de_texto(texto: str):
    '''
    Crear una Etiqueta desde una cadena de caracteres, ej 'D3'
    * requiere que el primer carácter sea una cara
    * requiere que los demás caracteres sean enteros
    '''
    # verificar que texto se puede convertir en una etiqueta
    if len(texto) < 2:
        raise ValueError('Etiqueta debe tener al menos 2 caracteres')
    cara_convertida = Cara[texto[0]]
    if cara_convertida is None:
        raise ValueError('Etiqueta tiene que empezar con la cara')
    posicion_convertida = int(texto[1:])

    # crearla
    return Etiqueta(cara_convertida, posicion_convertida)
