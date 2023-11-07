# create a test system and run on GPU
import sys
from openmmtools.testsystems import AlanineDipeptideExplicit


import openmm
import openmm.app
from openmm import unit

test_system = AlanineDipeptideExplicit()
system = test_system.system
positions = test_system.positions


# create the simulation
integrator = openmm.LangevinIntegrator(300*unit.kelvin, 1.0/unit.picoseconds, 2.0*unit.femtoseconds)
platform = openmm.Platform.getPlatformByName('CUDA')
simulation = openmm.app.Simulation(test_system.topology, system, integrator, platform)
simulation.context.setPositions(positions)

# minimize
simulation.minimizeEnergy()

# run
simulation.context.setVelocitiesToTemperature(300*unit.kelvin)
simulation.reporters.append(openmm.app.DCDReporter('output.dcd', 1000))
simulation.reporters.append(openmm.app.StateDataReporter(sys.stdout, 1000, step=True, potentialEnergy=True, temperature=True))

simulation.step(10000)