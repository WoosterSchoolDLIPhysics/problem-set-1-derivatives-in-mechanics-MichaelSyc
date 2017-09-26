# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 11:32:07 2017

@author: Michael
"""

from pylab import *

t = linspace(0,1,100)

x = 3*sin(2*pi*t)
y = 2*cos(2*pi*t)
vx = 6 *pi* cos(2*pi*t)/5
vy = -4*pi*sin(2*pi*t)/5
ax = -12*pi*pi*sin(2*pi*t)/5
ay = -8*pi*pi*cos(2*pi*t)/5

figure(1)

for it in arange(len(t)):
    clf()
    #subplot(131)
    plot(x,y)
    plot([0,x[it]],[0,y[it]],'b-o')
    axis('equal'); xlabel(r'$x$'); ylabel(r'$y$')
    text(1.2*x[it],1.2*y[it],r'$\vec{x}$',color='blue',size=15)

   
    plot(vx,vy)
    plot([0,vx[it]],[0,vy[it]],'r-o')
    axis('equal'); xlabel(r'$v$'); ylabel(r'$y$')
    text(1.2*vx[it],1.2*vy[it],r'$\vec{v}$',color='red',size=15)
    
    plot(ax,ay)
    plot([0,ax[it]],[0,ay[it]],'g-o')
    axis('equal'); xlabel(r'$a$'); ylabel(r'$y$')
    text(1.2*ax[it],1.2*ay[it],r'$\vec{a}$',color='green',size=15)
    
    grid()
    pause(.001)
    
    