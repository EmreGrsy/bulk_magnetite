# change background color to green for better post-processing
color Display Background white
display Backgroundgradient off
axes location off

package require topotools
package require pbctools

topo readlammpsdata magnetite_3x3x3_swp_constrained.data

topo guessatom lammps data

color add item Name C gray
color Name C gray

pbc box
display resetview

rotate x by -90
rotate y by -45
rotate x by 6

# Delete default representation
mol delrep 0 top

# Cartoon display
material add Cartoon
material change ambient Cartoon 0.00
material change diffuse Cartoon 0.90
material change specular Cartoon 0.00
material change shininess Cartoon 0.00
material change mirror Cartoon 0.00
material change opacity Cartoon 1.00
material change outline Cartoon 4.00
material change outlinewidth Cartoon 0.35


# Formate and surface hydroxyl
#mol representation vdw 0.6 1000
#mol color Charge
#mol material Cartoon
#mol selection {type 4 5} 
#mol addrep top

mol representation vdw 0.6 1000
mol color Name
mol material Cartoon
mol selection {type 3}
mol addrep top

mol representation vdw 0.6 1000
mol color Charge
mol material Cartoon
mol selection {type 2}
mol addrep top



# Surface hydrogen
#mol representation vdw 0.5 1000
#mol color Name
#mol material Cartoon
#mol selection {index 1224}
#mol addrep top

#set sys [atomselect top all]
#$sys moveby {0 0 -18}

# Magnetite slab
#mol representation vdw 0.5 1000
#mol color Charge
#mol material AOChalky
#mol selection {type 6 7 8 9 and z>10}
#mol addrep top

# Magnetite nanosphere
#mol representation Surf 11.2 0.000
#mol color Name
#mol material Transparent
#mol selection {type 1 2 3 4 and x > 0 and x < 50 and y>0 and y <50 }
#mol addrep top

# Display settings
display depthcue off
display cuemode Exp2
display cuestart 0.50
display cueend 10.00
display cuedensity 0.32
display eyesep 0.07
display focalLength 2.00
display height 4.0
display distance -2.00
display culling off
display fps off
display stereoswap off
display cachemode Off
display projection Orthographic
display shadows on
display ambientocclusion on
display aoambient 0.80
display aodirect 0.40

display update

# Rendeing options

# --asamples 12 -res 7680 4800  
render Tachyon not_oct "/usr/local/lib/vmd/tachyon_LINUXAMD64" -fullshade -trans_vmd -aasamples 12 %s -format TARGA -res 7680 4800 -o %s.tga




## Allign the sufrace to X-Y axis so it would be easier to define cut plane
#set transfer_matrix [transaxis z 135]
#$formate_full move $transfer_matrix
#
#display resetview
#
#rotate x by 270
#
## Delete default representation
#mol delrep 0 top
#
#set formate_only [atomselect top "all and y>-6 and y<6 and z>19"]
#set magnetite [atomselect top "all and y>-6 and y<6 and z<19"]
#
## Define representations 
#mol representation DynamicBonds 2.4 0.08 500
#mol color Type
#mol selection {all and y>-6 and y<6 and z<19}
#mol addrep top
#
#mol representation DynamicBonds 2.0 0.08 500
#mol color Type
#mol selection {all and y>-6 and y<6 and z>19}
#mol addrep top
#
#mol representation vdw 0.25 500
#mol color Type
#mol selection {all and y>-6 and y<6}
#mol addrep top
#
#display update
#
#display height 4
#
#[atomselect top all] moveby {0 0 -7}
#
##rotate y by 1
##rotate x by 2
#
## Rendeing options
#render Tachyon 001-dbt-fa-tet-half_green_e6 "/usr/local/lib/vmd/tachyon_LINUXAMD64" -fullshade -trans_vmd -aasamples 12 %s -format TARGA -res 7680 4800 -o %s.tga
#
