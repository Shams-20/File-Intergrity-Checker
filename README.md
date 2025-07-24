# 🛡️ File Integrity Monitoring Tool

A lightweight Python-based integrity checker that keeps your files in check and your folders honest. Perfect for spotting sneaky changes, deletions, or weird file drop-ins in any directory you care about.


## Features

- Recursive scanning of all files in a directory
- Calculates secure SHA-256 hashes
- Creates a baseline of the current file state
- Detects:
  - Modified files
  - Deleted/missing files
  - Newly added files
- Option to auto-update the baseline using a flag
- Human-readable CLI output


## Requirements

- Python 3.6 or higher
- No third-party libraries needed, 100% standard library


## Installation

Clone this bad boy:

```bash
git clone https://github.com/your-username/file-integrity-monitor.git
cd file-integrity-monitor
```


## Usage

### Basic Mode

```bash
python file_integrity_checker.py
```

You'll be prompted to enter the directory to scan. If it's your first time, it'll create a baseline. Every time after that, it’ll compare your current files to the saved baseline.

### Auto-Update Mode

```bash
python file_integrity_checker.py --auto-update
```

Runs the same comparison, but will **automatically update** the baseline if any changes are detected.


## How It Works

1. **First Run:**  
   - You give it a directory.
   - It hashes all files inside (recursively).
   - It saves that state in a `hashes.json` file.

2. **Later Runs:**  
   - It re-hashes everything.
   - Compares the new hashes with the old ones.
   - Reports:
     - 🔄 Changed files
     - ❌ Missing files
     - ➕ New files
   - You choose to update the baseline or keep it.


## Example Output

```
Enter the directory to scan: C:\Users\Example\Documents
Baseline found. Checking for changes...
File changed: C:\Users\Example\Documents\resume.docx
New file detected: C:\Users\Example\Documents\secret_notes.txt
Do you want to update the baseline with current state? (y/n): 
```

Or with auto-update:
```
Baseline found. Checking for changes...
File missing: C:\Important\config.json
Auto-update mode: updating baseline automatically.
Baseline updated.
```


## Test It Yourself

Try this:
1. Run the script in a folder.
2. Add, delete, or change a file.
3. Run it again and watch it catch the change!


## File Structure

```
file-integrity-monitor/
├── file_integrity_checker.py
├── hashes.json   ← Generated on first run
└── README.md
```


## 🧾 License

MIT - do what you want, just don’t pretend you built it from scratch 😘


## 💬 Contact

Got beef, bugs, or billion-dollar job offers? Hit me up at `shamsxshaikh@gmail.com`.

