from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression
import pickle
import pandas as pd

app = Flask(__name__)

with open('linear_regression_model.plk','rb') as f:
     model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def clickhere():
    if request.method == 'POST':
        try:
            area = float(request.form['area'])
            bedrooms = float(request.form['no_of_bedrooms'])
            bathrooms = float(request.form['no_of_bathrooms'])

            prediction = model.predict([[area, bedrooms, bathrooms]])

            return render_template('clickhere.html', prediction=prediction)
        except KeyError:
            # Handle the case where the "area" key is missing
            error_message = "Please enter a value for the lot area."
            return render_template('clickhere.html', error=error_message)
    return render_template('clickhere.html')



if __name__ == '__main__':
    app.run(debug=True)