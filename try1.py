#!/usr/local/bin/python
import numpy as np
from math import sqrt 

natm = 9
sgm = 1.0
eps = 1.0

xlat = 4*np.array([0,1,2,0,1,2,0,1,2])
ylat = 4*np.array([0,0,0,1,1,1,2,2,2])
zlat = np.array([0,0,0,0,0,0,0,0,0])

xref = 0.0
yref = 0.0
zref = 4.0

fp = open('potential.dat', 'w')

def myLoop(start, end, step):
    while start <= end:
        yield start
        start += step

for xref in myLoop(0, 8, 0.02): 
         for yref in myLoop(0, 8, 0.02): 
                  phi = 0.0
                  for i in range(0, natm):
                        r = sqrt( (xlat[i]-xref)**2 + (ylat[i]-yref)**2 + (zlat[i]-zref)**2 )     
                        sdr = sgm/r
                        phi += 4*eps*(sdr**12-sdr**6)
                  #print("%f %f %f \n" % (xref, yref, phi))
                  fp.write("%f %f %f \n" % (xref, yref, phi))

fp.close()

