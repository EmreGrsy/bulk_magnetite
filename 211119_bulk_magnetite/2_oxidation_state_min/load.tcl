global env
set env(LAMMPSREMAPFIELDS) vx=q
topo readlammpsdata magnetite_bulk_3x3.data
animate delete beg 1 end 2 skip 0 0
set mol [mol addfile swap.lammpstrj waitfor all]
# insert "mol addfile command here, if needed"
set nf [molinfo $mol get numframes]
set sel [atomselect $mol all]
for {set i 0} {$i < $nf} {incr i} {
  $sel frame $i
  $sel set charge [$sel get vx]
  $sel set user [$sel get vx]
  $sel set vx 0.0 
}
$sel delete
unset sel
unset env(LAMMPSREMAPFIELDS) 

topo guessatom lammps data
mol bondsrecalc 0
mol reanalyze 0
