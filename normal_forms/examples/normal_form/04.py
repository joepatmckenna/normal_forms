from normal_forms import normal_form
import sympy
from for_plotting import before_and_after


# Guckenheimer, Excercise 3.2.1d
def f(x, y):
    f1 = x * y + x * x * x
    f2 = -y - x * x * y
    return f1, f2


h = normal_form(f, (0, 0), 3)
before_and_after(f, h)
