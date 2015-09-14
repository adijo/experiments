"""
Modelling the probability of getting optimal number of 
visits by police officers in a tram.
1. k are the number of stops travelled by the average traveler.
2. p is the probability of an officer entering station at stop i in
   range [1..k]
3. n are the number of passengers travelling without tickets in the day.
4. Another parameter, say q, that gives us the percentage of people
   that we want to catch. Example: If q = 0.5, that would mean that we 
   expect that out of n people travelling without tickets, n/2 SHOULD be caught
   in expectation.
5. The problem would then boil down to estimate the value of the parameter p.
"""
from math import log, e

import pandas as pd
from ggplot import *
import random


def capture(q, k = 5):
    a = log(1 - float(q))
    b = a / float(k)
    c = pow(e, b)
    return 1 - c


qs = [random.random() for x in xrange(100000)]
qs.sort()
ans = map(lambda x : capture(x), qs)
data = pd.DataFrame({'Proportion' : qs, 'Probability' : ans})
plt = ggplot(aes(x = 'Proportion', y = 'Probability'), data = data) + \
geom_line()
plt.__repr__()