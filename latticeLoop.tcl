package require nanotube
package require psfgen
package require solvate
package require topotools
package require exectool
foreach bond [list 0.02 0.04 0.06 0.08] {
graphene -lx 4 -ly 4 -type zigzag -b 0 -cc $bond
set sel [atomselect top all]
$sel writepdb lattice.pdb

exec awk {BEGIN{FIELDWIDTHS="26 12 8 8"} NR>1{print $2,$3,$4;}} lattice.pdb > lattice-$bond.dat

mol delete all
}
exit
