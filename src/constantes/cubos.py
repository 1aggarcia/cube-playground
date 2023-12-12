from modelos.cubo import generar_cubo, crear_cubo_de_texto

CUBO_RESUELTO = generar_cubo(3)

MI_CUBO = crear_cubo_de_texto(
    u=
        [['U1', 'D2'],
        ['U3', 'U3']],
    d=
        [['R1', 'D2'],
        ['D3', 'L4']],
    f=
        [['F1', 'F2'],
        ['B3', 'R4']],
    b=
        [['F1', 'B2'],
        ['D3', 'B4']],
    l=
        [['L1', 'L2'],
        ['L3', 'U4']],
    r=
        [['R1', 'R2'],
        ['B3', 'F4']]
)

SUPERFLIP = crear_cubo_de_texto(
    u=
        [['U1', 'B2', 'U3'],
         ['L2', 'U5', 'R2'],
         ['U7', 'F2', 'U9']],
    d=
        [['D1', 'F8', 'D3'],
         ['L8', 'D5', 'R8'],
         ['D7', 'B8', 'D9']],
    f=
        [['F1', 'U8', 'F3'],
         ['L6', 'F5', 'R4'],
         ['F7', 'D2', 'F9']],
    b=
        [['B1', 'U2', 'B3'],
         ['R6', 'B5', 'L4'],
         ['B7', 'D8', 'B9']],
    l=
        [['L1', 'U4', 'L3'],
         ['B6', 'L5', 'F6'],
         ['L7', 'D4', 'L9']],
    r=
        [['R1', 'U6', 'R3'],
         ['F6', 'R5', 'B4'],
         ['R7', 'D6', 'R9']],
)
