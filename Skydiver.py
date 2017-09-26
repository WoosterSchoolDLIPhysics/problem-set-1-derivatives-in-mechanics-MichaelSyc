# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:19:16 2017

@author: Michael
"""

from pylab import * 

t0 = 0.0 
tf = 30.0
dt = 0.5

t = arange(t0 , tf , dt)
v = zeros(len(t))
v0 = 0
v[0] = v0

b = 0.1
g = 10
m = 1.0 

for i in arange(1 , len(t)):
    dv = (-b/m*v[i - 1]-g)*dt
    v[i] = v[i - 1] + dv    
    
figure(1)
clf()
plot(t , v , 'b-o')
vt = -m*g/b
plot(t , vt*(1-exp(-b*t/m)),'k')
plot(t , 0*t+vt , 'k--')
plot(t , -g*t , 'c--')
ylim(-120,0)
