import os
import shutil
import json
import logging
from datetime import datetime
from pathlib import Path

DESKTOP_PATH = Path.home() / "Desktop"
CONFIG_PATH = Path(__file__).parent / "config.json"
LOGS_DIR = Path(__file__).parent / "logs"
LOGS_DIR.mkdir(exist_ok=True)

# Setup logging
logging.basicConfig(
    filename=LOGS_DIR / "activity.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def load_config(config_path):
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ config.json not found.")
        exit(1)


def get_destination_folder(file_path, rules):
    ext = file_path.suffix.lower()
    for category, extensions in rules.items():
        if ext in extensions:
            return category
    return "Others"


def move_file(file_path, dest_folder):
    destination_dir = DESKTOP_PATH / dest_folder
    destination_dir.mkdir(exist_ok=True)

    destination_path = destination_dir / file_path.name

    # Avoid overwriting files with same name
    if destination_path.exists():
        timestamp = datetime.now().strftime("%H%M%S")
        new_name = f"{file_path.stem}_{timestamp}{file_path.suffix}"
        destination_path = destination_dir / new_name

    shutil.move(str(file_path), str(destination_path))
    logging.info(f"Moved: {file_path.name} → {dest_folder}/")
    print(f"✅ {file_path.name} → {dest_folder}/")

# Main cleaning function
def clean_desktop():
    print(f"Cleaning desktop: {DESKTOP_PATH}")
    rules = load_config(CONFIG_PATH)
    files_moved = 0

    for item in DESKTOP_PATH.iterdir():
        if item.is_file() and item.name != "cleaner.py" and item.name != "config.json":
            dest_folder = get_destination_folder(item, rules)
            move_file(item, dest_folder)
            files_moved += 1

    if files_moved == 0:
        print("No files to move — desktop already clean!")
    else:
        print(f"Done! Moved {files_moved} files. Check logs/activity.log for details.")


if __name__ == "__main__":
    clean_desktop()
