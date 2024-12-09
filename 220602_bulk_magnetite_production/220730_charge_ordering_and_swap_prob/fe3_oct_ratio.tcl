# Symmetrical 001 layers: 17, 21, 25, 29, 33, 37, 41
  
package require topotools
package require pbctools

#set nlayer 37

topo readlammpsdata magnetite_bulk_3x3x3.data

set log [open "x1.data" w]

# Number of oct layers
set noctl 16

# Topmost fe_oct ions zmin and zmax
set topmost {22.9 23.9}

# Distance between fe oct layers
set oct_oct 2.12

# Initialize zlayer
set zlayer {}

for {set x 0} {$x < $noctl} {incr x} {

        set zmin [expr {[lindex $topmost 0] - $x*$oct_oct}]
        set zmax [expr {[lindex $topmost 1] - $x*$oct_oct}]

        lappend zlayer [list $zmin $zmax]
}

# Count fe ions within each oct layer
for {set x 0} {$x < $noctl} {incr x} {

        set oct_3 [atomselect top "type 2 and x>[lindex $zlayer $x 0] and x<[lindex $zlayer $x 1]"]
        set oct_2 [atomselect top "type 1 and x>[lindex $zlayer $x 0] and x<[lindex $zlayer $x 1]"]

        puts $log "[expr {$x +1}] [$oct_3 num] [$oct_2 num] [expr {[$oct_3 num]+[$oct_2 num]}]"

}

