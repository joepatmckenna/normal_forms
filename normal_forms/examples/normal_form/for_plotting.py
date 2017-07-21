import matplotlib.pyplot as plt
import numpy as np

def before_and_after(f, h, x_min=-1, x_max=1, y_min=-1, y_max=1):
    fig, ax = plt.subplots(1, 2, figsize=(8, 3))

    x = np.linspace(x_min, x_max, 500)
    y = np.linspace(y_min, y_max, 500)
    X, Y = np.meshgrid(x, y)

    Z = np.array([[f(xi, yi) for xi in x] for yi in y])
    ax[0].contour(X, Y, Z[..., 0], [0])
    ax[0].contour(X, Y, Z[..., 1], [0])
    ax[0].streamplot(X, Y, Z[..., 0], Z[..., 1])

    Z = np.array([[h(xi, yi) for xi in x] for yi in y])
    ax[1].contour(X, Y, Z[..., 0], [0])
    ax[1].contour(X, Y, Z[..., 1], [0])
    ax[1].streamplot(X, Y, Z[..., 0], Z[..., 1])

    plt.show()
