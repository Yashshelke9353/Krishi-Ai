import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# 1. Load dataset (adjust path if needed)
data_path = os.path.join("Data-processed", "crop_recommendation.csv")
data = pd.read_csv(data_path)


# 2. Features & target
X = data.drop('label', axis=1)   # 'label' should be the crop name
y = data['label']

# 3. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Train RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Save model compatible with sklearn 1.5.1
model_path = os.path.join("models", "RandomForest.pkl")
with open(model_path, "wb") as f:
    pickle.dump(model, f)

print("✅ Model retrained and saved at:", model_path)
