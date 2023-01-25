import pycbg.preprocessing as utl
from pycbg.mesh import Mesh
import numpy as np
import math
dt = 1e-2
sim = utl.Simulation(title="mpm_consol")

#Resolution of domain
resolution = 10
resolutions = [resolution,resolution]

#height of column
length = 50
particle_dims   = (resolution,length)
domain_dims     = (resolution,length + (1*resolution))

node_type = "ED2Q4"
#node_type = "ED2Q16G"
#node_type = "ED3H64G"

#Create sim mesh
sim.create_mesh(dimensions=domain_dims, ncells=[x//r for x,r in zip(domain_dims,resolutions)],cell_type = node_type)
#Create particle mesh
pmesh = utl.Mesh(dimensions=particle_dims,origin=(0,0,0), ncells=[x//r for x,r in zip(particle_dims,resolutions)],cell_type=node_type)

#Set particles to fill particle mesh
mps_per_cell = 4
sim.particles = utl.Particles(pmesh,mps_per_cell,directory=sim.directory,particle_type="")

sim.init_entity_sets()
sim.particles._filename = "particles.txt"
sim.particles.write_file()

particles = sim.entity_sets.create_set(lambda x,y: True, typ="particle")

E = 1e6
nu = 0.0
density = 80
density_water = 999
#Set material properties
sim.materials.create_LinearElastic(pset_id=particles,density=density,youngs_modulus=E,poisson_ratio=nu)

walls = []

#Set boundary conditions
walls.append([sim.entity_sets.create_set(lambda x,y: x==lim, typ="node") for lim in [0, sim.mesh.l0]])
walls.append([sim.entity_sets.create_set(lambda x,y: y==lim, typ="node") for lim in [0, sim.mesh.l1]])
for direction, sets in enumerate(walls): _ = [sim.add_velocity_condition(direction, 0., es) for es in sets]

# Other simulation parameters (gravity, number of iterations, time step, ..):
sim.set_gravity([0,-10])
time = 100
nsteps = time//dt
sim.set_analysis_parameters(dt=dt,type="MPMExplicit2D", nsteps=nsteps, 
        output_step_interval=nsteps/100,
        damping=0.00)
#sim.analysis_params["damping"] = {"type": "Viscous", "damping_factor": E*1e-3}
#sim.analysis_params["velocity_update"] = True
sim.analysis_params["damping"] = {"type": "Cundall", "damping_factor": 0.05}
sim.post_processing["vtk"] = ["stresses","volume"]
sim.add_custom_parameters({"particles": particles, "walls": walls})
sim.write_input_file()

l = E * nu / ((1+nu)*(1-2*nu))
mu = E / (2*(1+nu))

bulk_stiffness = ((3 * l)+(2*mu))/3
min_x = min(resolutions[0:1])
speed_of_sound = math.sqrt(bulk_stiffness/density)

courant = speed_of_sound * dt/min_x

print("Ice properties")
print("bulk modulus {}".format(bulk_stiffness))
print("speed of sound {}".format(speed_of_sound))
print("Courant number of {}".format(courant))

print(
"""
Simulation properties:
Domain size {}
Particle size {}
dt {}
resolutions {}
E {}
nu {}
density {}
""".format(domain_dims,particle_dims,dt,resolutions,E,nu,density))

