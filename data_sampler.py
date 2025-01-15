import os
import random
from collections import defaultdict
import random
import random


### Old version
def stratified_sample_ltr_folder(folder_path, output_folder, sample_fraction=0.01, seed=42):
    """
    Stratified sampling of LTR datasets in a folder by qid from all .txt files.

    :param folder_path: Path to the folder containing LTR data files.
    :param output_folder: Path to the folder to save the sampled files.
    :param sample_fraction: Fraction of data to sample (e.g., 0.01 for 1%).
    :param seed: Random seed for reproducibility.
    """
    random.seed(seed)
    
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Process each .txt file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            qid_groups = defaultdict(list)
            
            # Group lines by qid for the current file
            with open(file_path, 'r') as infile:
                for line in infile:
                    parts = line.split()
                    qid = next((part.split(":")[1] for part in parts if part.startswith("qid:")), None)
                    if qid:
                        qid_groups[qid].append(line)
            
            # Sample lines within each qid group
            sampled_lines = []
            for qid, lines in qid_groups.items():
                sample_size = max(1, int(len(lines) * sample_fraction))
                sampled_lines.extend(random.sample(lines, sample_size))
            
            # Save the sampled lines to the corresponding output file
            output_file_path = os.path.join(output_folder, f'{filename}')
            with open(output_file_path, 'w') as outfile:
                outfile.writelines(sampled_lines)



# Use the function for your folder of LTR data
folder_path = './whole sets/MSLR30K/Fold5' #Your folder path containing .txt files
output_folder = './MSLR30K/Fold5'  # Folder path to save sampled files
sample_fraction = 0.01  # 1% of the data

stratified_sample_ltr_folder(folder_path, output_folder, sample_fraction)