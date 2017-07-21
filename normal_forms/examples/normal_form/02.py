from normal_forms import normal_form
import sympy
from for_plotting import before_and_after


# Guckenheimer, Excercise 3.2.1b
def f(x, y):
    f1 = y - x * (x**2 + y**2)
    f2 = -x - y * (x**2 + y**2)
    return f1, f2


h = normal_form(f, (0, 0), 3)
before_and_after(f, h)
