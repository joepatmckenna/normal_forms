from numpy import empty

def factorial_seq(n):
    """Return a sequence of factorials from 0! to n!."""
    seq = empty(n + 1, dtype=int)
    seq[0] = 1
    for i in range(1, n + 1):
        seq[i] = seq[i - 1] * i
    return seq


def simplicial_seq(n, k):
    """
    Return a list of simplicial numbers (n+j-1 choose j) for j=0,..k.
    (n+j-1 choose j) is the number of jth degree partial derivatives of
    a function f with dim(domain(f)) = n.

    Keyword arguments:
    n -- dim(domain(f)).
    k -- maximum derivative degree.
    """
    seq = empty(k + 1, dtype=int)
    seq[0] = 1
    for i in range(1, k + 1):
        seq[i] = seq[i - 1] * (n + i - 1) / i
    return seq
