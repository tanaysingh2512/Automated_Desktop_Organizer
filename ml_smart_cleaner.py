import os
import shutil
import pandas as pd
from pathlib import Path

# --- CONFIG ---
DESKTOP = Path.home() / "Desktop"
DATA_FILE = Path(__file__).parent / "file_training_data.csv"
TARGET_FOLDERS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Code": [".py", ".java", ".cpp"],
    "Compressed": [".zip", ".rar", ".tar", ".gz"],
    "Others": []
}

# --- 1️⃣ Collect data for ML ---
def log_file_move(file_name, destination_folder):
    """Record file movement into CSV dataset."""
    df = pd.DataFrame([[file_name, destination_folder]], columns=["filename", "label"])
    if DATA_FILE.exists():
        df.to_csv(DATA_FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(DATA_FILE, index=False)
    print(f"[LOG] Recorded: {file_name} -> {destination_folder}")

# --- 2️⃣ Clean + log files ---
def clean_desktop():
    for file in DESKTOP.iterdir():
        if file.is_file():
            ext = file.suffix.lower()
            moved = False

            for folder, extensions in TARGET_FOLDERS.items():
                if ext in extensions:
                    dest_folder = DESKTOP / folder
                    dest_folder.mkdir(exist_ok=True)
                    shutil.move(str(file), dest_folder / file.name)
                    log_file_move(file.name, folder)
                    moved = True
                    break

            if not moved:
                dest_folder = DESKTOP / "Others"
                dest_folder.mkdir(exist_ok=True)
                shutil.move(str(file), dest_folder / file.name)
                log_file_move(file.name, "Others")

if __name__ == "__main__":
    clean_desktop()
    print("✅ Cleaning + data logging complete!")
