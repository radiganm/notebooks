### pi.py
###
### Copyright 2017  Mac Radigan. 
### Permission is granted to copy, distribute and/or modify this document 
### under the terms of the GNU Free Documentation License, Version 1.3 
### or any later version published by the Free Software Foundation; 
### with no Invariant Sections, and with no Front-Cover or Back-Cover Texts. 
### A copy of the license is included in the section entitled "GNU Free 
### Documentation License". 


from os.path import join, splitext
from os import walk, system
from collections import OrderedDict
from functools import reduce
from itertools import permutations
import string
import random
import pdb
from collections import defaultdict
import numpy as np
from scipy import signal

INVARIANT_PREFACE     = ''
INVARIANT_PUBLICATION = 'f379e9385edeef35627a231754162bbee863be27'

META_TITLE         = 'modularity'

META_AUTHOR        = 'Copyright 2017 Mac Radigan'
META_LICENSE       = 'SPDX-License-Identifier: GFDL-1.3'
META_LICENSE_SPDX  = 'GFDL-1.3'
META_LICENSE_SHORT = 'GNU Free Documentation License v1.3'
META_LICENSE_TEXT  = """# Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections and with no restrictions on the Front-Cover and back the Front-Cover Texts. A copy of the license is included in the section entitled "GNU Free Documentation License".  """

N  = 30
bs = range(2, 31)
ms = range(2, 31)

def sequence(b,m):
  """Retruns and array with the sequence X_n = b^n mod m for n = 1, 2, ... N"""
  N  = 30
  ns = range(1, N)
  f  = lambda n: b**n % m
  xs = map(f, ns)
  return np.array(list(xs))

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
  gs = xs[:k1]
  hs = xs[k1:k2]
  return gs,hs

for b in bs:
  for m in ms:
    X   = sequence(b, m)
    G,H = decompose(X)
    Gs  = np.array2string(G, separator=',')[1:-3]
    Hs  = np.array2string(H, separator=',')[1:-3]
    G_N = len(G)
    H_N = len(H)
    apply_templates()

### *EOF*
