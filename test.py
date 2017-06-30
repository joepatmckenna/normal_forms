import normal_forms as nf
from sympy.functions import sin, cos, exp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# f:R1->R1


def f(x):
    return sin(x)


fig, ax = plt.subplots(1, 1)

# grid
x = np.linspace(-np.pi, np.pi)

# plot f
ax.plot(x, [f(xi) for xi in x], 'k-', lw=3, label='$f$')

# plot k-jets for k=1,3,5,7,9
for k in range(1, 10, 2):
    J = nf.jet(f, 0, k)
    ax.plot(x, [J(xi)[0, 0] for xi in x], label='$T_{%i}$' % (k, ))

# limits and legend
ax.set_ylim(-2, 2)
plt.legend()

plt.show()
plt.close()

# f:R1->R2


def f(x):
    return sin(x), cos(x)


fig, ax = plt.subplots(1, 1)
x = np.linspace(-np.pi, np.pi)
y = np.array([f(xi) for xi in x])
ax.plot(y[:, 0], y[:, 1], 'k-', lw=3, label='$f$')

for k in range(1, 10, 2):
    J = nf.jet(f, 0, k)
    y = np.array([J(xi)[:, 0] for xi in x])
    ax.plot(y[:, 0], y[:, 1], label='$T_{%i}$' % (k, ))

# limits and legend
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

plt.legend()
plt.show()
plt.close()

# f:R2->R1


def f(x, y):
    return sin(x) * cos(y)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-np.pi, np.pi)
y = np.linspace(-np.pi, np.pi)
X, Y = np.meshgrid(x, y)
Z = [[f(xi, yi) for yi in Y[:, 0]] for xi in X[0]]
ax.plot_wireframe(X, Y, Z, color='k', rstride=5, cstride=5, label='$f$')

J = nf.jet(f, (0, 0), 10)
Z = [[J((xi, yi))[0, 0] for yi in Y[:, 0]] for xi in X[0]]
ax.plot_wireframe(X, Y, Z, color='b', rstride=5, cstride=5, label='$T_{10}$')

ax.set_zlim(-2, 2)
plt.legend()
plt.show()
plt.close()


# ppp and pp3
def f(x, y, z, p=[0, .25, .5, 4, 3, 5]):
    f1 = x * (1 - x) - p[3] * x * y
    f2 = -p[1] * y + p[3] * x * y - p[4] * y * z - p[0] * (1 - exp(-p[5] * y))
    f3 = -p[2] * z + p[4] * y * z
    return f1, f2, f3


J = nf.jet(f, (0, 0, 0), 3)
print J.series[0]
print J.series[1]
print J.series[2]
