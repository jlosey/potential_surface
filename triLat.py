#!/usr/local/bin/python

import sys
import numpy as np
from math import sqrt 
#from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca()
#ax = fig.gca(projection='3d')

bond = float(sys.argv[1])
cmin = 0.0
cmax = 40.0

#Triangular lattice coordinates
x1 = np.arange(cmin,cmax+bond,bond)
x2 = np.add(x1,bond/2.0)
nx = len(x1)
y0 = np.zeros_like(x1)
yi = np.array([])
xi = np.array([])
height = (sqrt(3)/2)*bond
n = 0
while y0[0] <= cmax:
    if n%2 == 0:
        xi = np.hstack([xi,x1])
    else:
        xi = np.hstack([xi,x2])
    n = n + 1
    yi = np.hstack([yi,y0])
    y0 = np.add(y0,height)
xlat = xi
ylat = yi
zlat = np.zeros_like(xlat)
print x1.size,x2.size,y0.size
ax.plot(xlat,ylat,".")
#ax.set_xlim([18,22])
#ax.set_ylim([18,22])
plt.show()

natm = len(xlat)
xmin = np.amin(xlat)
xmax = np.amax(xlat)
xL = xmax - xmin
ymin = np.amin(ylat)
ymax = np.amax(ylat)
yL = ymax - ymin

sgm = 3.19
eps = 0.09369
zref = 3.4

fp = open('tri-pot-{}.dat'.format(bond), 'w')

def myLoop(start, end, step):
    while start <= end:
        yield start
        start += step

for xref in myLoop(xmin + xL/4.0, xmax - xL/4.0, 0.1): 
    #print xref
         for yref in myLoop(ymin + yL/4.0, ymax - yL/4.0, 0.1): 
                  phi = 0.0
                  for i in range(0, natm):
                        r = sqrt( (xlat[i]-xref)**2 + (ylat[i]-yref)**2 + (zlat[i]-zref)**2 ) 
                        #if r < xL/2.0:
                        sdr = sgm/r
                        phi += 4*eps*(sdr**12-sdr**6)
                  #print("%f %f %f \n" % (xref, yref, phi))
                  fp.write("%f %f %f \n" % (xref, yref, phi))

fp.close()
