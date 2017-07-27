## pi.py
## Copyright 2016 Mac Radigan
## All Rights Reserved

from os.path import join, splitext
from os import walk, system
from collections import OrderedDict
from functools import reduce
import string
import random

def factorize_list(val):
  return [(int(i), int(val / i)) for i in range(1, int(val**0.5)+1) if val % i == 0]

def factorize(n):    
  return set(reduce(list.__add__, ([int(i), int(n/i)] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

N = 24
ns = range(1,N+1)

colors = ['black', 'red', 'blue', 'green', 'red', 'blue', 'green', 'red', 'blue', 'green', 'red', 'blue', 'green', 'red', 'blue', 'green', 'red', 'blue', 'green'];

dat = OrderedDict([])

for n in ns:
  dat[n] = {}
  factor_list = factorize_list(n)
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
