from ase import units
from ase.md.langevin import Langevin
from ase.io import read, write
import numpy as np
import time

from mace.calculators import MACECalculator
import time

calculator = MACECalculator(model_path='../SPICE_sm_inv_neut_E0_swa.model', device='cuda', eager_only=True)
init_conf = read('ala3_vac_capped.xyz', '0')
init_conf.set_calculator(calculator)

print(init_conf.get_potential_energy())

# dyn = Langevin(init_conf, 0.5*units.fs, temperature_K=310, friction=5e-3)
# def write_frame():
# 		dyn.atoms.write('md_3bpa.xyz', append=True)
# dyn.attach(write_frame, interval=10)
# t1 = time.time()
# dyn.run(10)
# t2 = time.time()

# ns_day = 1000 / (t2-t1) * 86400 / 1e6
# print("MD finished!", ns_day, "ns/day")
