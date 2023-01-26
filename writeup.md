**Describe the bug**
A clear and concise description of the bug.
# GIMP broken?
The 2d, and 3d implementations of GIMP elements/particles have two issues with their implementation.
When using pycbg/GMSH to output nodes on the improve/mpmxdem branch gimp cells are generated with a different node order to those expected by the GIMP elements.
The 2D elements have incorrect shearing behaviour due to this, and the 3D elements have incorrect shear in one dimension but not the other.
This can be easily seen with a 1D consolidation problem.


**To Reproduce**
Steps to reproduce the behavior:
Compile the latest MPM branch
Grab some test 1D consolidation problems, available at:

2. Run on '....'
3. On condition '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Runtime environment (please complete the following information):**
 - OS/Docker image:
 - Branch [e.g. develop]

**Additional context**
Add any other context about the problem here.

