File Integrity Monitoring Tool

This project is a lightweight Python-based tool that performs file integrity checking by creating and comparing file hashes. It is designed to help detect unauthorized changes, deletions, or additions in a specified directory.

Features

Recursive file scanning within a given directory

SHA-256 hash calculation for all files

Baseline creation for initial integrity state

Change detection for:

Modified files

Deleted files

Newly added files

Optional auto-update of baseline using command-line flag

Clear CLI reporting of integrity status

Getting Started

Requirements

Python 3.6 or higher

No external dependencies

Installation

Clone the repository:

git clone https://github.com/your-username/file-integrity-monitor.git
cd file-integrity-monitor

Run the script:

python file_integrity_checker.py

Usage

🔹 Initial Baseline Creation

When you run the tool for the first time, it asks for a directory and creates a baseline of hashes (hashes.json).

python file_integrity_checker.py

You'll see:

Enter the directory to scan: /path/to/your/folder
No baseline found. Creating baseline...
Baseline saved.

🔹 Detecting Changes

On next run, it compares the current state to the saved one and reports any:

🔄 Modified files

❌ Deleted files

🆕 New files

python file_integrity_checker.py

Example output:

Baseline found. Checking for changes...
File changed: /folder/doc.txt
New file detected: /folder/image.png
File missing: /folder/old_data.csv

You’ll be asked:

Do you want to update the baseline with current state? (y/n):

🔹 Auto-Update Mode

Skip the prompt and update the baseline automatically:

python file_integrity_checker.py --auto-update

Output:

Auto-update mode: updating baseline automatically.
Baseline updated.

🔧 How It Works

File Collection: Recursively walks the specified directory.

Hash Calculation: Computes SHA-256 hashes of all files.

Baseline: Saves these hashes to hashes.json.

Comparison: On next run, checks for differences from the saved baseline.

📄 Example

$ python file_integrity_checker.py
Enter the directory to scan: ./important_folder
Baseline found. Checking for changes...
File changed: ./important_folder/summary.docx
File missing: ./important_folder/old_config.json
New file detected: ./important_folder/new_image.png

📚 Future Improvements

Integration with SIEM tools (Splunk, ELK)

Threat intelligence using YARA rules

Timestamp manipulation and file permission checks

PDF/HTML reporting

Real-time monitoring agent

✉️ Contact

For questions, reach out to your-email@example.com or raise an issue in the repo.

✅ License

MIT License. See LICENSE file for details.

