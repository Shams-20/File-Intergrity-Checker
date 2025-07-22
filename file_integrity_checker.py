# Importing standard libraries: os for file operations, hashlib for hashing, json for saving/loading data
import os
import hashlib
import json

def get_all_files(directory):       # Returns a list of all file paths under the given directory (recursively)
    file_paths = []                 # Creates an empty list to hold file paths.
    for root, dirs, files in os.walk(directory):        # Walks through the directory tree. os.walk function yields- root: current folder path , dirs: list of subdirectories , files: list of filenames in root.
        for filename in files:
            file_paths.append(os.path.join(root, filename))         # Build full file path and add to list
    return file_paths

def calculate_hash(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:         # Open file in binary mode
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)            # Reads files in chunks and updates hash
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

# Main script logic
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
    
        # ask if user wants to update baseline
    choice = input("Do you want to update the baseline with current state? (y/n): ").lower()
    if choice == "y":
        save_hashes(new_hashes, baseline_file)
        print("Baseline updated.")
    else:
        print("Baseline NOT updated. Keeping original.")

