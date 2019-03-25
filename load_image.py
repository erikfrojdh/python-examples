#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Short example for group meeting loading Jungfrau image 
"""

import os
import numpy as np
import matplotlib.pyplot as plt
plt.ion()

os.chdir('/home/l_frojdh/data')
header_size = 48
bitmask = np.array([0x3fff], dtype = np.uint16)
nrows = 512
ncols = 1024

with open('data_d0_f000000000000_0.raw', 'rb') as f:
    header = f.read(header_size)
    image = np.fromfile(f, dtype = np.uint16, 
                           count = nrows*ncols ).reshape((nrows,ncols))
    gain = np.right_shift(image, 14)
    image = np.bitwise_and(image, bitmask)
    
fig, ax = plt.subplots(1,2, figsize = (15,5))
ax[0].imshow(image, origin = 'lower')
ax[0].set_title("ADC value")
ax[1].imshow(gain, origin = 'lower')    
ax[1].set_title("Gain")
fig.tight_layout()
plt.savefig('/home/l_frojdh/reveal.js/deck/python/image.png')

