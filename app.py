from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
model_file_path = 'linear_regression_model.pkl'

try:
    with open(model_file_path, 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully.")
except FileNotFoundError:
    model = None
    print(f"Error: Model file '{model_file_path}' not found.")
except pickle.UnpicklingError as e:
    model = None
    print(f"Error loading the model: {e}")

@app.route('/', methods=['GET', 'POST'])
def clickhere():
    prediction = None
    error_message = None

    if request.method == 'POST':
        if not model:
            error_message = "Model is not available. Please contact the administrator."
        else:
            try:
                # Parse user input
                area = float(request.form.get('area', '0'))
                bedrooms = float(request.form.get('no_of_bedrooms', '0'))
                bathrooms = float(request.form.get('no_of_bathrooms', '0'))

                # Predict the price
                prediction = model.predict([[area, bedrooms, bathrooms]])[0]
                prediction = round(prediction, 2)
            except ValueError:
                error_message = "Invalid input. Please enter valid numeric values."
            except Exception as e:
                error_message = f"An unexpected error occurred: {e}"

    return render_template('clickhere.html', prediction=prediction, error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
