# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 11:18:41 2017

@author: Michael
"""

from pylab import * 

dt = 0.01

t = arange(0 , 4 , dt)

ft = t**4 - 4*t**3 + 2*t**2 + 3*t + 6

t = arange(0 , 4 , dt)

fx = 4*t**3 - 12*t**2 + 4*t + 3

t = arange(0 , 4 , dt)

fv = 12*t**2 - 24*t + 4

t = arange(0 , 4 , dt)

fa = 24*t - 24

figure(1)
clf()   
subplot(411)
plot(t,ft)
subplot(412)
plot(t,fx)
subplot(413)
plot(t,fv)
subplot(414)
plot(t,fa)




