from numpy import array, empty
from sympy import diff, lambdify, Matrix, ones, symbols
from sympy import zeros as sympy_zeros
from combinatorics import simplicial_seq
from multiindex import multiindex


class jet(object):
    """
    truncated Taylor's series

    variables:
    f: callable function that accepts $n$ arguments and returns a Sympy Matrix with dimension (m,1) corresponding to mathematical function $f:\mathbb{R}^n\rightarrow\mathbb{R}^m$
    x: number (if $n=1$) or iterable of $n$ numbers  (if $n\geq 1$) about which jet is expanded
    k: maxiumum degree of jet
    m: number of output arguments, i.e. dimension of range of $f$
    n: number of input arguments, i.e. dimension of domain of $f$
    var: $n$ Sympy variables x1,x2,...,xn
    coeff: jet coefficients indexed by coeff[degree,coord,term] where $0\leq$ degree $\leq k$, $0\leq$ coord $\leq m$, and $0\leq$ term $<{m-1+d \choose d)$ and $d$ is degree
    basis: monomial basis elements $\prod_{i\in S}(xi-x[i-1])$ where $S$ is a set in the power set of ${1,\ldots,n}$ and $|S|\leq k$ indexed by basis[degree][term]
    series: (m,1) Sympy Matrix symbolic representation of jet
    series_lam: callable lambdified version of series

    methods:
    __init__: compute series and create callable function corresponding to series
    __call__: evaluate the jet
    """

    def __init__(self, f, x, k):
        self.f = f
        self.x = x
        self.k = k
        if array(x).shape == ():
            n, m = 1, len(f(x))
            x = [x]
        else:
            n, m = len(x), len(f(*x))
        self.m = m
        self.n = n

        var = symbols('x1:%i' % (n + 1, ))

        self.var = var

        n_terms = simplicial_seq(n, k)

        coeff = [empty([n, n_terms[deg]]) for deg in range(k + 1)]
        basis = [ones(n_terms[deg], 1) for deg in range(k + 1)]
        coeff[0][:, 0] = f(*var).subs(zip(var, x))[0]
        for deg in range(1, k + 1):
            m_idx = multiindex(deg, n)
            for term in range(n_terms[deg]):
                coeff[deg][:, term] = list(
                    diff(f(*var), *m_idx.to_var(var)).subs(zip(var, x)) /
                    m_idx.factorial())
                basis[deg][term] = m_idx.to_polynomial(var, x)
                m_idx.increment()

        self.coeff = coeff
        self.basis = basis

        series = sympy_zeros(m, 1)
        for deg in range(k + 1):
            series += Matrix(coeff[deg]) * basis[deg]
        series.simplify()

        self.series = series
        self.series_lam = lambdify(var, series)

    def __call__(self, x):

        if array(x).shape == ():
            x = [x]

        return self.series_lam(*x)
