from flask import Flask, request, render_template_string
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# HTML inside Python
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Crop AI</title>
    <style>
        body {font-family: Arial; text-align: center; padding: 40px;}
        input {margin: 5px; padding: 8px;}
        button {padding: 10px 20px; background: green; color: white; border: none;}
    </style>
</head>
<body>

<h2>🌾 AI Crop Recommendation</h2>

<form action="/predict" method="post">
    <input type="text" name="N" placeholder="Nitrogen" required><br>
    <input type="text" name="P" placeholder="Phosphorus" required><br>
    <input type="text" name="K" placeholder="Potassium" required><br>
    <input type="text" name="temperature" placeholder="Temperature" required><br>
    <input type="text" name="humidity" placeholder="Humidity" required><br>
    <input type="text" name="rainfall" placeholder="Rainfall" required><br>

    <button type="submit">Predict</button>
</form>

<h3>{{ prediction_text }}</h3>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        final = np.array([features])
        prediction = model.predict(final)

        return render_template_string(HTML,
                                     prediction_text=f"🌱 Recommended Crop: {prediction[0]}")
    except:
        return render_template_string(HTML,
                                     prediction_text="❌ Invalid input!")

if __name__ == "__main__":
    app.run(debug=True)
