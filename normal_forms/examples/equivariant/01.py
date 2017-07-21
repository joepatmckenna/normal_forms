from normal_forms import normal_form
from normal_forms.lie_bracket import lie_bracket
import sympy


# Guckenheimer, Excercise 7.3.1
def f(x, y):
    f1 = y
    f2 = x * x + x * y
    return f1, f2


k = 5
h = normal_form(f, (0, 0), k)

# each normal form term for deg>1 is in the nullspace of transpose(L1)
print np.isclose(
    np.sum([
        np.linalg.norm(np.concatenate(h.jet.coeff[deg]).dot(h.L1[deg]))
        for deg in range(2, k + 1)
    ]), 0)

# how equivariant representation is related to the normal form
eqv_rep = h.jet.fun_deg[0] + h.jet.fun_deg[1]
for e in h.eqv:
    eqv_rep += e[0].dot(e[1])

for coord in range(h.m):
    print series[coord]
    print h.fun[coord]
