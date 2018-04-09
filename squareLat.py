#!/usr/local/bin/python

import sys
import numpy as np
from math import sqrt 

bond = float(sys.argv[1])
xmin = 0.0
xmax = 40.0
xL = xmax - xmin
ymin = 0.0
ymax = 40.0
yL = ymax - ymin
xL2 = xL/2.0
yL2 = yL/2.0

#Square lattice coordinate vectors
lat = np.arange(xmin,xmax+bond,bond)
#print lat
X, Y = np.meshgrid(lat,lat)
xlat = X.ravel()
ylat = Y.ravel()
zlat = np.zeros_like(xlat)
natm = len(xlat)

sgm = 3.19
eps = 0.09369
zref = 3.4

fp = open('square-pot-{}.dat'.format(bond), 'w')

def myLoop(start, end, step):
    while start <= end:
        yield start
        start += step
#change min max to self adjust for different bond lengths.
def constN(ind,midbox,minN,maxN):
    while ind[0].size < minN or ind[0].size >maxN:
        if ind[0].size < minN:
            midbox = midbox + 0.05
        if ind[0].size > maxN:
            midbox = midbox - 0.05
        ind = np.where((xlat >= xL2-midbox)\
            &(xlat <= xL2+midbox)\
            &(ylat >= yL2-midbox)\
            &(ylat <= yL2+midbox))
    return ind

midbox = 10.0
ind =np.where((xlat >= xL2-midbox)\
    &(xlat <= xL2+midbox)\
    &(ylat >= yL2-midbox)\
    &(ylat <= yL2+midbox))

#ind = constN(ind,midbox,16,25)

midxmin = min(xlat[ind])
midxmax = max(xlat[ind])
midymin = min(ylat[ind])
midymax = max(ylat[ind])

for xref in myLoop(midxmin, midxmax, 0.1): 
         print xref
         for yref in myLoop(midymin, midymax, 0.1): 
                  phi = 0.0
                  for i in range(0, natm):
                        r = sqrt( (xlat[i]-xref)**2 + (ylat[i]-yref)**2 + (zlat[i]-zref)**2 )
                        sdr = sgm/r
                        phi += 4*eps*(sdr**12-sdr**6)
                  #print("%f %f %f \n" % (xref, yref, phi))
                  fp.write("%f %f %f \n" % (xref, yref, phi))

fp.close()
