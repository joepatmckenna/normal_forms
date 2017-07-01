Taylor's Series
===============

The :math:`k`-jet centered at :math:`x_0` of a function :math:`f(x)` is the Taylor's series truncated at degree :math:`k`:

.. math::

   J_k(x) = \sum_{0\leq |\alpha|\leq k}\frac{f^{(\alpha)}(x_0)}{\alpha!}(x-x_0)^{\alpha}.

This formula makes sense for :math:`f:\mathbb{R}^n\rightarrow\mathbb{R}^m` with any natural number dimensions :math:`n` and :math:`m` when :math:`\alpha` is a multiindex :math:`\alpha=(\alpha_1,\ldots,\alpha_n)` with differentiation, exponentiation, factorial, and absolute value defined as

.. math::

   f^{(\alpha)} &= \frac{\partial^{\alpha_1}}{\partial^{\alpha_1} x_1}\cdots\frac{\partial^{\alpha_n}}{\partial^{\alpha_n} x_n}f \\
   x^{\alpha} &= x^{\alpha_1}\cdots x^{\alpha_n} \\
   \alpha! &= \alpha_1!\cdots\alpha_n! \\
   |\alpha| &= |\alpha_1|+\cdots|\alpha_n|

This package implements a class :class:`normal_forms.jet.jet` that can be used to manipulate and evaluate jets. For now, if :math:`f` is defined in terms of any other operators than the standard ``+-*\``, then the ``Sympy`` version of that function should be used. Once the ``jet`` is created, it can be evaluated at arbitrary points::

  >>> import normal_forms as nf
  >>> from sympy import exp
  >>> f = lambda x: exp(x)
  >>> J = nf.jet(f, x=0, k=10)
  >>> print J(1)
  >>> 2.718281801146385

Examples
~~~~~~~~

The domain and range may have the same dimension (:math:`n=m`), for example, :math:`f(x)=\sin(x)`:

.. plot:: normal_forms/examples/jet/jet1.py

The dimension of the range may be greater than the dimension of the domain (:math:`n<m`), for example, :math:`f(t)=(\sin(t),\cos(t))` viewed here as a parametric plot in the :math:`xy`-plane:

.. plot:: normal_forms/examples/jet/jet2.py

The dimension of the range may be less than the dimension of the domain (:math:`n>m`), for example, :math:`f(x,y)=\sin(x)\cos(y)`:

.. plot:: normal_forms/examples/jet/jet3.py
