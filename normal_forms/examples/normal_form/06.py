from normal_forms import normal_form
import sympy
from for_plotting import before_and_after


# Guckenheimer, Excercise 7.3.1
def f(x, y):
    f1 = y
    f2 = x * x + x * y
    return f1, f2


h = normal_form(f, (0, 0), 3)
before_and_after(f, h)
