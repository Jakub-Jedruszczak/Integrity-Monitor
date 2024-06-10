# File Integrity Monitor
This is a lightweight File Integrity Monitor (FIM) written in Python. It calculates SHA-512 hashes for files in a specified directory, creates a baseline for monitoring, and continuously checks for any changes, creations, or deletions of files. When an alert is triggered, a popup message box is displayed to notify the user.

---

## Features
* *SHA-512 Hashing*: Uses SHA-512 to ensure the integrity of the monitored files.
* *Baseline Creation*: Create a new baseline for the files in the specified directory.
* *Continuous Monitoring*: Continuously monitors the files against the saved baseline.
* **NEW!** *Popup Alerts*: Displays popup alerts using Tkinter for any file changes, creations, or deletions.

## Installation
Clone the Repository:
```bash
git clone https://github.com/Jakub-Jedruszczak/Integrity-Monitor
cd Integrity-Monitor
```

## Install Dependencies:
This project only requires the standard Python libraries, so no additional dependencies need to be installed.

## Usage
### Run the Script:
```bash
python integrity_monitor.py
```
### Select Operation Mode:
When prompted, choose:
* `A` to collect a new baseline.
* `B` to begin monitoring files with the saved baseline.

### Directory to Monitor:
The script monitors the root (`.`) directory by default. You can change this by modifying the `directory_to_monitor` variable in the script.

### Baseline file:
The script creates a `baseline_file.json` file in the root directory by default. Modifty the `baseline_file` variable in the script to change this.
