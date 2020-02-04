#!/bin/sh
blockMesh 1> blockMesh.txt
checkMesh 1> checkMesh.txt
icoFoam 1> icoFoam.txt
postProcess -func 'div(U)' 1> postproc_div.txt

