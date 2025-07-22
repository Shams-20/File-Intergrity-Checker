import os
import hashlib
import json

def get_all_files(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_paths.append(os.path.join(root, filename))
    return file_paths

def calculate_hash(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

def save_hashes(hash_dict, output_file):
    with open(output_file, 'w') as f:
        json.dump(hash_dict, f, indent=4)



