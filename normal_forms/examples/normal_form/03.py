from normal_forms import normal_form
import sympy
from for_plotting import before_and_after


# Guckenheimer, Excercise 3.2.1c
def f(x, y):
    f1 = x * x * x - 3 * x * y * y
    f2 = -3 * x * x * y + y * y * y
    return f1, f2


h = normal_form(f, (0, 0), 3)
before_and_after(f, h)
