#!/bin/bash
#SBATCH --job-name=git_push
#SBATCH --output=./git_push.out
#SBATCH --time=1:00:00
#SBATCH -p msismall
#SBATCH --ntasks=1
#SBATCH --mem=2g

OUTPUT_FILE="csci5541-s24-hw4-NLPitch-3*.json"
OUTPUT_DIR="csci5541-hw-prompting"

mv $OUTPUT_FILE ../
cd ..

if [ -d "$OUTPUT_DIR" ]; then
    echo "$OUTPUT_DIR already exist."
else
    git clone https://github.com/minnesotanlp/$OUTPUT_DIR.git
fi

mv $OUTPUT_FILE $OUTPUT_DIR/
cd $OUTPUT_DIR

git branch NLPitch
git checkout NLPitch
git add --all
git commit -m "NLPitch: Data file push"