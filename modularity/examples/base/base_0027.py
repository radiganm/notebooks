#!/usr/bin/python3
### base_27.py
### Copyright 2017 Mac Radigan
### SPDX-License-Identifier: GFDL-1.3

# <headingcell level=1>
# base 27


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
# Example #1: $\mathbf{X}^\left({b=27,m=2}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 2
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,2\right)} = \{ ,  \cdots \} = \left[ \mathbf{G}^{\left(27,2\right)} \mathbf{H}^{\left(27,2\right)} \mathbf{H}^{\left(27,2\right)} \mathbf{H}^{\left(27,2\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,2\right)} \left(\mathbf{H}^{\left(27,2\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,2\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,2\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,2\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,2\right)}\right| = 1 
# \end{aligned}
# <codecell>
example(b=27, m=2) ##   X[n] = 27^n mod 2




# <headingcell level=4>
# Example #2: $\mathbf{X}^\left({b=27,m=3}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 3
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,3\right)} = \{ ,  \cdots \} = \left[ \mathbf{G}^{\left(27,3\right)} \mathbf{H}^{\left(27,3\right)} \mathbf{H}^{\left(27,3\right)} \mathbf{H}^{\left(27,3\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,3\right)} \left(\mathbf{H}^{\left(27,3\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,3\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,3\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,3\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,3\right)}\right| = 1 
# \end{aligned}
# <codecell>
example(b=27, m=3) ##   X[n] = 27^n mod 3




# <headingcell level=4>
# Example #3: $\mathbf{X}^\left({b=27,m=4}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 4
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,4\right)} = \{ , 3 \cdots \} = \left[ \mathbf{G}^{\left(27,4\right)} \mathbf{H}^{\left(27,4\right)} \mathbf{H}^{\left(27,4\right)} \mathbf{H}^{\left(27,4\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,4\right)} \left(\mathbf{H}^{\left(27,4\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,4\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,4\right)} = \{ 3 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,4\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,4\right)}\right| = 2 
# \end{aligned}
# <codecell>
example(b=27, m=4) ##   X[n] = 27^n mod 4




# <headingcell level=4>
# Example #4: $\mathbf{X}^\left({b=27,m=5}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 5
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,5\right)} = \{ , 2,4,3 \cdots \} = \left[ \mathbf{G}^{\left(27,5\right)} \mathbf{H}^{\left(27,5\right)} \mathbf{H}^{\left(27,5\right)} \mathbf{H}^{\left(27,5\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,5\right)} \left(\mathbf{H}^{\left(27,5\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,5\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,5\right)} = \{ 2,4,3 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,5\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,5\right)}\right| = 4 
# \end{aligned}
# <codecell>
example(b=27, m=5) ##   X[n] = 27^n mod 5




# <headingcell level=4>
# Example #5: $\mathbf{X}^\left({b=27,m=6}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 6
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,6\right)} = \{ ,  \cdots \} = \left[ \mathbf{G}^{\left(27,6\right)} \mathbf{H}^{\left(27,6\right)} \mathbf{H}^{\left(27,6\right)} \mathbf{H}^{\left(27,6\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,6\right)} \left(\mathbf{H}^{\left(27,6\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,6\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,6\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,6\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,6\right)}\right| = 1 
# \end{aligned}
# <codecell>
example(b=27, m=6) ##   X[n] = 27^n mod 6




# <headingcell level=4>
# Example #6: $\mathbf{X}^\left({b=27,m=7}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 7
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,7\right)} = \{ , 6 \cdots \} = \left[ \mathbf{G}^{\left(27,7\right)} \mathbf{H}^{\left(27,7\right)} \mathbf{H}^{\left(27,7\right)} \mathbf{H}^{\left(27,7\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,7\right)} \left(\mathbf{H}^{\left(27,7\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,7\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,7\right)} = \{ 6 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,7\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,7\right)}\right| = 2 
# \end{aligned}
# <codecell>
example(b=27, m=7) ##   X[n] = 27^n mod 7




# <headingcell level=4>
# Example #7: $\mathbf{X}^\left({b=27,m=8}\right)$
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
# Example #8: $\mathbf{X}^\left({b=27,m=9}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 9
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,9\right)} = \{ ,  \cdots \} = \left[ \mathbf{G}^{\left(27,9\right)} \mathbf{H}^{\left(27,9\right)} \mathbf{H}^{\left(27,9\right)} \mathbf{H}^{\left(27,9\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,9\right)} \left(\mathbf{H}^{\left(27,9\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,9\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,9\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,9\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,9\right)}\right| = 1 
# \end{aligned}
# <codecell>
example(b=27, m=9) ##   X[n] = 27^n mod 9




# <headingcell level=4>
# Example #9: $\mathbf{X}^\left({b=27,m=10}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 10
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,10\right)} = \{ , 7,9,3 \cdots \} = \left[ \mathbf{G}^{\left(27,10\right)} \mathbf{H}^{\left(27,10\right)} \mathbf{H}^{\left(27,10\right)} \mathbf{H}^{\left(27,10\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,10\right)} \left(\mathbf{H}^{\left(27,10\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,10\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,10\right)} = \{ 7,9,3 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,10\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,10\right)}\right| = 4 
# \end{aligned}
# <codecell>
example(b=27, m=10) ##   X[n] = 27^n mod 10




# <headingcell level=4>
# Example #10: $\mathbf{X}^\left({b=27,m=11}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 11
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,11\right)} = \{ , 5,3,4,9 \cdots \} = \left[ \mathbf{G}^{\left(27,11\right)} \mathbf{H}^{\left(27,11\right)} \mathbf{H}^{\left(27,11\right)} \mathbf{H}^{\left(27,11\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,11\right)} \left(\mathbf{H}^{\left(27,11\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,11\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,11\right)} = \{ 5,3,4,9 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,11\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,11\right)}\right| = 5 
# \end{aligned}
# <codecell>
example(b=27, m=11) ##   X[n] = 27^n mod 11




# <headingcell level=4>
# Example #11: $\mathbf{X}^\left({b=27,m=12}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 12
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,12\right)} = \{ , 3 \cdots \} = \left[ \mathbf{G}^{\left(27,12\right)} \mathbf{H}^{\left(27,12\right)} \mathbf{H}^{\left(27,12\right)} \mathbf{H}^{\left(27,12\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,12\right)} \left(\mathbf{H}^{\left(27,12\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,12\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,12\right)} = \{ 3 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,12\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,12\right)}\right| = 2 
# \end{aligned}
# <codecell>
example(b=27, m=12) ##   X[n] = 27^n mod 12




# <headingcell level=4>
# Example #12: $\mathbf{X}^\left({b=27,m=13}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 13
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,13\right)} = \{ ,  \cdots \} = \left[ \mathbf{G}^{\left(27,13\right)} \mathbf{H}^{\left(27,13\right)} \mathbf{H}^{\left(27,13\right)} \mathbf{H}^{\left(27,13\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,13\right)} \left(\mathbf{H}^{\left(27,13\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,13\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,13\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,13\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,13\right)}\right| = 1 
# \end{aligned}
# <codecell>
example(b=27, m=13) ##   X[n] = 27^n mod 13




# <headingcell level=4>
# Example #13: $\mathbf{X}^\left({b=27,m=14}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 14
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,14\right)} = \{ , 13, \cdots \} = \left[ \mathbf{G}^{\left(27,14\right)} \mathbf{H}^{\left(27,14\right)} \mathbf{H}^{\left(27,14\right)} \mathbf{H}^{\left(27,14\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,14\right)} \left(\mathbf{H}^{\left(27,14\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,14\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,14\right)} = \{ 13, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,14\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,14\right)}\right| = 2 
# \end{aligned}
# <codecell>
example(b=27, m=14) ##   X[n] = 27^n mod 14




# <headingcell level=4>
# Example #14: $\mathbf{X}^\left({b=27,m=15}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 15
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,15\right)} = \{ , 12, 9, 3, \cdots \} = \left[ \mathbf{G}^{\left(27,15\right)} \mathbf{H}^{\left(27,15\right)} \mathbf{H}^{\left(27,15\right)} \mathbf{H}^{\left(27,15\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,15\right)} \left(\mathbf{H}^{\left(27,15\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,15\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,15\right)} = \{ 12, 9, 3, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,15\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,15\right)}\right| = 4 
# \end{aligned}
# <codecell>
example(b=27, m=15) ##   X[n] = 27^n mod 15




# <headingcell level=4>
# Example #15: $\mathbf{X}^\left({b=27,m=16}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 16
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,16\right)} = \{ , 11, 9, 3, \cdots \} = \left[ \mathbf{G}^{\left(27,16\right)} \mathbf{H}^{\left(27,16\right)} \mathbf{H}^{\left(27,16\right)} \mathbf{H}^{\left(27,16\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,16\right)} \left(\mathbf{H}^{\left(27,16\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,16\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,16\right)} = \{ 11, 9, 3, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,16\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,16\right)}\right| = 4 
# \end{aligned}
# <codecell>
example(b=27, m=16) ##   X[n] = 27^n mod 16




# <headingcell level=4>
# Example #16: $\mathbf{X}^\left({b=27,m=17}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 17
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,17\right)} = \{ , 10,15,14, 4, 6, 9, 5,16, 7, 2, 3,13,11, 8,12, \cdots \} = \left[ \mathbf{G}^{\left(27,17\right)} \mathbf{H}^{\left(27,17\right)} \mathbf{H}^{\left(27,17\right)} \mathbf{H}^{\left(27,17\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,17\right)} \left(\mathbf{H}^{\left(27,17\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,17\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,17\right)} = \{ 10,15,14, 4, 6, 9, 5,16, 7, 2, 3,13,11, 8,12, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,17\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,17\right)}\right| = 16 
# \end{aligned}
# <codecell>
example(b=27, m=17) ##   X[n] = 27^n mod 17




# <headingcell level=4>
# Example #17: $\mathbf{X}^\left({b=27,m=18}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 18
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,18\right)} = \{ ,  \cdots \} = \left[ \mathbf{G}^{\left(27,18\right)} \mathbf{H}^{\left(27,18\right)} \mathbf{H}^{\left(27,18\right)} \mathbf{H}^{\left(27,18\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,18\right)} \left(\mathbf{H}^{\left(27,18\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,18\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,18\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,18\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,18\right)}\right| = 1 
# \end{aligned}
# <codecell>
example(b=27, m=18) ##   X[n] = 27^n mod 18




# <headingcell level=4>
# Example #18: $\mathbf{X}^\left({b=27,m=19}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 19
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,19\right)} = \{ ,  8, 7,18,11,12, \cdots \} = \left[ \mathbf{G}^{\left(27,19\right)} \mathbf{H}^{\left(27,19\right)} \mathbf{H}^{\left(27,19\right)} \mathbf{H}^{\left(27,19\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,19\right)} \left(\mathbf{H}^{\left(27,19\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,19\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,19\right)} = \{  8, 7,18,11,12, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,19\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,19\right)}\right| = 6 
# \end{aligned}
# <codecell>
example(b=27, m=19) ##   X[n] = 27^n mod 19




# <headingcell level=4>
# Example #19: $\mathbf{X}^\left({b=27,m=20}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 20
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,20\right)} = \{ , 7,9,3 \cdots \} = \left[ \mathbf{G}^{\left(27,20\right)} \mathbf{H}^{\left(27,20\right)} \mathbf{H}^{\left(27,20\right)} \mathbf{H}^{\left(27,20\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,20\right)} \left(\mathbf{H}^{\left(27,20\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,20\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,20\right)} = \{ 7,9,3 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,20\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,20\right)}\right| = 4 
# \end{aligned}
# <codecell>
example(b=27, m=20) ##   X[n] = 27^n mod 20




# <headingcell level=4>
# Example #20: $\mathbf{X}^\left({b=27,m=21}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 21
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,21\right)} = \{ ,  6, \cdots \} = \left[ \mathbf{G}^{\left(27,21\right)} \mathbf{H}^{\left(27,21\right)} \mathbf{H}^{\left(27,21\right)} \mathbf{H}^{\left(27,21\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,21\right)} \left(\mathbf{H}^{\left(27,21\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,21\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,21\right)} = \{  6, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,21\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,21\right)}\right| = 2 
# \end{aligned}
# <codecell>
example(b=27, m=21) ##   X[n] = 27^n mod 21




# <headingcell level=4>
# Example #21: $\mathbf{X}^\left({b=27,m=22}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 22
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,22\right)} = \{ ,  5, 3,15, 9, \cdots \} = \left[ \mathbf{G}^{\left(27,22\right)} \mathbf{H}^{\left(27,22\right)} \mathbf{H}^{\left(27,22\right)} \mathbf{H}^{\left(27,22\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,22\right)} \left(\mathbf{H}^{\left(27,22\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,22\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,22\right)} = \{  5, 3,15, 9, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,22\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,22\right)}\right| = 5 
# \end{aligned}
# <codecell>
example(b=27, m=22) ##   X[n] = 27^n mod 22




# <headingcell level=4>
# Example #22: $\mathbf{X}^\left({b=27,m=23}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 23
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,23\right)} = \{ ,  4,16,18, 3,12, 2, 8, 9,13, 6, \cdots \} = \left[ \mathbf{G}^{\left(27,23\right)} \mathbf{H}^{\left(27,23\right)} \mathbf{H}^{\left(27,23\right)} \mathbf{H}^{\left(27,23\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,23\right)} \left(\mathbf{H}^{\left(27,23\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,23\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,23\right)} = \{  4,16,18, 3,12, 2, 8, 9,13, 6, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,23\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,23\right)}\right| = 11 
# \end{aligned}
# <codecell>
example(b=27, m=23) ##   X[n] = 27^n mod 23




# <headingcell level=4>
# Example #23: $\mathbf{X}^\left({b=27,m=24}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 24
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,24\right)} = \{ , 3 \cdots \} = \left[ \mathbf{G}^{\left(27,24\right)} \mathbf{H}^{\left(27,24\right)} \mathbf{H}^{\left(27,24\right)} \mathbf{H}^{\left(27,24\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,24\right)} \left(\mathbf{H}^{\left(27,24\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,24\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,24\right)} = \{ 3 \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,24\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,24\right)}\right| = 2 
# \end{aligned}
# <codecell>
example(b=27, m=24) ##   X[n] = 27^n mod 24




# <headingcell level=4>
# Example #24: $\mathbf{X}^\left({b=27,m=25}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 25
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,25\right)} = \{ ,  2, 4, 8,16, 7,14, 3, 6,12,24,23,21,17, 9,18,11,22,19,13, \cdots \} = \left[ \mathbf{G}^{\left(27,25\right)} \mathbf{H}^{\left(27,25\right)} \mathbf{H}^{\left(27,25\right)} \mathbf{H}^{\left(27,25\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,25\right)} \left(\mathbf{H}^{\left(27,25\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,25\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,25\right)} = \{  2, 4, 8,16, 7,14, 3, 6,12,24,23,21,17, 9,18,11,22,19,13, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,25\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,25\right)}\right| = 20 
# \end{aligned}
# <codecell>
example(b=27, m=25) ##   X[n] = 27^n mod 25




# <headingcell level=4>
# Example #25: $\mathbf{X}^\left({b=27,m=26}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 26
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,26\right)} = \{ ,  \cdots \} = \left[ \mathbf{G}^{\left(27,26\right)} \mathbf{H}^{\left(27,26\right)} \mathbf{H}^{\left(27,26\right)} \mathbf{H}^{\left(27,26\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,26\right)} \left(\mathbf{H}^{\left(27,26\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,26\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,26\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,26\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,26\right)}\right| = 1 
# \end{aligned}
# <codecell>
example(b=27, m=26) ##   X[n] = 27^n mod 26




# <headingcell level=4>
# Example #26: $\mathbf{X}^\left({b=27,m=27}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 27
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,27\right)} = \{ ,  \cdots \} = \left[ \mathbf{G}^{\left(27,27\right)} \mathbf{H}^{\left(27,27\right)} \mathbf{H}^{\left(27,27\right)} \mathbf{H}^{\left(27,27\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,27\right)} \left(\mathbf{H}^{\left(27,27\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,27\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,27\right)} = \{  \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,27\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,27\right)}\right| = 1 
# \end{aligned}
# <codecell>
example(b=27, m=27) ##   X[n] = 27^n mod 27




# <headingcell level=4>
# Example #27: $\mathbf{X}^\left({b=27,m=28}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 28
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,28\right)} = \{ , 27, \cdots \} = \left[ \mathbf{G}^{\left(27,28\right)} \mathbf{H}^{\left(27,28\right)} \mathbf{H}^{\left(27,28\right)} \mathbf{H}^{\left(27,28\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,28\right)} \left(\mathbf{H}^{\left(27,28\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,28\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,28\right)} = \{ 27, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,28\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,28\right)}\right| = 2 
# \end{aligned}
# <codecell>
example(b=27, m=28) ##   X[n] = 27^n mod 28




# <headingcell level=4>
# Example #28: $\mathbf{X}^\left({b=27,m=29}\right)$
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
# Example #29: $\mathbf{X}^\left({b=27,m=30}\right)$
# <markdowncell>
# \begin{aligned}
# \mathbf{X}_n = 27^n \mod m
# \end{aligned}
# with
# \begin{aligned}
# b = 27
# \end{aligned}
# \begin{aligned}
# m = 30
# \end{aligned}
# yeilding
# \begin{aligned}
# \mathbf{X}^{\left(27,30\right)} = \{ , 27, 9, 3, \cdots \} = \left[ \mathbf{G}^{\left(27,30\right)} \mathbf{H}^{\left(27,30\right)} \mathbf{H}^{\left(27,30\right)} \mathbf{H}^{\left(27,30\right)} \cdots \right] = \left[ \mathbf{G}^{\left(27,30\right)} \left(\mathbf{H}^{\left(27,30\right)}\right)^{*} \right]
# \end{aligned}
# where
# \begin{aligned}
# \mathbf{G}^{\left(27,30\right)} = \{  \}
# \end{aligned}
# \begin{aligned}
# \mathbf{H}^{\left(27,30\right)} = \{ 27, 9, 3, \}
# \end{aligned}
# so we have
# \begin{aligned}
# \left|\mathbf{G}^{\left(27,30\right)}\right| = 0 
# \end{aligned}
# \begin{aligned}
# \left|\mathbf{H}^{\left(27,30\right)}\right| = 4 
# \end{aligned}
# <codecell>
example(b=27, m=30) ##   X[n] = 27^n mod 30




# <rawcell>
### *EOF*