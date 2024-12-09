# This script computes ....
# there is a lot of room for improvment such as calculating the coord_num outside the function but mehhhhhhhhh

topo readlammpsdata oxygenTerminated_initial_structure_before_charge_redistribution.data
topo guessatom lammps data

# define the group of the atoms that you want to see their coordination
# in our current work "type 2 3" are the fe atoms we are intersted

set fe_group [atomselect top "type 2 3"]
set num_fe_group [$fe_group num]
puts "number is: $num_fe_group"

# coord_strucutre {arg1} function takes atom index and returns; atom index, coordination number and geometry
# geom_type 1 is octahedral coordination, geom_type 2 is tetrahedral coordination

proc coord_structure {arg1} {

        set coordinated_O [atomselect top "type 1 and within 3 of index $arg1"]
        set coord_num [$coordinated_O num]
        if {($coord_num == 0) || ($coord_num == 1)} { return [list $arg1 0 0] }
        set total_angle 0
        set count 0
        set geom_type 0
        foreach i1 [$coordinated_O get index] {
                foreach i2 [$coordinated_O get index] {
                        if {$i1 != $i2} {
                                set dummy_angle [measure angle [list $i1 $arg1 $i2]]
                                if {($dummy_angle < 190) && ($dummy_angle > 170)} {
                                } else {
                                        set total_angle [expr $total_angle + $dummy_angle]
                                        incr count
                                }
                        }
                }
        }
        set average_angle [expr $total_angle / $count]
        if {($average_angle > 85) && ($average_angle < 95)} {
                set geom_type 1
        } elseif {($average_angle > 100) && ($average_angle < 115)} {
                set geom_type 2
        }
        return [list $arg1 $geom_type $coord_num]
}

# set the number of different coordinated atoms to 0 

set feTet_1c 0
set feTet_2c 0
set feTet_3c 0
set feTet_4c 0
set feTet_5c 0
set feTet_6c 0
set feTet_7c 0

set feOct_1c 0
set feOct_2c 0
set feOct_3c 0
set feOct_4c 0
set feOct_5c 0
set feOct_6c 0
set feOct_7c 0

# loop over the atoms in the system and assign their coordination 

foreach i3 [$fe_group get index] {

	if {[lindex [coord_structure $i3] 1] == 2} {
		if {[lindex [coord_structure $i3] 2] == 1} {
			incr feTet_1c
		} elseif {[lindex [coord_structure $i3] 2] == 2} {
			incr feTet_2c
		} elseif {[lindex [coord_structure $i3] 2] == 3} {
                        incr feTet_3c
		} elseif {[lindex [coord_structure $i3] 2] == 4} {
                        incr feTet_4c
		} elseif {[lindex [coord_structure $i3] 2] == 5} {
                        incr feTet_5c
                } elseif {[lindex [coord_structure $i3] 2] == 6} {
                        incr feTet_6c
                } elseif {[lindex [coord_structure $i3] 2] == 7} {
                        incr feTet_7c 
		}	
	} elseif {[lindex [coord_structure $i3] 1] == 1} {
		if {[lindex [coord_structure $i3] 2] == 1} {
                        incr feOct_1c 
                } elseif {[lindex [coord_structure $i3] 2] == 2} {
                        incr feOct_2c  
                } elseif {[lindex [coord_structure $i3] 2] == 3} {
                        incr feOct_3c 
                } elseif {[lindex [coord_structure $i3] 2] == 4} {
                        incr feOct_4c 
                } elseif {[lindex [coord_structure $i3] 2] == 5} {
                        incr feOct_5c 
                } elseif {[lindex [coord_structure $i3] 2] == 6} {
                        incr feOct_6c 
                } elseif {[lindex [coord_structure $i3] 2] == 7} {
                        incr feOct_7c }
	}
}

puts "----------------------"
puts "----------------------"
puts "feTet_1c: $feTet_1c"
puts "feTet_2c: $feTet_2c"
puts "feTet_3c: $feTet_3c"
puts "feTet_4c: $feTet_4c"
puts "feTet_5c: $feTet_5c"
puts "feTet_6c: $feTet_6c"
puts "feTet_7c: $feTet_7c"
puts "----------------------"
puts "----------------------"
puts "feOct_1c: $feOct_1c"
puts "feOct_2c: $feOct_2c"
puts "feOCt_3c: $feOct_3c"
puts "feOCt_4c: $feOct_4c"
puts "feOct_5c: $feOct_5c"
puts "feOct_6c: $feOct_6c"
puts "feOct_7c: $feOct_7c"
puts "----------------------"
puts "----------------------"

