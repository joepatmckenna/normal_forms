
# # ppp and pp3
# def f(x, y, z, p=[0, .25, .5, 4, 3, 5]):
#     f1 = x * (1 - x) - p[3] * x * y
#     f2 = -p[1] * y + p[3] * x * y - p[4] * y * z - p[0] * (1 - exp(-p[5] * y))
#     f3 = -p[2] * z + p[4] * y * z
#     return f1, f2, f3


# J = nf.jet(f, (0, 0, 0), 3)
# print J.series[0]
# print J.series[1]
# print J.series[2]
