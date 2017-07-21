import sympy
f = lambda x, r=0: r + 1 - x - sympy.exp(-x)
from normal_forms import normal_form
h = normal_form(f, x=0, k=2)
print h.fun
print h(2)
