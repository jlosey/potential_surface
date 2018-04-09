set terminal pngcairo font "Times,12"
set output "bond-welldepth2.png"

set style line 1 lc 1 pt 5 ps 0.5
set style line 2 lc rgb "#3CB371" pt 7 ps 0.5
set style line 3 lc 3 pt 9 ps 0.5

set xlabel "Bond Length, nm"
set ylabel "Well Depth"
set key top left
plot 'hex-depth.dat' u 1:4 w lp ls 1 t 'Graphene', 'tri-depth.dat' u ($1/10):4 w lp ls 2 t 'Triangular Lattice', 'square-depth.dat' u ($1/10):4 w lp ls 3 t 'Square Lattice'

