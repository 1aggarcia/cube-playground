from modelos.cubo import generar_cubo, crear_cubo_de_texto

CUBO_RESUELTO_3 = generar_cubo(3)
CUBO_RESUELTO_7 = generar_cubo(7)
CUBO_RESUELTO_25 = generar_cubo(25)

MI_CUBO = crear_cubo_de_texto(
    u=
        [['U', 'D'],
        ['U', 'U']],
    d=
        [['R', 'D'],
        ['D', 'L']],
    f=
        [['F', 'F'],
        ['B', 'R']],
    b=
        [['F', 'B'],
        ['D', 'B']],
    l=
        [['L', 'L'],
        ['L', 'U']],
    r=
        [['R', 'R'],
        ['B', 'F']]
)

SUPERFLIP = crear_cubo_de_texto(
    u=
        [['U', 'B', 'U'],
         ['L', 'U', 'R'],
         ['U', 'F', 'U']],
    d=
        [['D', 'F', 'D'],
         ['L', 'D', 'R'],
         ['D', 'B', 'D']],
    f=
        [['F', 'U', 'F'],
         ['L', 'F', 'R'],
         ['F', 'D', 'F']],
    b=
        [['B', 'U', 'B'],
         ['R', 'B', 'L'],
         ['B', 'D', 'B']],
    l=
        [['L', 'U', 'L'],
         ['B', 'L', 'F'],
         ['L', 'D', 'L']],
    r=
        [['R', 'U', 'R'],
         ['F', 'R', 'B'],
         ['R', 'D', 'R']],
)

ESQUINA_MALA = crear_cubo_de_texto(
    u=
        [['U', 'U', 'U'],
         ['U', 'U', 'U'],
         ['U', 'U', 'F']],
    d=
        [['D', 'D', 'D'],
         ['D', 'D', 'D'],
         ['D', 'D', 'D']],
    f=
        [['F', 'F', 'R'],
         ['F', 'F', 'F'],
         ['F', 'F', 'F']],
    b=
        [['B', 'B', 'B'],
         ['B', 'B', 'B'],
         ['B', 'B', 'B']],
    l=
        [['L', 'L', 'L'],
         ['L', 'L', 'L'],
         ['L', 'L', 'L']],
    r=
        [['U', 'R', 'R'],
         ['R', 'R', 'R'],
         ['R', 'R', 'R']],
)
