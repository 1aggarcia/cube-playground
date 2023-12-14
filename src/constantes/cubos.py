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

ESQUINA_MALA = crear_cubo_de_texto(
    u=
        [['U1', 'U2', 'U3'],
         ['U4', 'U5', 'U6'],
         ['U7', 'U8', 'F3']],
    d=
        [['D1', 'D2', 'D3'],
         ['D4', 'D5', 'D6'],
         ['D7', 'D8', 'D9']],
    f=
        [['F1', 'F2', 'R1'],
         ['F4', 'F5', 'F6'],
         ['F7', 'F8', 'F9']],
    b=
        [['B1', 'B2', 'B3'],
         ['B4', 'B5', 'B6'],
         ['B7', 'B8', 'B9']],
    l=
        [['L1', 'L2', 'L3'],
         ['L4', 'L5', 'L6'],
         ['L7', 'L8', 'L9']],
    r=
        [['U9', 'R2', 'R3'],
         ['R4', 'R5', 'R6'],
         ['R7', 'R8', 'R9']],
)
