import pickle

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_crop(features):
    prediction = model.predict([features])
    return prediction[0]

# CLI Interface
if __name__ == "__main__":
    print("🌾 Welcome to ChashiHelper 🌾")
    print("Enter soil & weather details:\n")

    N = float(input("Nitrogen (N): "))
    P = float(input("Phosphorus (P): "))
    K = float(input("Potassium (K): "))
    temperature = float(input("Temperature (°C): "))
    humidity = float(input("Humidity (%): "))
    ph = float(input("pH value: "))
    rainfall = float(input("Rainfall (mm): "))

    features = [N, P, K, temperature, humidity, ph, rainfall]

    result = predict_crop(features)

    print(f"\n✅ Recommended Crop: {result}")
