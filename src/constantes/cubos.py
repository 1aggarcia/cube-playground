from modelos.cubo import generarCubo, crearCuboDeTexto

CUBO_RESUELTO = generarCubo(3)

MI_CUBO = crearCuboDeTexto(
    U=
        [['U1', 'D2'],
        ['U3', 'U3']],
    D=
        [['R1', 'D2'],
        ['D3', 'L4']],
    F=
        [['F1', 'F2'],
        ['B3', 'R4']],
    B=
        [['F1', 'B2'],
        ['D3', 'B4']],
    L=
        [['L1', 'L2'],
        ['L3', 'U4']],
    R=
        [['R1', 'R2'],
        ['B3', 'F4']]
)

SUPERFLIP = crearCuboDeTexto(
    U=
        [['U1', 'B2', 'U3'],
         ['L2', 'U5', 'R2'],
         ['U7', 'F2', 'U9']],
    D=
        [['D1', 'F8', 'D3'],
         ['L8', 'D5', 'R8'],
         ['D7', 'B8', 'D9']],
    F=
        [['F1', 'U8', 'F3'],
         ['L6', 'F5', 'R4'],
         ['F7', 'D2', 'F9']],
    B=
        [['B1', 'U2', 'B3'],
         ['R6', 'B5', 'L4'],
         ['B7', 'D8', 'B9']],
    L=
        [['L1', 'U4', 'L3'],
         ['B6', 'L5', 'F6'],
         ['L7', 'D4', 'L9']],
    R=
        [['R1', 'U6', 'R3'],
         ['F6', 'R5', 'B4'],
         ['R7', 'D6', 'R9']],
)