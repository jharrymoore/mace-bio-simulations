#!/bin/bash -l
#SBATCH -N 1
#SBATCH -t 18:00:00
#SBATCH -p ampere
#SBATCH --gres=gpu:1
#SBATCH -A csanyi-SL2-GPU

export HDF5_USE_FILE_LOCKING=FALSE
source ~/.bashrc

conda activate mace-mlmm
which python


mace-md -f ala3_solvated.pdb --ml_mol ala3_solvated.xyz --model_path /path/to/mace.model --output_dir mace_small_solv --steps 1000000 --interval 1000 --nl nnpops  --minimiser ase --unwrap --meta 