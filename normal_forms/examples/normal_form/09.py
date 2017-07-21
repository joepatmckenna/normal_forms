from normal_forms import normal_form
import sympy

# ppp and pp3
def f(x, y, z, p=[0, .25, .5, 4, 3, 5]):
    f1 = x * (1 - x) - p[3] * x * y
    f2 = -p[1] * y + p[3] * x * y - p[4] * y * z - p[0] * (
        1 - sympy.exp(-p[5] * y))
    f3 = -p[2] * z + p[4] * y * z
    return f1, f2, f3

h = normal_form(f, (0, 0, 0), 4)
