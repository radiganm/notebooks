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


{% for m_n, mx in enumerate(ms) %}

# <headingcell level=4>
# Example #{{m_n+1}}: $\mathbf{X}^\left({b={{b}},m={{mx}}}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = {{b}}^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = {{b}}
# \end{aligned}
# \begin{aligned}
# m = {{mx}}
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left({{b}},{{mx}}\right)} = \{ {{Gs}}, {{Hs}} \cdots \} = \left[ \mathbf{G}^{\left({{b}},{{mx}}\right)} \mathbf{H}^{\left({{b}},{{mx}}\right)} \mathbf{H}^{\left({{b}},{{mx}}\right)} \mathbf{H}^{\left({{b}},{{mx}}\right)} \cdots \right] = \left[ \mathbf{G}^{\left({{b}},{{mx}}\right)} \left(\mathbf{H}^{\left({{b}},{{mx}}\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left({{b}},{{mx}}\right)} = \{ {{Gs}} \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left({{b}},{{mx}}\right)} = \{ {{Hs}} \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left({{b}},{{mx}}\right)}\right| = {{G_N}}
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left({{b}},{{mx}}\right)}\right| = {{H_N}}
# \end{aligned}
# <codecell>
example(b={{b}}, m={{mx}}) ##   X[n] = {{b}}^n mod {{mx}}


{% endfor %}

# <rawcell>
### *EOF*
