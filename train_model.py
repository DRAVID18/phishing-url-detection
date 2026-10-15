
import os
import joblib
import pandas as pd

from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# 1. Load the dataset
dataset = fetch_ucirepo(id=327)

X = dataset.data.features
target = dataset.data.targets.iloc[:, 0]

# 2. Convert labels:
# -1 = phishing, 1 = legitimate
target = pd.to_numeric(target)
y = (target == -1).astype(int)

# 3. Inspect the dataset
print("Dataset shape:", X.shape)
print("Missing values:", X.isnull().sum().sum())
print("Label counts:")
print(y.value_counts())

# 4. Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 5. Train the model
model = DecisionTreeClassifier(
    max_depth=8,
    random_state=42
)
model.fit(X_train, y_train)

# 6. Evaluate predictions
predictions = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, predictions))
print("\nClassification Report:")
print(classification_report(
    y_test,
    predictions,
    target_names=["Legitimate", "Phishing"]
))
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

# 7. Save the trained model and feature names
os.makedirs("models", exist_ok=True)

joblib.dump(
    {
        "model": model,
        "features": list(X.columns)
    },
    "models/phishing_model.joblib"
)

print("\nModel saved successfully!")
