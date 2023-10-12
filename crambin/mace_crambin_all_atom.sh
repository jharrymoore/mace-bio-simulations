#!/bin/bash -l
#SBATCH -N 1
#SBATCH -t 12:00:00
#SBATCH -p ampere
#SBATCH --gres=gpu:1
#SBATCH -A csanyi-SL3-GPU

export HDF5_USE_FILE_LOCKING=FALSE
source ~/.bashrc

conda activate mace-mlmm
which python


mace-md -f minimised_system.pdb --ml_mol minimised_system.xyz --model_path /path/to/mace.model --steps 1000000 --interval 2 --output_dir crambin_2.5nm_high_res_long_periodic --nl nnpops
