import numpy as np
import sys
import glob

shape = str(sys.argv[1])
fout = open("{}-depth.dat".format(shape),"w") 
flist = sorted(glob.glob("{}-pot-*.dat".format(shape)))
for fl in flist:
    fs = fl.split("-")
    bond = fs[2].rstrip(".dat")
    pot = np.loadtxt(fl)

    xC = np.where((pot[:,0] >= 10) & (pot[:,0] <= 30))
    yC = np.where((pot[:,1] >= 10) & (pot[:,1] <= 30))

    #print bond,xC,yC
    potC = pot[np.intersect1d(xC,yC),2]
    print bond,potC
    potCmin = np.amin(potC)
    potCmax = np.amax(potC)
    depth = potCmax-potCmin
    fout.write("{0}\t{1}\t{2}\t{3}\n".format(bond,potCmin,potCmax,depth))
fout.close()
