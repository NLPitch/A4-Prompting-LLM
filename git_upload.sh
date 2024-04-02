#!/bin/bash
#SBATCH --job-name=git_push
#SBATCH --output=./git_push.out
#SBATCH --time=1:00:00
#SBATCH -p msismall
#SBATCH --ntasks=1
#SBATCH --mem=2g

pwd