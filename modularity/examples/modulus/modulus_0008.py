#!/usr/bin/python3
### modulus_8.py
### Copyright 2017 Mac Radigan
### SPDX-License-Identifier: GFDL-1.3

# <headingcell level=1>
# modulus 8


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
# Example #1: $\mathbf{X}^\left({b=2,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 2^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 2
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(2,8\right)} = \{ 2,  \cdots \} = \left[ \mathbf{G}^{\left(2,8\right)} \mathbf{H}^{\left(2,8\right)} \mathbf{H}^{\left(2,8\right)} \mathbf{H}^{\left(2,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(2,8\right)} \left(\mathbf{H}^{\left(2,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(2,8\right)} = \{ 2 \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(2,8\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(2,8\right)}\right| = 2
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(2,8\right)}\right| = 1
# \end{aligned}
# <codecell>
example(b=2, m=8) ##   X[n] = 2^n mod 8




# <headingcell level=4>
# Example #2: $\mathbf{X}^\left({b=3,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 3^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 3
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(3,8\right)} = \{ , 3 \cdots \} = \left[ \mathbf{G}^{\left(3,8\right)} \mathbf{H}^{\left(3,8\right)} \mathbf{H}^{\left(3,8\right)} \mathbf{H}^{\left(3,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(3,8\right)} \left(\mathbf{H}^{\left(3,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(3,8\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(3,8\right)} = \{ 3 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(3,8\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(3,8\right)}\right| = 2
# \end{aligned}
# <codecell>
example(b=3, m=8) ##   X[n] = 3^n mod 8




# <headingcell level=4>
# Example #3: $\mathbf{X}^\left({b=4,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 4^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 4
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(4,8\right)} = \{ ,  \cdots \} = \left[ \mathbf{G}^{\left(4,8\right)} \mathbf{H}^{\left(4,8\right)} \mathbf{H}^{\left(4,8\right)} \mathbf{H}^{\left(4,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(4,8\right)} \left(\mathbf{H}^{\left(4,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(4,8\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(4,8\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(4,8\right)}\right| = 1
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(4,8\right)}\right| = 1
# \end{aligned}
# <codecell>
example(b=4, m=8) ##   X[n] = 4^n mod 8




# <headingcell level=4>
# Example #4: $\mathbf{X}^\left({b=5,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 5^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 5
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(5,8\right)} = \{ , 5 \cdots \} = \left[ \mathbf{G}^{\left(5,8\right)} \mathbf{H}^{\left(5,8\right)} \mathbf{H}^{\left(5,8\right)} \mathbf{H}^{\left(5,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(5,8\right)} \left(\mathbf{H}^{\left(5,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(5,8\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(5,8\right)} = \{ 5 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(5,8\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(5,8\right)}\right| = 2
# \end{aligned}
# <codecell>
example(b=5, m=8) ##   X[n] = 5^n mod 8




# <headingcell level=4>
# Example #5: $\mathbf{X}^\left({b=6,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 6^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 6
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(6,8\right)} = \{ 6,  \cdots \} = \left[ \mathbf{G}^{\left(6,8\right)} \mathbf{H}^{\left(6,8\right)} \mathbf{H}^{\left(6,8\right)} \mathbf{H}^{\left(6,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(6,8\right)} \left(\mathbf{H}^{\left(6,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(6,8\right)} = \{ 6 \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(6,8\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(6,8\right)}\right| = 2
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(6,8\right)}\right| = 1
# \end{aligned}
# <codecell>
example(b=6, m=8) ##   X[n] = 6^n mod 8




# <headingcell level=4>
# Example #6: $\mathbf{X}^\left({b=7,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 7^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 7
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(7,8\right)} = \{ , 7 \cdots \} = \left[ \mathbf{G}^{\left(7,8\right)} \mathbf{H}^{\left(7,8\right)} \mathbf{H}^{\left(7,8\right)} \mathbf{H}^{\left(7,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(7,8\right)} \left(\mathbf{H}^{\left(7,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(7,8\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(7,8\right)} = \{ 7 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(7,8\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(7,8\right)}\right| = 2
# \end{aligned}
# <codecell>
example(b=7, m=8) ##   X[n] = 7^n mod 8




# <headingcell level=4>
# Example #7: $\mathbf{X}^\left({b=8,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 8^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 8
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(8,8\right)} = \{ ,  \cdots \} = \left[ \mathbf{G}^{\left(8,8\right)} \mathbf{H}^{\left(8,8\right)} \mathbf{H}^{\left(8,8\right)} \mathbf{H}^{\left(8,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(8,8\right)} \left(\mathbf{H}^{\left(8,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(8,8\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(8,8\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(8,8\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(8,8\right)}\right| = 1
# \end{aligned}
# <codecell>
example(b=8, m=8) ##   X[n] = 8^n mod 8




# <headingcell level=4>
# Example #8: $\mathbf{X}^\left({b=9,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 9^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 9
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(9,8\right)} = \{ ,  \cdots \} = \left[ \mathbf{G}^{\left(9,8\right)} \mathbf{H}^{\left(9,8\right)} \mathbf{H}^{\left(9,8\right)} \mathbf{H}^{\left(9,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(9,8\right)} \left(\mathbf{H}^{\left(9,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(9,8\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(9,8\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(9,8\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(9,8\right)}\right| = 1
# \end{aligned}
# <codecell>
example(b=9, m=8) ##   X[n] = 9^n mod 8




# <headingcell level=4>
# Example #9: $\mathbf{X}^\left({b=10,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 10^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 10
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(10,8\right)} = \{ 2,  \cdots \} = \left[ \mathbf{G}^{\left(10,8\right)} \mathbf{H}^{\left(10,8\right)} \mathbf{H}^{\left(10,8\right)} \mathbf{H}^{\left(10,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(10,8\right)} \left(\mathbf{H}^{\left(10,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(10,8\right)} = \{ 2 \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(10,8\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(10,8\right)}\right| = 2
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(10,8\right)}\right| = 1
# \end{aligned}
# <codecell>
example(b=10, m=8) ##   X[n] = 10^n mod 8




# <headingcell level=4>
# Example #10: $\mathbf{X}^\left({b=11,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 11^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 11
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(11,8\right)} = \{ , 3 \cdots \} = \left[ \mathbf{G}^{\left(11,8\right)} \mathbf{H}^{\left(11,8\right)} \mathbf{H}^{\left(11,8\right)} \mathbf{H}^{\left(11,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(11,8\right)} \left(\mathbf{H}^{\left(11,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(11,8\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(11,8\right)} = \{ 3 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(11,8\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(11,8\right)}\right| = 2
# \end{aligned}
# <codecell>
example(b=11, m=8) ##   X[n] = 11^n mod 8




# <headingcell level=4>
# Example #11: $\mathbf{X}^\left({b=12,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 12^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 12
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(12,8\right)} = \{ ,  \cdots \} = \left[ \mathbf{G}^{\left(12,8\right)} \mathbf{H}^{\left(12,8\right)} \mathbf{H}^{\left(12,8\right)} \mathbf{H}^{\left(12,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(12,8\right)} \left(\mathbf{H}^{\left(12,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(12,8\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(12,8\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(12,8\right)}\right| = 1
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(12,8\right)}\right| = 1
# \end{aligned}
# <codecell>
example(b=12, m=8) ##   X[n] = 12^n mod 8




# <headingcell level=4>
# Example #12: $\mathbf{X}^\left({b=13,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 13^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 13
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(13,8\right)} = \{ , 5 \cdots \} = \left[ \mathbf{G}^{\left(13,8\right)} \mathbf{H}^{\left(13,8\right)} \mathbf{H}^{\left(13,8\right)} \mathbf{H}^{\left(13,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(13,8\right)} \left(\mathbf{H}^{\left(13,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(13,8\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(13,8\right)} = \{ 5 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(13,8\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(13,8\right)}\right| = 2
# \end{aligned}
# <codecell>
example(b=13, m=8) ##   X[n] = 13^n mod 8




# <headingcell level=4>
# Example #13: $\mathbf{X}^\left({b=14,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 14^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 14
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(14,8\right)} = \{ 6,  \cdots \} = \left[ \mathbf{G}^{\left(14,8\right)} \mathbf{H}^{\left(14,8\right)} \mathbf{H}^{\left(14,8\right)} \mathbf{H}^{\left(14,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(14,8\right)} \left(\mathbf{H}^{\left(14,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(14,8\right)} = \{ 6 \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(14,8\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(14,8\right)}\right| = 2
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(14,8\right)}\right| = 1
# \end{aligned}
# <codecell>
example(b=14, m=8) ##   X[n] = 14^n mod 8




# <headingcell level=4>
# Example #14: $\mathbf{X}^\left({b=15,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 15^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 15
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(15,8\right)} = \{ , 7 \cdots \} = \left[ \mathbf{G}^{\left(15,8\right)} \mathbf{H}^{\left(15,8\right)} \mathbf{H}^{\left(15,8\right)} \mathbf{H}^{\left(15,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(15,8\right)} \left(\mathbf{H}^{\left(15,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(15,8\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(15,8\right)} = \{ 7 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(15,8\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(15,8\right)}\right| = 2
# \end{aligned}
# <codecell>
example(b=15, m=8) ##   X[n] = 15^n mod 8




# <headingcell level=4>
# Example #15: $\mathbf{X}^\left({b=16,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 16^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 16
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(16,8\right)} = \{ ,  \cdots \} = \left[ \mathbf{G}^{\left(16,8\right)} \mathbf{H}^{\left(16,8\right)} \mathbf{H}^{\left(16,8\right)} \mathbf{H}^{\left(16,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(16,8\right)} \left(\mathbf{H}^{\left(16,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(16,8\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(16,8\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(16,8\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(16,8\right)}\right| = 1
# \end{aligned}
# <codecell>
example(b=16, m=8) ##   X[n] = 16^n mod 8




# <headingcell level=4>
# Example #16: $\mathbf{X}^\left({b=17,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 17^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 17
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(17,8\right)} = \{ ,  \cdots \} = \left[ \mathbf{G}^{\left(17,8\right)} \mathbf{H}^{\left(17,8\right)} \mathbf{H}^{\left(17,8\right)} \mathbf{H}^{\left(17,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(17,8\right)} \left(\mathbf{H}^{\left(17,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(17,8\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(17,8\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(17,8\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(17,8\right)}\right| = 1
# \end{aligned}
# <codecell>
example(b=17, m=8) ##   X[n] = 17^n mod 8




# <headingcell level=4>
# Example #17: $\mathbf{X}^\left({b=18,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 18^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 18
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(18,8\right)} = \{ 2,  \cdots \} = \left[ \mathbf{G}^{\left(18,8\right)} \mathbf{H}^{\left(18,8\right)} \mathbf{H}^{\left(18,8\right)} \mathbf{H}^{\left(18,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(18,8\right)} \left(\mathbf{H}^{\left(18,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(18,8\right)} = \{ 2 \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(18,8\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(18,8\right)}\right| = 2
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(18,8\right)}\right| = 1
# \end{aligned}
# <codecell>
example(b=18, m=8) ##   X[n] = 18^n mod 8




# <headingcell level=4>
# Example #18: $\mathbf{X}^\left({b=19,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 19^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 19
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(19,8\right)} = \{ , 3 \cdots \} = \left[ \mathbf{G}^{\left(19,8\right)} \mathbf{H}^{\left(19,8\right)} \mathbf{H}^{\left(19,8\right)} \mathbf{H}^{\left(19,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(19,8\right)} \left(\mathbf{H}^{\left(19,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(19,8\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(19,8\right)} = \{ 3 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(19,8\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(19,8\right)}\right| = 2
# \end{aligned}
# <codecell>
example(b=19, m=8) ##   X[n] = 19^n mod 8




# <headingcell level=4>
# Example #19: $\mathbf{X}^\left({b=20,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 20^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 20
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(20,8\right)} = \{ ,  \cdots \} = \left[ \mathbf{G}^{\left(20,8\right)} \mathbf{H}^{\left(20,8\right)} \mathbf{H}^{\left(20,8\right)} \mathbf{H}^{\left(20,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(20,8\right)} \left(\mathbf{H}^{\left(20,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(20,8\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(20,8\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(20,8\right)}\right| = 1
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(20,8\right)}\right| = 1
# \end{aligned}
# <codecell>
example(b=20, m=8) ##   X[n] = 20^n mod 8




# <headingcell level=4>
# Example #20: $\mathbf{X}^\left({b=21,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 21^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 21
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(21,8\right)} = \{ , 5 \cdots \} = \left[ \mathbf{G}^{\left(21,8\right)} \mathbf{H}^{\left(21,8\right)} \mathbf{H}^{\left(21,8\right)} \mathbf{H}^{\left(21,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(21,8\right)} \left(\mathbf{H}^{\left(21,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(21,8\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(21,8\right)} = \{ 5 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(21,8\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(21,8\right)}\right| = 2
# \end{aligned}
# <codecell>
example(b=21, m=8) ##   X[n] = 21^n mod 8




# <headingcell level=4>
# Example #21: $\mathbf{X}^\left({b=22,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 22^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 22
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(22,8\right)} = \{ 6,  \cdots \} = \left[ \mathbf{G}^{\left(22,8\right)} \mathbf{H}^{\left(22,8\right)} \mathbf{H}^{\left(22,8\right)} \mathbf{H}^{\left(22,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(22,8\right)} \left(\mathbf{H}^{\left(22,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(22,8\right)} = \{ 6 \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(22,8\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(22,8\right)}\right| = 2
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(22,8\right)}\right| = 1
# \end{aligned}
# <codecell>
example(b=22, m=8) ##   X[n] = 22^n mod 8




# <headingcell level=4>
# Example #22: $\mathbf{X}^\left({b=23,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 23^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 23
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(23,8\right)} = \{ , 7 \cdots \} = \left[ \mathbf{G}^{\left(23,8\right)} \mathbf{H}^{\left(23,8\right)} \mathbf{H}^{\left(23,8\right)} \mathbf{H}^{\left(23,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(23,8\right)} \left(\mathbf{H}^{\left(23,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(23,8\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(23,8\right)} = \{ 7 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(23,8\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(23,8\right)}\right| = 2
# \end{aligned}
# <codecell>
example(b=23, m=8) ##   X[n] = 23^n mod 8




# <headingcell level=4>
# Example #23: $\mathbf{X}^\left({b=24,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 24^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 24
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(24,8\right)} = \{ ,  \cdots \} = \left[ \mathbf{G}^{\left(24,8\right)} \mathbf{H}^{\left(24,8\right)} \mathbf{H}^{\left(24,8\right)} \mathbf{H}^{\left(24,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(24,8\right)} \left(\mathbf{H}^{\left(24,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(24,8\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(24,8\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(24,8\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(24,8\right)}\right| = 1
# \end{aligned}
# <codecell>
example(b=24, m=8) ##   X[n] = 24^n mod 8




# <headingcell level=4>
# Example #24: $\mathbf{X}^\left({b=25,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 25^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 25
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(25,8\right)} = \{ ,  \cdots \} = \left[ \mathbf{G}^{\left(25,8\right)} \mathbf{H}^{\left(25,8\right)} \mathbf{H}^{\left(25,8\right)} \mathbf{H}^{\left(25,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(25,8\right)} \left(\mathbf{H}^{\left(25,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(25,8\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(25,8\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(25,8\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(25,8\right)}\right| = 1
# \end{aligned}
# <codecell>
example(b=25, m=8) ##   X[n] = 25^n mod 8




# <headingcell level=4>
# Example #25: $\mathbf{X}^\left({b=26,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 26^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 26
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(26,8\right)} = \{ 2,  \cdots \} = \left[ \mathbf{G}^{\left(26,8\right)} \mathbf{H}^{\left(26,8\right)} \mathbf{H}^{\left(26,8\right)} \mathbf{H}^{\left(26,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(26,8\right)} \left(\mathbf{H}^{\left(26,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(26,8\right)} = \{ 2 \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(26,8\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(26,8\right)}\right| = 2
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(26,8\right)}\right| = 1
# \end{aligned}
# <codecell>
example(b=26, m=8) ##   X[n] = 26^n mod 8




# <headingcell level=4>
# Example #26: $\mathbf{X}^\left({b=27,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,8\right)} = \{ , 3 \cdots \} = \left[ \mathbf{G}^{\left(27,8\right)} \mathbf{H}^{\left(27,8\right)} \mathbf{H}^{\left(27,8\right)} \mathbf{H}^{\left(27,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,8\right)} \left(\mathbf{H}^{\left(27,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,8\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,8\right)} = \{ 3 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,8\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,8\right)}\right| = 2
# \end{aligned}
# <codecell>
example(b=27, m=8) ##   X[n] = 27^n mod 8




# <headingcell level=4>
# Example #27: $\mathbf{X}^\left({b=28,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 28^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 28
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(28,8\right)} = \{ ,  \cdots \} = \left[ \mathbf{G}^{\left(28,8\right)} \mathbf{H}^{\left(28,8\right)} \mathbf{H}^{\left(28,8\right)} \mathbf{H}^{\left(28,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(28,8\right)} \left(\mathbf{H}^{\left(28,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(28,8\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(28,8\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(28,8\right)}\right| = 1
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(28,8\right)}\right| = 1
# \end{aligned}
# <codecell>
example(b=28, m=8) ##   X[n] = 28^n mod 8




# <headingcell level=4>
# Example #28: $\mathbf{X}^\left({b=29,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 29^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 29
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(29,8\right)} = \{ , 5 \cdots \} = \left[ \mathbf{G}^{\left(29,8\right)} \mathbf{H}^{\left(29,8\right)} \mathbf{H}^{\left(29,8\right)} \mathbf{H}^{\left(29,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(29,8\right)} \left(\mathbf{H}^{\left(29,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(29,8\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(29,8\right)} = \{ 5 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(29,8\right)}\right| = 0
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(29,8\right)}\right| = 2
# \end{aligned}
# <codecell>
example(b=29, m=8) ##   X[n] = 29^n mod 8




# <headingcell level=4>
# Example #29: $\mathbf{X}^\left({b=30,m=8}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 30^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 30
# \end{aligned}
# \begin{aligned}
# m = 8
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(30,8\right)} = \{ 6,  \cdots \} = \left[ \mathbf{G}^{\left(30,8\right)} \mathbf{H}^{\left(30,8\right)} \mathbf{H}^{\left(30,8\right)} \mathbf{H}^{\left(30,8\right)} \cdots \right] = \left[ \mathbf{G}^{\left(30,8\right)} \left(\mathbf{H}^{\left(30,8\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(30,8\right)} = \{ 6 \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(30,8\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(30,8\right)}\right| = 2
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(30,8\right)}\right| = 1
# \end{aligned}
# <codecell>
example(b=30, m=8) ##   X[n] = 30^n mod 8




# <rawcell>
### *EOF*