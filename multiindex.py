from numpy import max, product
from numpy import zeros as numpy_zeros
from combinatorics import factorial_seq


class multiindex(object):
    """
    a multiindex object

    idx -- list of indices
    """

    def __init__(self, n, idx_max=None):
        """
        initialize indices

        n -- length of multiindex
        idx_max -- upper bound of (exclusive) of indices
        """

        self.idx = numpy_zeros(n, dtype=int)
        self.idx_max = idx_max

    def increment(self):
        """
        Increment multiindex. A 'telephone-book' ordering is used and indices are assumed to be increasing from left to right. For example, the multiindices of length 2 with individual indices less than idx_max=3 are, in increasing order: (0,0), (0,1), (0,2), (1,1), (1,2), (2,2). Next multiindex is cycled back to the first multiindex.
        """

        n_idx = len(self.idx)
        if all(self.idx >= self.idx_max):
            self.idx = numpy_zeros(n_idx, dtype=int)
        else:
            i = n_idx - 1
            self.idx[i] += 1
            while self.idx[i] == self.idx_max:
                i -= 1
                self.idx[i] += 1
            self.idx[i:] = self.idx[i]

    def to_polynomial(self, var, x):
        """
        convert multiindex to corresponding polynomial

        var -- list of Sympy variables
        x -- roots of polynomials
        """

        return product([var[idx] - x[idx] for idx in self.idx])

    def to_var(self, var):
        """
        convert multiindex to list of variables

        var -- list of Sympy variables x1,x2,...,xn
        """
        return [var[idx] for idx in self.idx]

    def factorial(self):
        """calculate multiindex factorial"""

        fac_key = numpy_zeros(self.idx_max, dtype=int)
        for idx in self.idx:
            fac_key[idx] += 1
        fac = factorial_seq(int(max(fac_key)))
        return product([fac[key] for key in fac_key])
