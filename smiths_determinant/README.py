### smiths_determinant
### Copyright 2017 Mac Radigan
### SPDX-License-Identifier: GFDL-1.3

# <headingcell level=2>
# Copying
# <rawcell>
# Copyright (C)  2017  Mac Radigan. 
# Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections and with no restrictions on the Front-Cover and back the Front-Cover Texts. A copy of the license is included in the section entitled "GNU Free Documentation License".

# <headingcell level=1>
# Smith's Determinant

# <markdowncell>
# $$\begin{vmatrix} 
# \gcd\left(1,1\right) & \gcd\left(1,2\right) & \gcd\left(1,3\right) & \cdots & \gcd\left(1,N\right) \\
# \gcd\left(2,1\right) & \gcd\left(2,2\right) & \gcd\left(2,3\right) & \cdots & \gcd\left(2,N\right) \\
# \vdots               & \vdots               & \vdots               & \ddots & \vdots               \\
# \gcd\left(N,1\right) & \gcd\left(N,2\right) & \gcd\left(N,3\right) & \cdots & \gcd\left(N,N\right) \notag
# \end{vmatrix}
# =
# \displaystyle{\prod_{n=1}^{N}\varphi\left(n\right)}
# $$
# 
# where
# 
# $$
# \varphi\left(n\right)
# =
# n \displaystyle{\prod_{p_k \mid n}\varphi\left(1 - \frac{1}{p_k}\right)}
# $$
# 
# and $p_k$ are distinct prime numbers with $p_k < n$

# <rawcell>
### *EOF*
