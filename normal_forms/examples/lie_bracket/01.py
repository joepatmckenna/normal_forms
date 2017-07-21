from normal_forms.lie_bracket import lie_bracket
import sympy

var = sympy.symarray('x', (2, ))

# lie bracket Lg with g = (-y,x)
g = sympy.Matrix([-var[1], var[0]])
L = lie_bracket(g, var=var)

# Lg([x^3,y^3]) = [-3x^2y+y^3, -x^3+3xy^2]
f = sympy.Matrix([var[0]**3, var[1]**3])
print L(f)

# matrix for Lg acting on 2-dim 3rd degree polynomial vector fields
print L[3]
