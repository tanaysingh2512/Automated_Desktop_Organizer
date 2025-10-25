# Automated Desktop Organizer

An intelligent desktop organization tool that automatically categorizes, moves, and manages files using machine learning.  
The system monitors desktop activity, classifies files based on their type and content, and keeps the workspace clutter-free.  
This project combines automation, machine learning, and practical file management to improve productivity and digital organization.

---

## Features

### Automated File Organization
Automatically sorts files into relevant folders (e.g., Images, Documents, PDFs, Code) based on learned patterns.

### Machine Learning Classifier
A trained model (`file_classifier.pkl`) predicts file categories using metadata and file attributes.

### Smart Learning and Adaptation
The system improves over time by training on real file data (`file_training_data.csv`).

### Custom Configuration
The `config.json` file allows users to define custom folder paths and rules.

### Logging and Tracking
Every action is recorded in the `logs/` directory for transparency and debugging.

### Backup Functionality
Includes `desktop_cleaner_backup.py` for safe file management and recovery.

---

## Configuration

```{
  "desktop_path": "/Users/username/Desktop",
  "folders": {
    "Documents": ["pdf", "docx", "txt", "xlsx"],
    "Images": ["png", "jpg", "jpeg", "gif"],
    "Code": ["py", "js", "html", "css"],
    "Others": []
  },
  "log_path": "./logs/cleaner.log"
}
```

##Installation

### Clone the repository
```
git clone https://github.com/tanaysingh2512/Automated_Desktop_Organizer.git
cd Automated_Desktop_Organizer
```

### Create and activate a virtual environment
```
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies
```pip install -r requirements.txt
```

### Run the cleaner
```python desktop_cleaner.py
```

## Machine Learning Model

The ML classifier (file_classifier.pkl) learns from file names, extensions, and metadata to categorize files.
To retrain the model:
python train_model.py

## File Overview

| File                        | Description                                                       |
| --------------------------- | ----------------------------------------------------------------- |
| `desktop_cleaner_backup.py` | Script that performs desktop cleaning and file organization. |
| `ml_smart_cleaner.py`       | Uses machine learning for intelligent file classification.        |
| `train_model.py`            | Script to train or retrain the classification model.              |
| `config.json`               | Configuration file for folder paths and user preferences.         |
| `file_classifier.pkl`       | Pre-trained model used for classification.                        |
| `file_training_data.csv`    | Dataset used to train the ML model.                               |
| `logs/`                     | Directory storing logs of cleaning operations.                    |
| `requirements.txt`          | List of Python dependencies for the project.                      |
| `smart_cleaner.py`          | Enhanced cleaner script integrating both automation and ML.       |

## Example Log Entry
```
[2025-10-26 00:45:12] INFO - File 'invoice_2025.pdf' moved to 'Documents'
[2025-10-26 00:45:12] INFO - File 'photo.jpg' moved to 'Images'
[2025-10-26 00:45:12] INFO - File 'main.py' moved to 'Code'
```
## Technical Stack

### Language: Python 3.x

### Libraries: scikit-learn, pandas, os, shutil, logging, json

### Model: Supervised learning classifier trained on file metadata and naming patterns
