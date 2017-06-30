import numpy as np
import sympy
import combinatorics
from multiindex import multiindex


class jet(object):
    """
    truncated Taylor's series

    variables:
    f -- callable function that accepts $n$ arguments and returns
    a Sympy Matrix with dimension (m,1) corresponding to mathematical
    function $f:\mathbb{R}^n\rightarrow\mathbb{R}^m$
    x -- number (if $n=1$) or iterable of $n$ numbers  (if $n\geq 1$)
    about which jet is expanded
    k -- maxiumum degree of jet
    m -- number of output arguments, i.e. dimension of range of $f$
    n -- number of input arguments, i.e. dimension of domain of $f$
    var -- $n$ Sympy variables x1,x2,...,xn
    coeff: jet coefficients indexed by coeff[degree,coord,term] where
    $0\leq$ degree $\leq k$, $0\leq$ coord $\leq m$, and $0\leq$ term
    $<{m-1+d \choose d)$ and $d$ is degree
    basis -- monomial basis elements $\prod_{i\in S}(xi-x[i-1])$ where
    $S$ is a set in the power set of ${1,\ldots,n}$ and $|S|\leq k$
    indexed by basis[degree][term]
    series -- (m,1) Sympy Matrix symbolic representation of jet
    series_lam -- callable lambdified version of series

    methods:
    __init__ -- create callable jet function
    __call__ -- evaluate the jet
    """

    def __init__(self, f, x, k):
        self.f = f
        self.x = x
        self.k = k
        if np.array(x).shape == ():
            n, x = 1, [x]
        else:
            n = len(x)
        if np.array(f(*x)).shape == ():
            m = 1
        else:
            m = len(f(*x))
        self.m = m
        self.n = n

        # create list of n symbols
        var = sympy.symbols('x1:%i' % (n + 1, ))
        self.var = var

        # compute number of terms per degree in expanded form sum(coeff[:,deg]*basis[deg])
        n_terms = combinatorics.simplicial_seq(n, k)

        # compute coeff and basis element vectors of expanded form
        coeff = [np.empty([m, n_terms[deg]]) for deg in range(k + 1)]
        basis = [sympy.ones(n_terms[deg], 1) for deg in range(k + 1)]
        coeff[0][:, 0] = list(sympy.Matrix([f(*var)]).subs(zip(var, x)))
        for deg in range(1, k + 1):
            m_idx = multiindex(deg, n)
            for term in range(n_terms[deg]):
                coeff[deg][:, term] = list(
                    sympy.diff(sympy.Matrix([f(*var)]), *m_idx.to_var(var))
                    .subs(zip(var, x)) / m_idx.factorial())
                basis[deg][term] = m_idx.to_polynomial(var, x)
                m_idx.increment()
        self.coeff = coeff
        self.basis = basis

        # compute series and simplify
        series = sympy.zeros(m, 1)
        for deg in range(k + 1):
            series += sympy.Matrix(coeff[deg]) * basis[deg]
        series.simplify()
        self.series = series

        # lambdify series
        self.series_lam = sympy.lambdify(var, series)

    def __call__(self, x):

        if np.array(x).shape == ():
            x = [x]

        return self.series_lam(*x)
