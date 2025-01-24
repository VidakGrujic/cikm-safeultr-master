import pickle
import torch
import json
# Replace 'file_path' with the path to your file
file_path = 'CRM_project_logs/MSLR30K/logging_policy/logging_policy'

try:
    # Load the file using PyTorch
    data = torch.load(file_path)

    # Inspect or use the loaded data
    print(data)


    with open('CRM_project_logs/MSLR30K/logging_policy/logging_policy.txt', 'w', encoding='utf-8') as txt_file:
        txt_file.write(str(data))
    


except Exception as e:
    print(f"An error occurred: {e}")