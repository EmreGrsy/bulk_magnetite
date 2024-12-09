#!/bin/bash
# This script is for rearranging parameters after using VMD::TopoTools::.
# This script assumes that the input file includes; atoms, bonds, angles, dihedrals and impropers. If this is not the case, delete the unnecessary entries.


# Input file.

infile="$PWD/a_feoct_assigned.data"


# Structural information.

sed '/ Atoms # full/Q' $infile>.tmp_initial


# Parse the number of atoms and bonded terms, and increment them by 1.
# Number of atoms and bonded terms are incremented to include "\n" after each section such as "Atoms # full". 
# Number of types are incremented to include "#", this is required for coefficient array indexing. 

atom_number=$(($(grep " atoms" $infile | awk '{print $1}')+1)) 
atom_type_number=$(($(grep " atom types" $infile | awk '{print $1}')+1))

# Initialize coefficient arrays (coefficient arrays start with 0).

pair_coeffs=($(sed -n "/# Pair Coeffs/,+${atom_type_number}p" $infile | sed -e '1,2d' | awk '{print $3}'))


# Change TopoTools assigned parameters back to original parameters by using Coefficient array mapping.

grep -A $atom_number " Atoms # full" $infile | sed -e '1,2d' | 
awk -v arr1="${pair_coeffs[*]}" '{split(arr1,arr2);for(a in arr2){if($3==a){$3=arr2[a]; print}}}' | awk '!a[$1]++'>.tmp_atom

# Combine temp files.

cat .tmp_initial>>.tmp_data

echo " Atoms # full">>.tmp_data
echo -en '\n'>>.tmp_data
cat .tmp_atom>>.tmp_data
echo -en '\n'>>.tmp_data

# Write the final structure.

cat .tmp_data>b_feoct_assigned.data


# Remove temp file.

rm .tmp*
