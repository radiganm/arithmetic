## pi.py
## Mac Radigan

##  Copyright 2017  Mac Radigan. 
##  Permission is granted to copy, distribute and/or modify this document 
##  under the terms of the GNU Free Documentation License, Version 1.3 
##  or any later version published by the Free Software Foundation; 
##  with the Invariant Sections being Preface, with the Front-Cover Texts 
##  being "for Ashton, Lyla, Neomi, Ruth, and Malakai", and no Back-Cover Texts. 
##  A copy of the license is included in the section entitled "GNU Free 
##  Documentation License". 


from os.path import join, splitext
from os import walk, system
from collections import OrderedDict
from functools import reduce
from itertools import permutations
import string
import random
import pdb

COVER_FRONT = 'for Ashton, Lyla, Neomi, Ruth, and Malakai'

def permute_list(xs):
  ys = [set(permutations(x)) for x in xs]
  return [x for y in ys for x in y]

def factorize_list(n):
  return [(int(i), int(n / i)) for i in range(1, int(n**0.5)+1) if n % i == 0]

def factorize(n):    
  return set(reduce(list.__add__, ([int(i), int(n/i)] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

N = 24
ns = range(1,N+1)

colors = ['black', 'red', 'blue', 'green', 'red', 'blue', 'green', 'red', 'blue', 'green', 'red', 'blue', 'green', 'red', 'blue', 'green', 'red', 'blue', 'green'];

dat = OrderedDict([])

for n in ns:
  dat[n] = {}
  factor_list = permute_list(factorize_list(n))
 #pdb.set_trace()
  for k, factors in enumerate(factor_list):
    dat[n][k] = {}
    dat[n][k]['factors'] = factors
    dat[n][k]['factor_id'] = ','.join(map(lambda x: "%d" % x,factors))
    dat[n][k]['factor_expression'] = "$%d = %s$" % (n, ' \\times '.join(map(lambda x: "%d" % x,factors)))
    dat[n][k]['factors_string'] = '-'.join(map(lambda x: "%d" % x,factors))
    dat[n][k]['name'] = "%s_%s" % (n, dat[n][k]['factors_string'])

#for n in ns:
#  dat[n] = {}
#  factor_list = list(factorize(n))
#  k = 0
#  factors = factor_list
#  dat[n][k] = {}
#  dat[n][k]['factors'] = factors
#  dat[n][k]['factor_id'] = ','.join(map(lambda x: "%d" % x,factors))
#  dat[n][k]['factor_expression'] = "$%d = %s$" % (n, ' \\times '.join(map(lambda x: "%d" % x,factors)))
#  dat[n][k]['factors_string'] = '-'.join(map(lambda x: "%d" % x,factors))
#  dat[n][k]['name'] = "%s_%s" % (n, dat[n][k]['factors_string'])

for n_k in dat.items():
  n = n_k[0]
  for k, fmap in enumerate(dat[n].items()):
    factors = fmap[1]['factors']
    factors_string = fmap[1]['factors_string']
    name = fmap[1]['name']
    apply_templates()

## *EOF*
