import pandas as pd
import pickle
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load cleaned data.
df = pd.read_csv("data/cleaned_insurance.csv")


X = df.drop(columns=["charges"])
y = df["charges"]

# Identifying categorical columns.
categorical_features = X.select_dtypes(include=["object", "category"]).columns

# Identifying numeric columns.
numeric_features = X.select_dtypes(include=["int64", "float64"]).columns

# Preprocessing prepares the data before modelling.
preprocessor = ColumnTransformer(
    transformers=[
        ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("numeric", StandardScaler(), numeric_features)
    ]
)

# Creating the model pipeline.
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", LinearRegression())
    ]
)

# Splitting the data into training and test data.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train the model.
model.fit(X_train, y_train)

# Make predictions on the test data.
predictions = model.predict(X_test)

# Evaluate the model.
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Model results:")
print("Mean Absolute Error:", round(mae, 2))
print("Mean Squared Error:", round(mse, 2))
print("R2 Score:", round(r2, 3))

# Save the model.
Path("models").mkdir(exist_ok=True)

with open("models/insurance_cost_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved at models/insurance_cost_model.pkl")