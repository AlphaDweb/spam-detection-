import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load dataset (tab-separated)
data = pd.read_csv("sms.csv", sep="\t", header=None, names=["label", "text"])

# Map labels to binary values (ham = 0, spam = 1)
data["label"] = data["label"].map({"ham": 0, "spam": 1})

# Remove rows with missing values (if any)
data.dropna(inplace=True)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    data["text"], data["label"], test_size=0.2, random_state=42
)

# Vectorization (convert text to numerical format)
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train the model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Save model and vectorizer
joblib.dump(model, "spam_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

# Evaluate the model
y_pred = model.predict(X_test_vec)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
