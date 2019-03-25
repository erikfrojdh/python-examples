#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fit all 500k pixels in an EIGER module and plot some sample ones
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.ion()
sns.set()
sns.set_context('talk')
sns.set_style('white')

from sls_detector_tools.mpfit import fit
from sls_detector_tools.calibration import find_initial_parameters
from sls_detector_tools.function import scurve
from sls_detector_tools.plot import imshow
import sls_detector_tools.root_helper as r

with np.load('/home/l_frojdh/data/T72-cSAXS_vcmp_FeXRF_0.npz') as f:
    data = f['data']
    x = f['x']
    

y = data.sum(axis = 0).sum(axis = 0)
y = y/(data.sum(axis = 2)>0).sum()
par = find_initial_parameters(x,y)
names = ['p$_0$', 'p$_1$', '$\mu$', r'$\sigma$', 'A', 'C']
labels = [f'{name}: {p:.2f}\n' for (name, p) in zip(names, par)]
labels = ''.join(labels)

fig, ax = plt.subplots(1,1, figsize = (12,7))
ax.plot(x, y, 'o', label = 'Data')
ax.plot(x, scurve(x, *par), label = labels)
ax.grid(True)
sns.despine()
ax.legend()
plt.savefig('/home/l_frojdh/reveal.js/deck/python/average.png')
par[1] = 0

result = fit(data, x, 12, par)


#pixels = [(100,120), (500,753), (300,25)]
#fig, ax = plt.subplots(1,1, figsize = (12,7))
#colors = sns.color_palette()
#for p, c in zip(pixels, colors):
#    ax.plot(x, data[p], 'o', alpha = 0.5)
#    ax.plot(x, scurve(x, *result[p]),label = str(p), color = c)
#ax.legend()
#ax.set_xlim(500,2000)
#ax.set_xlabel('vthreshold')
#ax.set_ylabel('counts')
#sns.despine()
#ax.grid(True)
#fig.tight_layout()
#
#
#old = np.load('result.npy')
#print((result['p0']-old['p0']).sum())