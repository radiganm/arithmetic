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
  return set(reduce(list.__add__, ([int(i), int(n//i)] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

N = 5
ns = range(1,N+1)

colors = ['black', 'red', 'blue', 'green'];

dat = OrderedDict([])

for n in ns:
  dat[n] = {}
  dat[n]['factor_list'] = factorize_list(n)
  dat[n]['factorization'] = factorize(n)
  for factors in dat[n]['factor_list']:
    dat[n]['factor_id'] = ','.join(map(lambda x: "%d" % x,factors))
    dat[n]['factor_expression'] = "$%d = %s$" % (n, ' \\times '.join(map(lambda x: "%d" % x,factors)))
    dat[n]['factor_string'] = '-'.join(map(lambda x: "%d" % x,factors))
    dat[n]['name'] = "%s_%s" % (n, dat[n]['factor_string'])

for k_n in dat.items():
  n = k_n[0]
  factor_list = dat[n]['factor_list']
  for factors in factor_list:
    factors_string = '-'.join(map(lambda x: "%d" % x,factors))
    name = "%s_%s" % (n, dat[n]['factor_string'])
    apply_templates()

## *EOF*
