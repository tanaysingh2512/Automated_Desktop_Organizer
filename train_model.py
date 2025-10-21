import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
from pathlib import Path

DATA_FILE = Path(__file__).parent / "file_training_data.csv"
df = pd.read_csv(DATA_FILE)
X = df["filename"]
y = df["label"]

# Convert text to numeric features
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Split dataset for evaluation
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)
model = MultinomialNB()
model.fit(X_train, y_train)

#  Evaluate model 
y_pred = model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))

joblib.dump((vectorizer, model), Path(__file__).parent / "file_classifier.pkl")
print("Model trained and saved as 'file_classifier.pkl'")
