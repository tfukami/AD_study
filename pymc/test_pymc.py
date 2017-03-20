#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

N = 40
X = np.random.uniform(10, size=N)
Y = X * 30 + 4 + np.random.normal(0, 16, size=N)
plt.plot(X, Y, "o")


import pymc3 as pm
import theano
theano.config.compute_test_value = 'ignore'
import time
from pymc3.backends.base import merge_traces

multicore=False
saveimage=False

itenum=1000
t0=time.clock()
chainnum=3

with pm.Model() as model:
    alpha = pm.Normal('alpha', mu=0, sd=20)
    beta = pm.Normal('beta', mu=0, sd=20)
    sigma = pm.Uniform('sigma', lower=0)
    y = pm.Normal('y', mu=beta*X + alpha, sd=sigma, observed=Y)
    start = pm.find_MAP()
    step = pm.NUTS()

with model:
    if(multicore):
        trace = pm.sample(itenum, step, start=start,
                njobs=chainnum, random_seed=range(chainnum),
                progress_bar=False)
    else:
        ts = [pm.sample(itenum, step, chain=i, progressbar=False) for i in range(chainnum)]
        trace = merge_traces(ts)
    if(saveimage):
        pm.traceplot(trace).savefig("simple_linear_trace.png")
    print "Rhat="+str(pm.gelman_rubin(trace))

t1 = time.clock()
print "elapsed time=" + str(t1 - t0)
