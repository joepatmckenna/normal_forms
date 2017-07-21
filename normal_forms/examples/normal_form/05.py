from normal_forms import normal_form
import sympy
import numpy as np
from for_plotting import before_and_after


# Guckenheimer, Equation 2.2.6
def f(x, y, beta=1, delta=0):
    f1 = y
    f2 = beta * x - x * x * x - delta * y
    return f1, f2


h = normal_form(f, (0, 0), 3)
before_and_after(f, h, -2, 2, -2, 2)

