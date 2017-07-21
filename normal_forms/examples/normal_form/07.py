from normal_forms import normal_form
import sympy


# Murdock, Normal Forms and Unfoldings of Local Dynamical Systems, Example 4.5.24
def f(x, y, z):
    f1 = 6 * x + x**2 + x * y + x * z + y**2 + y * z + z**2
    f2 = 2 * y + x**2 + x * y + x * z + y**2 + y * z + z**2
    f3 = 3 * z + x**2 + x * y + x * z + y**2 + y * z + z**2
    return f1, f2, f3


h = normal_form(f, (0, 0, 0), 2)
# coeff of z**2
print h.fun[0].coeff(h.jet.var[2]**2)
