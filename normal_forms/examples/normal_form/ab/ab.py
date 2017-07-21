from normal_forms import normal_form
import sympy
import numpy as np
import auto


def f(x, y, p1, p2, p3):
    f1 = -x + p1 * (1 - x) * sympy.exp(y)
    f2 = -y + p1 * p2 * (1 - x) * sympy.exp(y) - p3 * y
    return f1, f2


# continue in par 2
start = auto.run(
    e='ab',
    c='ab.1',
    unames={1: 'x',
            2: 'y'},
    parnames={1: 'p1',
              2: 'p2',
              3: 'p3'},
    U={'x': 0,
       'y': 0},
    PAR={'p1': 0,
         'p2': 8,
         'p3': 3},
    ICP=['p2'],
    RL1=14)

ab = auto.run(start('EP2'), c='ab.2')

ab = auto.rl(ab)
auto.sv(ab, 'ab')

auto.cl()

hb = ab('HB1')
p = hb['p1'], hb['p2'], hb['p3']
x = hb['x'][0], hb['y'][0]

h = normal_form(f, x, 3, p)
