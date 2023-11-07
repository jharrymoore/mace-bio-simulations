import ase.data
import ase.io
import numpy as np
import torch
import time
from e3nn.util import jit
from mace import data
from mace.tools import torch_geometric, torch_tools, utils

model = torch.load(f="../SPICE_sm_inv_neut_E0_swa.model", map_location="cuda")
model = model.to(
    "cuda"
)  # shouldn't be necessary but seems to help wtih CUDA problems

# model = jit.compile(model)

torch_tools.set_default_dtype("float64")

for param in model.parameters():
    param.requires_grad = False

# Load data and prepare input
atoms_list = ase.io.read("ala3_vac_capped.xyz", index=":")
configs = [data.config_from_atoms(atoms) for atoms in atoms_list]

z_table = utils.AtomicNumberTable([int(z) for z in model.atomic_numbers])

data_loader = torch_geometric.dataloader.DataLoader(
    dataset=[
        data.AtomicData.from_config(
            config, z_table=z_table, cutoff=float(model.r_max)
        )
        for config in configs
    ],
    batch_size=1,
    shuffle=False,
    drop_last=False,
)

# Collect data
energies_list = []
contributions_list = []
stresses_list = []
forces_collection = []

# single batch
batch = next(iter(data_loader)).to("cuda").to_dict()
s = torch.cuda.Stream()
with torch.cuda.stream(s):
    for i in range(3):
        output = model(batch, compute_stress=False)
torch.cuda.current_stream().wait_stream(s)


g = torch.cuda.CUDAGraph()
with torch.cuda.graph(g):
    output = model(batch, compute_stress=False)



t1 = time.time()
for _ in range(1000):

    output = g.replay()
    # model(batch, compute_stress=False)

t2 = time.time()
print(t2 - t1)
print(output)