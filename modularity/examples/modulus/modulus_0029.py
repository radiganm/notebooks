#!/usr/bin/python3
### modulus_29.py
### Copyright 2017 Mac Radigan
### SPDX-License-Identifier: GFDL-1.3

# <headingcell level=1>
# modulus 29


# <headingcell level=2>
# Copying
# <rawcell>
# Copyright 2017 Mac Radigan
# # Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections and with no restrictions on the Front-Cover and back the Front-Cover Texts. A copy of the license is included in the section entitled "GNU Free Documentation License".  


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




# <headingcell level=4>
# Example #1: $\mathbf{X}^\left({b=2,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 2^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 2
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(2,29\right)} = \{ ,  2, 4, 8,16, 3, 6,12,24,19, 9,18, 7,14,28,27,25,21,13,26,23,17, 5,10,20,
 11,22,15, \cdots \} = \left[ \mathbf{G}^{\left(2,29\right)} \mathbf{H}^{\left(2,29\right)} \mathbf{H}^{\left(2,29\right)} \mathbf{H}^{\left(2,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(2,29\right)} \left(\mathbf{H}^{\left(2,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(2,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(2,29\right)} = \{  2, 4, 8,16, 3, 6,12,24,19, 9,18, 7,14,28,27,25,21,13,26,23,17, 5,10,20,
 11,22,15, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(2,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(2,29\right)}\right| = 28
# \end{aligned}
# <codecell>
example(b=2, m=29) ##   X[n] = 2^n mod 29




# <headingcell level=4>
# Example #2: $\mathbf{X}^\left({b=3,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 3^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 3
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(3,29\right)} = \{ ,  3, 9,27,23,11, 4,12, 7,21, 5,15,16,19,28,26,20, 2, 6,18,25,17,22, 8,24,
 14,13,10, \cdots \} = \left[ \mathbf{G}^{\left(3,29\right)} \mathbf{H}^{\left(3,29\right)} \mathbf{H}^{\left(3,29\right)} \mathbf{H}^{\left(3,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(3,29\right)} \left(\mathbf{H}^{\left(3,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(3,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(3,29\right)} = \{  3, 9,27,23,11, 4,12, 7,21, 5,15,16,19,28,26,20, 2, 6,18,25,17,22, 8,24,
 14,13,10, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(3,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(3,29\right)}\right| = 28
# \end{aligned}
# <codecell>
example(b=3, m=29) ##   X[n] = 3^n mod 29




# <headingcell level=4>
# Example #3: $\mathbf{X}^\left({b=4,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 4^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 4
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(4,29\right)} = \{ ,  4,16, 6,24, 9, 7,28,25,13,23, 5,20,22, \cdots \} = \left[ \mathbf{G}^{\left(4,29\right)} \mathbf{H}^{\left(4,29\right)} \mathbf{H}^{\left(4,29\right)} \mathbf{H}^{\left(4,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(4,29\right)} \left(\mathbf{H}^{\left(4,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(4,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(4,29\right)} = \{  4,16, 6,24, 9, 7,28,25,13,23, 5,20,22, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(4,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(4,29\right)}\right| = 14
# \end{aligned}
# <codecell>
example(b=4, m=29) ##   X[n] = 4^n mod 29




# <headingcell level=4>
# Example #4: $\mathbf{X}^\left({b=5,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 5^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 5
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(5,29\right)} = \{ ,  5,25, 9,16,22,23,28,24, 4,20,13, 7, 6, \cdots \} = \left[ \mathbf{G}^{\left(5,29\right)} \mathbf{H}^{\left(5,29\right)} \mathbf{H}^{\left(5,29\right)} \mathbf{H}^{\left(5,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(5,29\right)} \left(\mathbf{H}^{\left(5,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(5,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(5,29\right)} = \{  5,25, 9,16,22,23,28,24, 4,20,13, 7, 6, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(5,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(5,29\right)}\right| = 14
# \end{aligned}
# <codecell>
example(b=5, m=29) ##   X[n] = 5^n mod 29




# <headingcell level=4>
# Example #5: $\mathbf{X}^\left({b=6,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 6^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 6
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(6,29\right)} = \{ ,  6, 7,13,20, 4,24,28,23,22,16, 9,25, 5, \cdots \} = \left[ \mathbf{G}^{\left(6,29\right)} \mathbf{H}^{\left(6,29\right)} \mathbf{H}^{\left(6,29\right)} \mathbf{H}^{\left(6,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(6,29\right)} \left(\mathbf{H}^{\left(6,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(6,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(6,29\right)} = \{  6, 7,13,20, 4,24,28,23,22,16, 9,25, 5, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(6,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(6,29\right)}\right| = 14
# \end{aligned}
# <codecell>
example(b=6, m=29) ##   X[n] = 6^n mod 29




# <headingcell level=4>
# Example #6: $\mathbf{X}^\left({b=7,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 7^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 7
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(7,29\right)} = \{ ,  7,20,24,23,16,25, \cdots \} = \left[ \mathbf{G}^{\left(7,29\right)} \mathbf{H}^{\left(7,29\right)} \mathbf{H}^{\left(7,29\right)} \mathbf{H}^{\left(7,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(7,29\right)} \left(\mathbf{H}^{\left(7,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(7,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(7,29\right)} = \{  7,20,24,23,16,25, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(7,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(7,29\right)}\right| = 7
# \end{aligned}
# <codecell>
example(b=7, m=29) ##   X[n] = 7^n mod 29




# <headingcell level=4>
# Example #7: $\mathbf{X}^\left({b=8,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 8^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 8
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(8,29\right)} = \{ ,  8, 6,19, 7,27,13,17,20,15, 4, 3,24,18,28,21,23,10,22, 2,16,12, 9,14,25,
 26, 5,11, \cdots \} = \left[ \mathbf{G}^{\left(8,29\right)} \mathbf{H}^{\left(8,29\right)} \mathbf{H}^{\left(8,29\right)} \mathbf{H}^{\left(8,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(8,29\right)} \left(\mathbf{H}^{\left(8,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(8,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(8,29\right)} = \{  8, 6,19, 7,27,13,17,20,15, 4, 3,24,18,28,21,23,10,22, 2,16,12, 9,14,25,
 26, 5,11, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(8,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(8,29\right)}\right| = 28
# \end{aligned}
# <codecell>
example(b=8, m=29) ##   X[n] = 8^n mod 29




# <headingcell level=4>
# Example #8: $\mathbf{X}^\left({b=9,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 9^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 9
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(9,29\right)} = \{ ,  9,23, 4, 7, 5,16,28,20, 6,25,22,24,13, \cdots \} = \left[ \mathbf{G}^{\left(9,29\right)} \mathbf{H}^{\left(9,29\right)} \mathbf{H}^{\left(9,29\right)} \mathbf{H}^{\left(9,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(9,29\right)} \left(\mathbf{H}^{\left(9,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(9,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(9,29\right)} = \{  9,23, 4, 7, 5,16,28,20, 6,25,22,24,13, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(9,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(9,29\right)}\right| = 14
# \end{aligned}
# <codecell>
example(b=9, m=29) ##   X[n] = 9^n mod 29




# <headingcell level=4>
# Example #9: $\mathbf{X}^\left({b=10,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 10^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 10
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(10,29\right)} = \{ , 10,13,14,24, 8,22,17,25,18, 6, 2,20,26,28,19,16,15, 5,21, 7,12, 4,11,23,
 27, 9, 3, \cdots \} = \left[ \mathbf{G}^{\left(10,29\right)} \mathbf{H}^{\left(10,29\right)} \mathbf{H}^{\left(10,29\right)} \mathbf{H}^{\left(10,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(10,29\right)} \left(\mathbf{H}^{\left(10,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(10,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(10,29\right)} = \{ 10,13,14,24, 8,22,17,25,18, 6, 2,20,26,28,19,16,15, 5,21, 7,12, 4,11,23,
 27, 9, 3, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(10,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(10,29\right)}\right| = 28
# \end{aligned}
# <codecell>
example(b=10, m=29) ##   X[n] = 10^n mod 29




# <headingcell level=4>
# Example #10: $\mathbf{X}^\left({b=11,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 11^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 11
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(11,29\right)} = \{ , 11, 5,26,25,14, 9,12,16, 2,22,10,23,21,28,18,24, 3, 4,15,20,17,13,27, 7,
 19, 6, 8, \cdots \} = \left[ \mathbf{G}^{\left(11,29\right)} \mathbf{H}^{\left(11,29\right)} \mathbf{H}^{\left(11,29\right)} \mathbf{H}^{\left(11,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(11,29\right)} \left(\mathbf{H}^{\left(11,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(11,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(11,29\right)} = \{ 11, 5,26,25,14, 9,12,16, 2,22,10,23,21,28,18,24, 3, 4,15,20,17,13,27, 7,
 19, 6, 8, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(11,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(11,29\right)}\right| = 28
# \end{aligned}
# <codecell>
example(b=11, m=29) ##   X[n] = 11^n mod 29




# <headingcell level=4>
# Example #11: $\mathbf{X}^\left({b=12,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 12^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 12
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(12,29\right)} = \{ , 12,28,17, \cdots \} = \left[ \mathbf{G}^{\left(12,29\right)} \mathbf{H}^{\left(12,29\right)} \mathbf{H}^{\left(12,29\right)} \mathbf{H}^{\left(12,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(12,29\right)} \left(\mathbf{H}^{\left(12,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(12,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(12,29\right)} = \{ 12,28,17, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(12,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(12,29\right)}\right| = 4
# \end{aligned}
# <codecell>
example(b=12, m=29) ##   X[n] = 12^n mod 29




# <headingcell level=4>
# Example #12: $\mathbf{X}^\left({b=13,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 13^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 13
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(13,29\right)} = \{ , 13,24,22,25, 6,20,28,16, 5, 7, 4,23, 9, \cdots \} = \left[ \mathbf{G}^{\left(13,29\right)} \mathbf{H}^{\left(13,29\right)} \mathbf{H}^{\left(13,29\right)} \mathbf{H}^{\left(13,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(13,29\right)} \left(\mathbf{H}^{\left(13,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(13,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(13,29\right)} = \{ 13,24,22,25, 6,20,28,16, 5, 7, 4,23, 9, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(13,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(13,29\right)}\right| = 14
# \end{aligned}
# <codecell>
example(b=13, m=29) ##   X[n] = 13^n mod 29




# <headingcell level=4>
# Example #13: $\mathbf{X}^\left({b=14,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 14^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 14
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(14,29\right)} = \{ , 14,22,18,20,19, 5,12,23, 3,13, 8,25, 2,28,15, 7,11, 9,10,24,17, 6,26,16,
 21, 4,27, \cdots \} = \left[ \mathbf{G}^{\left(14,29\right)} \mathbf{H}^{\left(14,29\right)} \mathbf{H}^{\left(14,29\right)} \mathbf{H}^{\left(14,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(14,29\right)} \left(\mathbf{H}^{\left(14,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(14,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(14,29\right)} = \{ 14,22,18,20,19, 5,12,23, 3,13, 8,25, 2,28,15, 7,11, 9,10,24,17, 6,26,16,
 21, 4,27, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(14,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(14,29\right)}\right| = 28
# \end{aligned}
# <codecell>
example(b=14, m=29) ##   X[n] = 14^n mod 29




# <headingcell level=4>
# Example #14: $\mathbf{X}^\left({b=15,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 15^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 15
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(15,29\right)} = \{ , 15,22,11,20,10, 5,17,23,26,13,21,25,27,28,14, 7,18, 9,19,24,12, 6, 3,16,
  8, 4, 2, \cdots \} = \left[ \mathbf{G}^{\left(15,29\right)} \mathbf{H}^{\left(15,29\right)} \mathbf{H}^{\left(15,29\right)} \mathbf{H}^{\left(15,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(15,29\right)} \left(\mathbf{H}^{\left(15,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(15,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(15,29\right)} = \{ 15,22,11,20,10, 5,17,23,26,13,21,25,27,28,14, 7,18, 9,19,24,12, 6, 3,16,
  8, 4, 2, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(15,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(15,29\right)}\right| = 28
# \end{aligned}
# <codecell>
example(b=15, m=29) ##   X[n] = 15^n mod 29




# <headingcell level=4>
# Example #15: $\mathbf{X}^\left({b=16,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 16^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 16
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(16,29\right)} = \{ , 16,24, 7,25,23,20, \cdots \} = \left[ \mathbf{G}^{\left(16,29\right)} \mathbf{H}^{\left(16,29\right)} \mathbf{H}^{\left(16,29\right)} \mathbf{H}^{\left(16,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(16,29\right)} \left(\mathbf{H}^{\left(16,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(16,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(16,29\right)} = \{ 16,24, 7,25,23,20, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(16,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(16,29\right)}\right| = 7
# \end{aligned}
# <codecell>
example(b=16, m=29) ##   X[n] = 16^n mod 29




# <headingcell level=4>
# Example #16: $\mathbf{X}^\left({b=17,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 17^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 17
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(17,29\right)} = \{ , 17,28,12, \cdots \} = \left[ \mathbf{G}^{\left(17,29\right)} \mathbf{H}^{\left(17,29\right)} \mathbf{H}^{\left(17,29\right)} \mathbf{H}^{\left(17,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(17,29\right)} \left(\mathbf{H}^{\left(17,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(17,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(17,29\right)} = \{ 17,28,12, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(17,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(17,29\right)}\right| = 4
# \end{aligned}
# <codecell>
example(b=17, m=29) ##   X[n] = 17^n mod 29




# <headingcell level=4>
# Example #17: $\mathbf{X}^\left({b=18,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 18^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 18
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(18,29\right)} = \{ , 18, 5, 3,25,15, 9,17,16,27,22,19,23, 8,28,11,24,26, 4,14,20,12,13, 2, 7,
 10, 6,21, \cdots \} = \left[ \mathbf{G}^{\left(18,29\right)} \mathbf{H}^{\left(18,29\right)} \mathbf{H}^{\left(18,29\right)} \mathbf{H}^{\left(18,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(18,29\right)} \left(\mathbf{H}^{\left(18,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(18,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(18,29\right)} = \{ 18, 5, 3,25,15, 9,17,16,27,22,19,23, 8,28,11,24,26, 4,14,20,12,13, 2, 7,
 10, 6,21, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(18,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(18,29\right)}\right| = 28
# \end{aligned}
# <codecell>
example(b=18, m=29) ##   X[n] = 18^n mod 29




# <headingcell level=4>
# Example #18: $\mathbf{X}^\left({b=19,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 19^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 19
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(19,29\right)} = \{ , 19,13,15,24,21,22,12,25,11, 6,27,20, 3,28,10,16,14, 5, 8, 7,17, 4,18,23,
  2, 9,26, \cdots \} = \left[ \mathbf{G}^{\left(19,29\right)} \mathbf{H}^{\left(19,29\right)} \mathbf{H}^{\left(19,29\right)} \mathbf{H}^{\left(19,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(19,29\right)} \left(\mathbf{H}^{\left(19,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(19,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(19,29\right)} = \{ 19,13,15,24,21,22,12,25,11, 6,27,20, 3,28,10,16,14, 5, 8, 7,17, 4,18,23,
  2, 9,26, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(19,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(19,29\right)}\right| = 28
# \end{aligned}
# <codecell>
example(b=19, m=29) ##   X[n] = 19^n mod 29




# <headingcell level=4>
# Example #19: $\mathbf{X}^\left({b=20,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 20^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 20
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(20,29\right)} = \{ , 20,23,25, 7,24,16, \cdots \} = \left[ \mathbf{G}^{\left(20,29\right)} \mathbf{H}^{\left(20,29\right)} \mathbf{H}^{\left(20,29\right)} \mathbf{H}^{\left(20,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(20,29\right)} \left(\mathbf{H}^{\left(20,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(20,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(20,29\right)} = \{ 20,23,25, 7,24,16, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(20,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(20,29\right)}\right| = 7
# \end{aligned}
# <codecell>
example(b=20, m=29) ##   X[n] = 20^n mod 29




# <headingcell level=4>
# Example #20: $\mathbf{X}^\left({b=21,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 21^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 21
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(21,29\right)} = \{ , 21, 6,10, 7, 2,13,12,20,14, 4,26,24,11,28, 8,23,19,22,27,16,17, 9,15,25,
  3, 5,18, \cdots \} = \left[ \mathbf{G}^{\left(21,29\right)} \mathbf{H}^{\left(21,29\right)} \mathbf{H}^{\left(21,29\right)} \mathbf{H}^{\left(21,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(21,29\right)} \left(\mathbf{H}^{\left(21,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(21,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(21,29\right)} = \{ 21, 6,10, 7, 2,13,12,20,14, 4,26,24,11,28, 8,23,19,22,27,16,17, 9,15,25,
  3, 5,18, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(21,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(21,29\right)}\right| = 28
# \end{aligned}
# <codecell>
example(b=21, m=29) ##   X[n] = 21^n mod 29




# <headingcell level=4>
# Example #21: $\mathbf{X}^\left({b=22,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 22^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 22
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(22,29\right)} = \{ , 22,20, 5,23,13,25,28, 7, 9,24, 6,16, 4, \cdots \} = \left[ \mathbf{G}^{\left(22,29\right)} \mathbf{H}^{\left(22,29\right)} \mathbf{H}^{\left(22,29\right)} \mathbf{H}^{\left(22,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(22,29\right)} \left(\mathbf{H}^{\left(22,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(22,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(22,29\right)} = \{ 22,20, 5,23,13,25,28, 7, 9,24, 6,16, 4, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(22,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(22,29\right)}\right| = 14
# \end{aligned}
# <codecell>
example(b=22, m=29) ##   X[n] = 22^n mod 29




# <headingcell level=4>
# Example #22: $\mathbf{X}^\left({b=23,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 23^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 23
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(23,29\right)} = \{ , 23, 7,16,20,25,24, \cdots \} = \left[ \mathbf{G}^{\left(23,29\right)} \mathbf{H}^{\left(23,29\right)} \mathbf{H}^{\left(23,29\right)} \mathbf{H}^{\left(23,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(23,29\right)} \left(\mathbf{H}^{\left(23,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(23,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(23,29\right)} = \{ 23, 7,16,20,25,24, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(23,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(23,29\right)}\right| = 7
# \end{aligned}
# <codecell>
example(b=23, m=29) ##   X[n] = 23^n mod 29




# <headingcell level=4>
# Example #23: $\mathbf{X}^\left({b=24,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 24^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 24
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(24,29\right)} = \{ , 24,25,20,16, 7,23, \cdots \} = \left[ \mathbf{G}^{\left(24,29\right)} \mathbf{H}^{\left(24,29\right)} \mathbf{H}^{\left(24,29\right)} \mathbf{H}^{\left(24,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(24,29\right)} \left(\mathbf{H}^{\left(24,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(24,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(24,29\right)} = \{ 24,25,20,16, 7,23, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(24,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(24,29\right)}\right| = 7
# \end{aligned}
# <codecell>
example(b=24, m=29) ##   X[n] = 24^n mod 29




# <headingcell level=4>
# Example #24: $\mathbf{X}^\left({b=25,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 25^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 25
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(25,29\right)} = \{ , 25,16,23,24,20, 7, \cdots \} = \left[ \mathbf{G}^{\left(25,29\right)} \mathbf{H}^{\left(25,29\right)} \mathbf{H}^{\left(25,29\right)} \mathbf{H}^{\left(25,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(25,29\right)} \left(\mathbf{H}^{\left(25,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(25,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(25,29\right)} = \{ 25,16,23,24,20, 7, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(25,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(25,29\right)}\right| = 7
# \end{aligned}
# <codecell>
example(b=25, m=29) ##   X[n] = 25^n mod 29




# <headingcell level=4>
# Example #25: $\mathbf{X}^\left({b=26,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 26^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 26
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(26,29\right)} = \{ , 26, 9, 2,23,18, 4,17, 7, 8, 5,14,16,10,28, 3,20,27, 6,11,25,12,22,21,24,
 15,13,19, \cdots \} = \left[ \mathbf{G}^{\left(26,29\right)} \mathbf{H}^{\left(26,29\right)} \mathbf{H}^{\left(26,29\right)} \mathbf{H}^{\left(26,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(26,29\right)} \left(\mathbf{H}^{\left(26,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(26,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(26,29\right)} = \{ 26, 9, 2,23,18, 4,17, 7, 8, 5,14,16,10,28, 3,20,27, 6,11,25,12,22,21,24,
 15,13,19, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(26,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(26,29\right)}\right| = 28
# \end{aligned}
# <codecell>
example(b=26, m=29) ##   X[n] = 26^n mod 29




# <headingcell level=4>
# Example #26: $\mathbf{X}^\left({b=27,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,29\right)} = \{ , 27, 4,21,16,26, 6,17,24,10, 9,11, 7,15,28, 2,25, 8,13, 3,23,12, 5,19,20,
 18,22,14, \cdots \} = \left[ \mathbf{G}^{\left(27,29\right)} \mathbf{H}^{\left(27,29\right)} \mathbf{H}^{\left(27,29\right)} \mathbf{H}^{\left(27,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,29\right)} \left(\mathbf{H}^{\left(27,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,29\right)} = \{ 27, 4,21,16,26, 6,17,24,10, 9,11, 7,15,28, 2,25, 8,13, 3,23,12, 5,19,20,
 18,22,14, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,29\right)}\right| = 28
# \end{aligned}
# <codecell>
example(b=27, m=29) ##   X[n] = 27^n mod 29




# <headingcell level=4>
# Example #27: $\mathbf{X}^\left({b=28,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 28^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 28
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(28,29\right)} = \{ , 28, \cdots \} = \left[ \mathbf{G}^{\left(28,29\right)} \mathbf{H}^{\left(28,29\right)} \mathbf{H}^{\left(28,29\right)} \mathbf{H}^{\left(28,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(28,29\right)} \left(\mathbf{H}^{\left(28,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(28,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(28,29\right)} = \{ 28, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(28,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(28,29\right)}\right| = 2
# \end{aligned}
# <codecell>
example(b=28, m=29) ##   X[n] = 28^n mod 29




# <headingcell level=4>
# Example #28: $\mathbf{X}^\left({b=29,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 29^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 29
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(29,29\right)} = \{ ,  \cdots \} = \left[ \mathbf{G}^{\left(29,29\right)} \mathbf{H}^{\left(29,29\right)} \mathbf{H}^{\left(29,29\right)} \mathbf{H}^{\left(29,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(29,29\right)} \left(\mathbf{H}^{\left(29,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(29,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(29,29\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(29,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(29,29\right)}\right| = 1
# \end{aligned}
# <codecell>
example(b=29, m=29) ##   X[n] = 29^n mod 29




# <headingcell level=4>
# Example #29: $\mathbf{X}^\left({b=30,m=29}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 30^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 30
# \end{aligned}
# \begin{aligned}
# m = 29
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(30,29\right)} = \{ ,  \cdots \} = \left[ \mathbf{G}^{\left(30,29\right)} \mathbf{H}^{\left(30,29\right)} \mathbf{H}^{\left(30,29\right)} \mathbf{H}^{\left(30,29\right)} \cdots \right] = \left[ \mathbf{G}^{\left(30,29\right)} \left(\mathbf{H}^{\left(30,29\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(30,29\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(30,29\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(30,29\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(30,29\right)}\right| = 1
# \end{aligned}
# <codecell>
example(b=30, m=29) ##   X[n] = 30^n mod 29




# <rawcell>
### *EOF*