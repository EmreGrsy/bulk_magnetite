package require topotools
package require pbctools

topo readlammpsdata b_feoct_assigned.data
topo guessatom lammps data

set fe2_oct [atomselect top "type 5"]
set num_fe2_oct [$fe2_oct num]

proc coord_structure {arg1} {
	
	set coordinated_fe3 [atomselect top "type 4 and pbwithin 3.2 of index $arg1"]
        set coord_num [$coordinated_fe3 num]

        # Leave out fe2 with 0 and 1 coordination, its not possible to define an angle.
        if {($coord_num == 0) || ($coord_num == 1)} { return [list $arg1 0 0] }                        
	
	foreach i1 [$coordinated_fe3 get index] {
                foreach i2 [$coordinated_fe3 get index] {
                        if {($i1 != $i2) && ( $i1>$i2)} {
                                
				set dummy_angle [measure angle [list $i1 $arg1 $i2]]
				set fe3fe3_dist [measure bond [list $i1 $i2]]
                                
                                if {($dummy_angle < 184) && ($dummy_angle > 176) && ($fe3fe3_dist > 5.8)} {
                                        puts "$i1 $arg1 $i2 $fe3fe3_dist $dummy_angle"
                                } elseif {($fe3fe3_dist > 8)} {
					
					set fe3_near [atomselect top "index $i1 $i2 and within 3.2 of index $arg1"]
					set fe3_far [atomselect top "index $i1 $i2 and not within 3.2 of index $arg1"]
					set fe2 [atomselect top "index $arg1"]
					set nfe3_near [$fe3_near num]
					
					# Check if one of the fe3+ is in the same pb as the fe2+, if not, skip.	
					if {($nfe3_near == 1)} {
						
						#puts "---------------"
						#puts "$i1 $arg1 $i2 $fe3fe3_dist $dummy_angle [$fe3_near get index]"
						
						set cfe3_far [lindex [$fe3_far get {x y z}] 0]
						set cfe3_near [lindex [$fe3_near get {x y z}] 0]
						set cfe2 [lindex [$fe2 get {x y z}] 0]

						set x_dist [lindex [vecsub $cfe3_near $cfe3_far] 0]
						set y_dist [lindex [vecsub $cfe3_near $cfe3_far] 1]
						set z_dist [lindex [vecsub $cfe3_near $cfe3_far] 2]

						if {[expr abs($x_dist)] > 6.5 } {
							if {$x_dist > 0} {
								set cfe3_far [vecadd {25.44 0 0} $cfe3_far]
							} elseif {$x_dist < 0 } {
								set cfe3_far [vecadd {-25.44 0 0} $cfe3_far]
							}
							#puts "x) [vecdist $cfe3_near $cfe3_far]"
						} 
						
						if {[expr abs($y_dist)] > 6.5} {
							if {$y_dist > 0} {
                                                                set cfe3_far [vecadd {0 25.44 0} $cfe3_far]
                                                        } elseif {$y_dist < 0 } {
                                                                set cfe3_far [vecadd {0 -25.44 0} $cfe3_far]
                                                        }
                                                        #puts "y) [vecdist $cfe3_near $cfe3_far]"
						}
					
						if {[expr abs($z_dist)] > 6.5 } {
							if {$z_dist > 0} {
                                                                set cfe3_far [vecadd {0 0 25.44} $cfe3_far]
                                                        } elseif {$z_dist < 0 } {
                                                                set cfe3_far [vecadd {0 0 -25.44} $cfe3_far]
                                                        }
                                                        #puts "z) [vecdist $cfe3_near $cfe3_far]"
						}
						
						set fe3fe3_constructed [vecdist $cfe3_near $cfe3_far]

						set fe2fe3_near [vecsub $cfe3_near $cfe2]
						set fe2fe3_far [vecsub $cfe3_far $cfe2]

						set dot_product [vecdot $fe2fe3_near $fe2fe3_far]
						set lfe2fe3_near [veclength $fe2fe3_near]
						set lfe2fe3_far [veclength $fe2fe3_far]
					
						set angle [expr {(acos($dot_product / ($lfe2fe3_near * $lfe2fe3_far))) * (180/3.14159265359)}]

						if {($angle < 184) && ($angle > 176) && ($fe3fe3_constructed > 5.8)}  {
							puts "$i1 $arg1 $i2 $fe3fe3_constructed $angle"
						}
					}
				}
                        }
                }
        }
}

foreach i3 [$fe2_oct get index] {
	coord_structure $i3
}
