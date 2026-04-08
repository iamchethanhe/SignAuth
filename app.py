import os
import numpy as np
import cv2
from flask import Flask, render_template, request, redirect, url_for
from tensorflow.keras.models import load_model

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load models
image_model = load_model("models/image_model.h5")
sign_model = load_model("models/sign_model.h5")


# ---------------- LOGIN ----------------
@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username == "chethan" and password == "chethan123":
        return redirect(url_for("home"))
    else:
        return render_template("login.html", error="Invalid credentials")


# ---------------- HOME ----------------
@app.route("/home")
def home():
    return render_template("index.html")


# ---------------- ABOUT ----------------
@app.route("/about")
def about():
    return render_template("about.html")


# ---------------- SERVICE ----------------
@app.route("/service")
def service():
    return render_template("service.html")


# ---------------- PREDICT ----------------
@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["file"]
    mode = request.form["mode"]

    if file.filename == "":
        return render_template("service.html", result="No file selected")

    path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(path)

    img = cv2.imread(path)
    img = cv2.resize(img, (128,128))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    if mode == "image":
        pred = image_model.predict(img)[0][0]
        result = "Tampered Image ❌" if pred > 0.5 else "Authentic Image ✅"
    else:
        pred = sign_model.predict(img)[0][0]
        result = "Forged Signature ❌" if pred > 0.5 else "Genuine Signature ✅"

    return render_template(
        "service.html",
        result=result,
        img_path=f"uploads/{file.filename}",
        mode=mode
    )


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)