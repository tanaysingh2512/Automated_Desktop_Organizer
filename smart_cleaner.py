import os
import shutil
from pathlib import Path
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
from datetime import datetime
import argparse

#Path to ML model and CSV file
DESKTOP = Path.home() / "Desktop"
MODEL_FILE = Path(__file__).parent / "file_classifier.pkl"
DATA_FILE = Path(__file__).parent / "file_training_data.csv"

LOGS_DIR = Path(__file__).parent / "logs"
LOGS_DIR.mkdir(exist_ok=True)
LOG_FILE = LOGS_DIR / "activity.log"

#Arguments
parser = argparse.ArgumentParser(description="Smart Desktop Cleaner (ML-powered)")
parser.add_argument(
    "--path",
    type=str,
    default=str(DESKTOP),
    help="Path of folder to clean (default is Desktop)."
)
parser.add_argument(
    "--retrain",
    action="store_true",
    help="Retrain the ML model using the latest training data and exit."
)
args = parser.parse_args()

TARGET_PATH = Path(args.path)

def retrain_model():
    if not DATA_FILE.exists():
        print("No training data found. Skipping retraining.")
        return None, None

    df = pd.read_csv(DATA_FILE)
    if df.empty:
        print("Training data is empty. Skipping retraining.")
        return None, None

    X = df["filename"]
    y = df["label"]

    vectorizer = CountVectorizer()
    X_vectorized = vectorizer.fit_transform(X)

    model = MultinomialNB()
    model.fit(X_vectorized, y)

    # Save updated model
    joblib.dump((vectorizer, model), MODEL_FILE)
    print("Model retrained with latest data.")
    return vectorizer, model

def log_action(filename, folder_name):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {filename} → {folder_name}\n")

def clean_folder(vectorizer, model):
    files_moved = 0
    for file in TARGET_PATH.iterdir():
        if file.is_file() and file.name not in ["smart_cleaner.py", "file_classifier.pkl"]:
            X = vectorizer.transform([file.name])
            folder_name = model.predict(X)[0]

            dest_folder = TARGET_PATH / folder_name
            dest_folder.mkdir(exist_ok=True)
            
            shutil.move(str(file), dest_folder / file.name)
            print(f"Moved: {file.name} → {folder_name}/")
            log_action(file.name, folder_name)
            files_moved += 1

    if files_moved == 0:
        print("No files to move — folder already clean!")
    else:
        print(f"Cleaning complete! {files_moved} files moved.")

if __name__ == "__main__":
    if args.retrain:
        retrain_model()
        exit()

    if MODEL_FILE.exists():
        vectorizer, model = joblib.load(MODEL_FILE)
    else:
        vectorizer, model = retrain_model()
        if vectorizer is None or model is None:
            print("Cannot clean without a trained model.")
            exit()

    clean_folder(vectorizer, model)
    retrain_model()
