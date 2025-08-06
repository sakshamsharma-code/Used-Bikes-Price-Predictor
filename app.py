from flask import Flask, app, render_template, request,url_for
import joblib
from sklearn.preprocessing import LabelEncoder
app = Flask(__name__)
model = joblib.load('model.lb')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')  

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        brand_name = request.form['brand_name']
        owner = float(request.form['owner'])
        age = float(request.form['age'])
        power = float(request.form['power'])
        kms_driven = float(request.form['kms_driven'])

        le_brand_name = LabelEncoder()
        le_brand_name.fit(['TVS', 'Royal Enfield', 'Triumph', 'Yamaha', 'Honda', 'Hero',
       'Bajaj', 'Suzuki', 'Benelli', 'KTM', 'Mahindra', 'Kawasaki',
       'Ducati', 'Hyosung', 'Harley-Davidson', 'Jawa', 'BMW', 'Indian',
       'Rajdoot', 'LML', 'Yezdi', 'MV', 'Ideal'])

        encoded_brand_name = le_brand_name.transform([brand_name])[0]
        input_vector = [encoded_brand_name, owner, age, power, kms_driven]

        prediction = model.predict([input_vector])[0]
        prediction = round(float(prediction), 2)

        return render_template('project.html', prediction=prediction)

    return render_template('project.html')
if __name__ == '__main__':
    app.run(debug=True)