#!/usr/bin/python3
### base_{{b}}.py
### {{META_AUTHOR}}
### {{META_LICENSE}}

# <headingcell level=1>
# base {{b}}


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


{% for b_n, b in enumerate(bs) %}

# <headingcell level=4>
# Example #{{b_n+1}}: $\mathbf{X}^\left({b={{b}},m={{m}}}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = {{b}}^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = {{b}} \\
# m = {{m}}
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left({{b}},{{m}}\right)} = \{ {{Gs}}, {{Hs}} \cdots \} = \left[ \mathbf{G}^{\left({{b}},{{m}}\right)} \mathbf{H}^{\left({{b}},{{m}}\right)} \mathbf{H}^{\left({{b}},{{m}}\right)} \mathbf{H}^{\left({{b}},{{m}}\right)} \cdots \right] = \left[ \mathbf{G}^{\left({{b}},{{m}}\right)} \left(\mathbf{H}^{\left({{b}},{{m}}\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left({{b}},{{m}}\right)} = \{ {{Gs}} \} \\
# \mathbf{H}^{\left({{b}},{{m}}\right)} = \{ {{Hs}} \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left({{b}},{{m}}\right)}\right| = {{G_N}} \\
# \left|\mathbf{H}^{\left({{b}},{{m}}\right)}\right| = {{H_N}}
# \end{aligned}
# <codecell>
example(b={{b}}, m={{m}}) ##   X[n] = {{b}}^n mod {{m}}


{% endfor %}

# <rawcell>
### *EOF*
