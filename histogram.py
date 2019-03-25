#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filling a ROOT histogram with random values from Python
"""
import numpy as np
from ROOT import TCanvas, TH1D, TF1, kAzure
hits = np.random.normal(5,0.7,5000)

c = TCanvas("name", "title")
h = TH1D("some histogram", "A normal distribution", 80, 0, 10)
for hit in hits:
    h.Fill(hit)
    
fit = h.Fit("gaus", "S")
    
h.GetXaxis().SetTitle("xvalues")
h.GetYaxis().SetTitle("yvalues")
h.SetFillColor(kAzure+4)
h.Draw()
c.Draw()