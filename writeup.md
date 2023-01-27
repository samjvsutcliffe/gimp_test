**Describe the bug**
A clear and concise description of the bug.
# GIMP broken?
The 2d, and 3d implementations of GIMP elements/particles have two issues with their implementation.
When using pycbg/GMSH to output nodes on the improve/mpmxdem branch gimp cells are generated with a different node order to those expected by the GIMP elements.
The 2D elements have incorrect shearing behaviour due to this, and the 3D elements have incorrect shear in one dimension but not the other.
This can be easily seen with a 1D consolidation problem.

The second issue is that (at least for the pycbg generated meshes) the GIMP elements do not actually cross the cells, they are only smoother inside of the cell.
If you were to generate a mesh that has 16 nodes per cell with the correct behaviour, you end up with boundary cells not having enough nodes for the GIMP element.

To fix this the GIMP elements must be able to have less than 16 nodes in their "stencil" to account for the boundaries.


# Reproduce
To reproduce:

Compile the latest MPM build on master, and add the build to your PATH

Grab the test 1D consolidation problems, available at:
https://github.com/samjvsutcliffe/gimp_test

You can run all of the tests with 
```
./run_tests
```

Afterwards you can run the evaluation.py with python3, pandas, matplotlib, and pytables.
The evaluation will draw final shear stress plots, along with vertical stresses.
```
pip3 install pandas matplotlib tables
python3 evaluation.py
```
You can also look at the shear stresses in the VTKs generated, which will be large ~1000MPa RMS.

To generate these meshes you will need the latest branch of pycbg for 2d mesh generation and 2d GIMP.

This can be done by using a local install of the mirrored version.

You need to install this local version using pip install -e
```
git clone https://github.com/samjvsutcliffe/pycbg.git
cd pycbg
git switch improve/mpmxdem
pip3 install -e ./
```

# Expected behavior
For a 1d consolidation we expect no shear stresses.
This should be true for MPM/GIMP.
We should also expect better continuity over cell boundaries for the GIMP case.

What we find is spurious shear stress for GIMP in the order of 1000MPa RMS, and cell crossing issues due to the lack of cross cell-continuity.

# Screenshots

MPM 1D consolidation:

![image](https://user-images.githubusercontent.com/117826225/215151109-8e441e97-3b01-4f49-b19e-53da67071664.png)

GIMP 1D consolidation:

![image](https://user-images.githubusercontent.com/117826225/215151055-2a6afebe-a633-409f-9057-bf1cc48c05cb.png)

Vertical stress distributions for both:

![image](https://user-images.githubusercontent.com/117826225/215158604-5477ad27-7925-4ace-915e-b8316116cf5d.png)



# Runtime environment (please complete the following information):
 - OS/Docker image: Ubuntu 20.04/WSL
 - Branch: develop

# Fix?

One fix for this is to still output 16 nodes in the meshing program, but when reading them in discard out of bounds nodes (i.e. write them as -1 on the mesh file).
This allows the nodels local coordinates to still be indexable from their read-in position in node list for each element.
I implemented this quick fix locally, but it also requries an element allocated per cell, as the local mapping is generated at read time & unique.
