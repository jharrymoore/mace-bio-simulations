#!/bin/bash -l
#SBATCH -N 1
#SBATCH -t 24:00:00
#SBATCH -p ampere
#SBATCH --gres=gpu:1
#SBATCH -A csanyi-SL2-GPU

export HDF5_USE_FILE_LOCKING=FALSE
source ~/.bashrc

conda activate mace-mlmm
which python


mace-md -f ala3_vac_capped.pdb --ml_mol ala3_vac_capped.xyz --model_path /path/to/mace.model --output_dir mace_small_vac_5ns --steps 5000000 --interval 1000 --nl nnpops  --minimiser ase --unwrap --meta 