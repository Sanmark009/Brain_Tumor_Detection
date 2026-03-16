from flask import Flask, render_template, request, redirect, session, url_for
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from PIL import Image
import io
import os
import json

app = Flask(__name__)
app.secret_key = "vadivel_secret_key"

# Load pre-trained model
model = tf.keras.models.load_model("model/brain_tumor_model.h5")

# Load class indices from JSON
with open('class_indices.json', 'r') as f:
    class_indices = json.load(f)

# Reverse the mapping to get label names based on index
labels = {v: k for k, v in class_indices.items()}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if "username" in session:
        return redirect(url_for("dashboard"))

    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "password":
            session["username"] = username
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid username or password"
    return render_template("index.html", error=error)

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))
    
    result = None

    if request.method == "POST":
        patient_name = request.form.get("patient_name")
        father_name = request.form.get("father_name")
        dob = request.form.get("dob")
        file = request.files.get("file")

        if file:
            try:
                # Process image
                img = Image.open(io.BytesIO(file.read())).convert("RGB")
                img = img.resize((224, 224))
                img_array = image.img_to_array(img)
                img_array = np.expand_dims(img_array, axis=0) / 255.0

                # Predict
                prediction = model.predict(img_array)
                confidence = float(np.max(prediction)) * 100
                label_index = np.argmax(prediction)
                label = labels[label_index]  # Use the class index mapping

                affected_area = round(confidence, 2) if label != "No Tumor" else 0.0
                healthy_area = round(100.0 - affected_area, 2)

                # Store the result
                result = {
                    "patient_name": patient_name,
                    "father_name": father_name,
                    "dob": dob,
                    "label": label,
                    "confidence": round(confidence, 2),
                    "affected_area": affected_area,
                    "healthy_area": healthy_area
                }

                # Pass result to the results page
                return render_template("results.html", result=result)
            except Exception as e:
                result = {"error": "Prediction failed. Please check the uploaded image."}

    return render_template("dashboard.html", result=result)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
