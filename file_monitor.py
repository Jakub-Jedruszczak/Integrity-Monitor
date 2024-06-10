import os
import hashlib
import time
import json # for the output file

def calculate_file_hash(filepath, chunk_size=8192):
    sha512 = hashlib.sha512() # longer than 256, so fewer collisions
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(chunk_size), b""):
                sha512.update(chunk)
        return sha512.hexdigest()
    except IOError as e:
        print(f"Error reading {filepath}: {e}")
        return None

def erase_baseline_if_exists(baseline_file):
    # Used to reset the baseline file
    if os.path.exists(baseline_file):
        os.remove(baseline_file)

def collect_new_baseline(directory, baseline_file):
    # Creates new baseline file
    erase_baseline_if_exists(baseline_file)
    baseline = {}
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            file_hash = calculate_file_hash(filepath)
            if file_hash:
                baseline[filepath] = file_hash
    with open(baseline_file, 'w') as f:
        json.dump(baseline, f, indent=4)
    print("Baseline created")

def load_baseline(baseline_file):
    if not os.path.exists(baseline_file):
        return {}
    with open(baseline_file, 'r') as f:
        return json.load(f)
    print("Baseline file loaded")
    
def monitor_files(directory, baseline_file):
    baseline = load_baseline(baseline_file)
    while True:
        current_files = {}
        for root, _, files in os.walk(directory):
            for file in files:
                filepath = os.path.join(root, file)
                file_hash = calculate_file_hash(filepath)
                if file_hash:
                    current_files[filepath] = file_hash

        for filepath, file_hash in current_files.items():
            if filepath not in baseline:
                print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {filepath} has been created!")
            elif baseline[filepath] != file_hash:
                print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {filepath} has changed!!!")

        for filepath in set(baseline.keys()) - set(current_files.keys()):
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {filepath} has been deleted!")

        baseline = current_files
        time.sleep(1)

def main():
    print("\nWhat would you like to do?\n")
    print("    A) Collect new Baseline?")
    print("    B) Begin monitoring files with saved Baseline?\n")
    response = input("Please enter 'A' or 'B': ").strip().upper()

    directory_to_monitor = '.' # Enter your directory
    baseline_file = 'baseline_file.json' # Enter your baseline's file path

    if response == 'A':
        collect_new_baseline(directory_to_monitor, baseline_file)
    elif response == 'B':
        monitor_files(directory_to_monitor, baseline_file)
    else:
        print("Invalid response. Please enter 'A' or 'B'.")

if __name__ == "__main__":
    main()
