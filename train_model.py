import pickle
from sklearn.linear_model import LinearRegression

# Sample data
# Feature columns: [Area (sq ft), Number of Bedrooms, Number of Bathrooms]
X = [[1000, 2, 1], [1200, 3, 2], [800, 1, 1]]
# Target column: [Price in dollars]
y = [200000, 250000, 150000]

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the trained model to a file
model_file_path = 'linear_regression_model.pkl'
try:
    with open(model_file_path, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved successfully as '{model_file_path}'")
except Exception as e:
    print(f"Error saving the model: {e}")
