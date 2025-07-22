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

def load_hashes(input_file):
    with open(input_file, 'r') as f:
        return json.load(f)

def compare_hashes(old_hashes, new_hashes):
    for path, old_hash in old_hashes.items():
        new_hash = new_hashes.get(path)
        if not new_hash:
            print(f"File missing: {path}")
        elif old_hash != new_hash:
            print(f"File changed: {path}")
    for path in new_hashes:
        if path not in old_hashes:
            print(f"New file detected: {path}")

if __name__ == "__main__":
    directory = input("Enter the directory to scan: ")
    baseline_file = "hashes.json"

    if not os.path.exists(baseline_file):
        print("No baseline found. Creating baseline...")
        files = get_all_files(directory)
        hashes = {f: calculate_hash(f) for f in files}
        save_hashes(hashes, baseline_file)
        print("Baseline saved.")
    else:
        print("Baseline found. Checking for changes...")
        old_hashes = load_hashes(baseline_file)
        files = get_all_files(directory)
        new_hashes = {f: calculate_hash(f) for f in files}
        compare_hashes(old_hashes, new_hashes)



