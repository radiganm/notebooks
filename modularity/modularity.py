#!/usr/bin/python3
### modularity.py
### Copyright 2017 Mac Radigan
### SPDX-License-Identifier: GFDL-1.3

# <headingcell level=1>
# modularity


# <headingcell level=2>
# Copying
# <rawcell>
# Copyright (C)  2017  Mac Radigan. 
# Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections and with no restrictions on the Front-Cover and back the Front-Cover Texts. A copy of the license is included in the section entitled "GNU Free Documentation License".


# <headingcell level=2>
# Introduction
# <markdowncell>
# For an integer seqence $n = 1, 2, \cdots \infty$, and choice of integers $b, m \in \mathbb{Z^+}$, what is the behavior of the sequence $\mathbf{X}_n = b^n \mod m$?


# <headingcell level=2>
# Dicussion
# <markdowncell>
# It is helpful to note that we can write $\mathbf{X} = \left[ \mathbf{G} \mathbf{H}^{*} \right]$, where $\mathbf{G}$ is a non-cylcic sequence of length $\left|\mathbf{G}\right|$, and $\mathbf{H}$ is a cylcic sequence of order $\left|\mathbf{H}\right|$.  We are first and primarily interested in what generalizations can be made about the lengths $\left|\mathbf{G}\right|$ and $\left|\mathbf{H}\right|$ for interesting constrained classes of $b$ and $m$.


# <headingcell level=2>
# Notation
# <markdowncell>
# For an integer seqence $n = 1, 2, \cdots \infty$, and choice of integers $b, m \in \mathbb{Z^+}$, what is the behavior of the sequence $\mathbf{X}_n = b^n \mod m$?


# <headingcell level=2>
# Normalization
# <markdowncell>
# It may be insightful to explore a normalized form having modulus $2 \pi$, giving the form $H_n = e^{i \phi_n + 2 \pi k}$ where $\phi_n = \left( 2 \pi \frac{b}{m} \right)^n$.


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


# <headingcell level=3>
# $\mathbf{X} = \left[ \mathbf{G} \mathbf{H}^{*} \right]$
# <codecell>
def hist(xs):
  """Builds a histogram h from values in xs"""
  h = defaultdict(int)
  for x in xs:
    h[x] += 1
  return h

def decompose(xs):
  """Decomposes a sequence xs in to a non-cyclic prefix, G, and repeated cyclic subsequence H"""
  x_hist = hist(xs)
  k1 = [ k for k,x in enumerate(xs) if x_hist[x] > 1 ][0]
  k2 = [ k+k1+1 for k,x in enumerate(xs[k1+1:]) if xs[k1] == x ][0]
  G  = xs[:k1]
  H  = xs[k1:k2]
  return G,H


# <headingcell level=3>
# A. Cases of historical interest
# <markdowncell>
# Fermat's Little Theorem states that if $m$ is prime, then for any integer $b$, it holds that $b^m - b$ is an integer multiple of $m$.
#
# This may be written as
#
# $b^m \equiv b \left( \mod m \right)$
#
# Also, if $m \nmid b$
#
# $b^{m-1} \equiv 1 \left( \mod m \right)$


# <headingcell level=4>
# Example A.1: $\mathbf{X}^\left({b=2,m=5}\right)$
# <markdowncell>
# We can check:
# <markdowncell>
# $b^m \equiv b \left( \mod m \right)$
# <codecell>
b = 2
m = 5
print("check:  %d == %d" % (b**m % m, b))
# <markdowncell>
# $b^{m-1} \equiv 1 \left( \mod m \right)$
# <codecell>
b = 2
m = 5
print("check:  %d == %d" % (b**(m-1) % m, 1))
# <markdowncell>
# so in this case
# \begin{aligned}
# \mathbf{X}_n = b^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 2
# \end{aligned}
# \begin{aligned}
# m = 5
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(2,5\right)} = \{ 2, 4, 3, 1, \cdots \} = \left[ \mathbf{G}^{\left(2,5\right)} \mathbf{H}^{\left(2,5\right)} \mathbf{H}^{\left(2,5\right)} \mathbf{H}^{\left(2,5\right)} \cdots \right] = \left[ \mathbf{G}^{\left(2,5\right)} \left(\mathbf{H}^{\left(2,5\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(2,5\right)} = \varnothing
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(2,5\right)} = \{ 2, 4, 3, 1 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(2,5\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(2,5\right)}\right| = 4
# \end{aligned}
# <codecell>
example(b=2, m=5) ##   X[n] = 2^n mod 5

# <headingcell level=4>
# Example A.2: $\mathbf{X}^\left({b=2,m=7}\right)$
# <markdowncell>
# We can check:
# <markdowncell>
# $b^m \equiv b \left( \mod m \right)$
# <codecell>
b = 2
m = 7
print("check:  %d == %d" % (b**m % m, b))
# <markdowncell>
# $b^{m-1} \equiv 1 \left( \mod m \right)$
# <codecell>
b = 2
m = 7
print("check:  %d == %d" % (b**(m-1) % m, 1))
# <markdowncell>
# so in this case
# \begin{aligned}
# \mathbf{X}_n = b^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 2
# \end{aligned}
# \begin{aligned}
# m = 7
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(2,7\right)} = \{ 2, 4, 1, 2, 4, 1, \cdots \} = \left[ \mathbf{G}^{\left(2,7\right)} \mathbf{H}^{\left(2,7\right)} \mathbf{H}^{\left(2,7\right)} \mathbf{H}^{\left(2,7\right)} \cdots \right] = \left[ \mathbf{G}^{\left(2,7\right)} \left(\mathbf{H}^{\left(2,7\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(2,7\right)} = \varnothing
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(2,7\right)} = \{ 2, 4, 1 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(2,7\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(2,7\right)}\right| = 3
# \end{aligned}
# <codecell>
example(b=2, m=7) ##   X[n] = 2^n mod 7


# <headingcell level=4>
# Example A.3: $\mathbf{X}^\left({b=3,m=7}\right)$
# <markdowncell>
# We can check:
# <markdowncell>
# $b^m \equiv b \left( \mod m \right)$
# <codecell>
b = 3
m = 7
print("check:  %d == %d" % (b**m % m, b))
# <markdowncell>
# $b^{m-1} \equiv 1 \left( \mod m \right)$
# <codecell>
b = 3
m = 7
print("check:  %d == %d" % (b**(m-1) % m, 1))
# <markdowncell>
# so in this case
# \begin{aligned}
# \mathbf{X}_n = b^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 3
# \end{aligned}
# \begin{aligned}
# m = 7
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(3,7\right)} = \{ 3, 2, 6, 4, 5, 1, 3, 2, 6, 4, 5, 1, \cdots \} = \left[ \mathbf{G}^{\left(3,7\right)} \mathbf{H}^{\left(3,7\right)} \mathbf{H}^{\left(3,7\right)} \mathbf{H}^{\left(3,7\right)} \cdots \right] = \left[ \mathbf{G}^{\left(3,7\right)} \left(\mathbf{H}^{\left(3,7\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(3,7\right)} = \varnothing
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(3,7\right)} = \{ 3, 2, 6, 4, 5, 1 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(3,7\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(3,7\right)}\right| = 6
# \end{aligned}
# <codecell>
example(b=3, m=7) ##   X[n] = 3^n mod 7


# <headingcell level=4>
# Example A.4: $\mathbf{X}^\left({b=5,m=7}\right)$
# <markdowncell>
# We can check:
# <markdowncell>
# $b^m \equiv b \left( \mod m \right)$
# <codecell>
b = 5
m = 7
print("check:  %d == %d" % (b**m % m, b))
# <markdowncell>
# $b^{m-1} \equiv 1 \left( \mod m \right)$
# <codecell>
b = 5
m = 7
print("check:  %d == %d" % (b**(m-1) % m, 1))
# <markdowncell>
# so in this case
# \begin{aligned}
# \mathbf{X}_n = b^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 5
# \end{aligned}
# \begin{aligned}
# m = 7
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(5,7\right)} = \{ 5, 4, 6, 2, 3, 1, 5, 4, 6, 2, 3, 1, \cdots \} = \left[ \mathbf{G}^{\left(5,7\right)} \mathbf{H}^{\left(5,7\right)} \mathbf{H}^{\left(5,7\right)} \mathbf{H}^{\left(5,7\right)} \cdots \right] = \left[ \mathbf{G}^{\left(5,7\right)} \left(\mathbf{H}^{\left(5,7\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(5,7\right)} = \varnothing
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(5,7\right)} = \{ 5, 4, 6, 2, 3, 1 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(5,7\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(5,7\right)}\right| = 6
# \end{aligned}
# <codecell>
example(b=5, m=7) ##   X[n] = 5^n mod 7


# <headingcell level=3>
# B. Examples exploring powers of two bases ($b = 2^k $  $ \exists k \in \mathbb{Z}^+$)

# <headingcell level=4>
# Example B.1: $\mathbf{X}^\left({b=2,m=10}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = b^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 2
# \end{aligned}
# \begin{aligned}
# m = 10
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(2,10\right)} = \{ 2, 4, 8, 6, 2, 4, 8, 6, \cdots \} = \left[ \mathbf{G}^{\left(2,10\right)} \mathbf{H}^{\left(2,10\right)} \mathbf{H}^{\left(2,10\right)} \mathbf{H}^{\left(2,10\right)} \cdots \right] = \left[ \mathbf{G}^{\left(2,10\right)} \left(\mathbf{H}^{\left(2,10\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(2,10\right)} = \varnothing
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(2,10\right)} = \{ 2, 4, 8, 6 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(2,10\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(2,10\right)}\right| = 4
# \end{aligned}
# <codecell>
example(b=2, m=10) ##   X[n] = 2^n mod 10


# <headingcell level=4>
# Example B.2: $\mathbf{X}^\left({b=4,m=10}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = b^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 4
# \end{aligned}
# \begin{aligned}
# m = 10
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(4,10\right)} = \{ 4, 6, 4, 6, \cdots \} = \left[ \mathbf{G}^{\left(4,10\right)} \mathbf{H}^{\left(4,10\right)} \mathbf{H}^{\left(4,10\right)} \mathbf{H}^{\left(4,10\right)} \cdots \right] = \left[ \mathbf{G}^{\left(4,10\right)} \left(\mathbf{H}^{\left(4,10\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(4,10\right)} = \varnothing
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(4,10\right)} = \{ 4, 6 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(4,10\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(4,10\right)}\right| = 2
# \end{aligned}
# <codecell>
example(b=4, m=10) ##   X[n] = 4^n mod 10


# <headingcell level=4>
# Example B.3: $\mathbf{X}^\left({b=8,m=10}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = b^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 8
# \end{aligned}
# \begin{aligned}
# m = 10
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(8,10\right)} = \{ 8, 6, 2, 4, 8, 6, 2, 4, \cdots \} = \left[ \mathbf{G}^{\left(8,10\right)} \mathbf{H}^{\left(8,10\right)} \mathbf{H}^{\left(8,10\right)} \mathbf{H}^{\left(8,10\right)} \cdots \right] = \left[ \mathbf{G}^{\left(8,10\right)} \left(\mathbf{H}^{\left(8,10\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(8,10\right)} = \varnothing
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(8,10\right)} = \{ 8, 6, 2, 4 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(8,10\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(8,10\right)}\right| = 4
# \end{aligned}
# <codecell>
example(b=8, m=10) ##   X[n] = 8^n mod 10


# <headingcell level=3>
# C. Interesting cases that give $\left|\mathbf{G}\right| \neq 0$


# <headingcell level=4>
# Example C.1: $\mathbf{X}^\left({b=12,m=40}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = b^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 12
# \end{aligned}
# \begin{aligned}
# m = 40
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(12,40\right)} = \{ 12, 24, 8, 16, 32, 24, 8, 16, 32, \cdots \} = \left[ \mathbf{G}^{\left(12,40\right)} \mathbf{H}^{\left(12,40\right)} \mathbf{H}^{\left(12,40\right)} \mathbf{H}^{\left(12,40\right)} \cdots \right] = \left[ \mathbf{G}^{\left(12,40\right)} \left(\mathbf{H}^{\left(12,40\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(12,40\right)} = \{ 12 \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(12,40\right)} = \{ 24, 8, 16, 32 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(12,40\right)}\right| = 1
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(12,40\right)}\right| = 4
# \end{aligned}
# <codecell>
example(b=12, m=40) ##   X[n] = 12^n mod 40


# <headingcell level=4>
# Example C.2: $\mathbf{X}^\left({b=45,m=175}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = b^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 45
# \end{aligned}
# \begin{aligned}
# m = 175
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(45,175\right)} = \{ 45, 100, 125, 25, 75, 50, 150, 100, 125, 25, 75, 50, 150, \cdots \} = \left[ \mathbf{G}^{\left(45,175\right)} \mathbf{H}^{\left(45,175\right)} \mathbf{H}^{\left(45,175\right)} \mathbf{H}^{\left(45,175\right)} \cdots \right] = \left[ \mathbf{G}^{\left(45,175\right)} \left(\mathbf{H}^{\left(45,175\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(45,175\right)} = \{ 45 \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(45,175\right)} = \{ 45, 100, 125, 25, 75, 50, 150 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(45,175\right)}\right| = 1
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(45,175\right)}\right| = 6
# \end{aligned}
# <codecell>
example(b=45, m=175) ##   X[n] = 45^n mod 175


# <headingcell level=4>
# Example C.3: $\mathbf{X}^\left({b=45,m=189}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = b^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 45
# \end{aligned}
# \begin{aligned}
# m = 189
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(45,189\right)} = \{ 135, 27, 81, 54, 108, 135, 27, 81, 54, 108, \cdots \} = \left[ \mathbf{G}^{\left(45,189\right)} \mathbf{H}^{\left(45,189\right)} \mathbf{H}^{\left(45,189\right)} \mathbf{H}^{\left(45,189\right)} \cdots \right] = \left[ \mathbf{G}^{\left(45,189\right)} \left(\mathbf{H}^{\left(45,189\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(45,189\right)} = \{ 45 \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(45,189\right)} = \{ 135, 27, 81, 54, 108 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(45,189\right)}\right| = 1
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(45,189\right)}\right| = 5
# \end{aligned}
# <codecell>
example(b=45, m=189) ##   X[n] = 45^n mod 189


# <rawcell>
### *EOF*
