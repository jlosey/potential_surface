#!/usr/local/bin/python

import sys
import numpy as np
from math import sqrt 

fp1 = str(sys.argv[1])
print fp1
bond = str(fp1.rstrip(".dat").split("-")[1])
#fp2 = str(sys.argv[2])
coord = np.loadtxt(fp1)
xlat = coord[:,0]
ylat = coord[:,1]
zlat = coord[:,2]

natm = len(xlat)
xmin = xlat.min()
xmax = xlat.max()
xL = xmax - xmin
ymin = ylat.min()
ymax = ylat.max()
yL = ymax - ymin

sgm = 3.19
eps = 0.09369
zref = 3.4

fp = open('hex-pot-{}.dat'.format(bond), 'w')

def myLoop(start, end, step):
    while start <= end:
        yield start
        start += step

for xref in myLoop(xmin + xL/4.0, xmax - xL/4.0, 0.1): 
         print xref
         for yref in myLoop(ymin + yL/4.0, ymax - yL/4.0, 0.1): 
                  phi = 0.0
                  for i in range(0, natm):
                        r = sqrt( (xlat[i]-xref)**2 + (ylat[i]-yref)**2 + (zlat[i]-zref)**2 )
                        sdr = sgm/r
                        phi += 4*eps*(sdr**12-sdr**6)
                  #print("%f %f %f \n" % (xref, yref, phi))
                  fp.write("%f %f %f \n" % (xref, yref, phi))

fp.close()
