#!/usr/bin/python3
### modulus_{{m}}.py
### {{META_AUTHOR}}
### {{META_LICENSE}}

# <headingcell level=1>
# modulus {{m}}


# <headingcell level=2>
# Copying
# <rawcell>
# {{META_AUTHOR}}
# {{META_LICENSE_TEXT}}


# <headingcell level=3>
# $b^n \mod m$ for $n = 1, 2, \cdots 30$
# <codecell>
def example(b,m):
  """Prints the sequence X_n = b^n mod m for n = 1, 2, ... N"""
  N  = 30
  ns = range(1, N)
  f  = lambda n: b**n % m
  xs = map(f, ns)
  print(list(xs))


{% for b_n, bx in enumerate(bs) %}

# <headingcell level=4>
# Example #{{b_n+1}}: $\mathbf{X}^\left({b={{bx}},m={{m}}}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = {{bx}}^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = {{bx}}
# \end{aligned}
# \begin{aligned}
# m = {{m}}
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left({{bx}},{{m}}\right)} = \{ {{dat[bx][m]['Gs']}}, {{dat[bx][m]['Hs']}} \cdots \} = \left[ \mathbf{G}^{\left({{bx}},{{m}}\right)} \mathbf{H}^{\left({{bx}},{{m}}\right)} \mathbf{H}^{\left({{bx}},{{m}}\right)} \mathbf{H}^{\left({{bx}},{{m}}\right)} \cdots \right] = \left[ \mathbf{G}^{\left({{bx}},{{m}}\right)} \left(\mathbf{H}^{\left({{bx}},{{m}}\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left({{bx}},{{m}}\right)} = \{ {{dat[bx][m]['Gs']}} \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left({{bx}},{{m}}\right)} = \{ {{dat[bx][m]['Hs']}} \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left({{bx}},{{m}}\right)}\right| = {{dat[bx][m]['G_N']}}
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left({{bx}},{{m}}\right)}\right| = {{dat[bx][m]['H_N']}}
# \end{aligned}
# <codecell>
example(b={{bx}}, m={{m}}) ##   X[n] = {{bx}}^n mod {{m}}


{% endfor %}

# <rawcell>
### *EOF*
