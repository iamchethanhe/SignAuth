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


# ---------------- FACE DETECTION ----------------
def contains_face(filepath):
    img = cv2.imread(filepath)

    if img is None:
        return False

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    return len(faces) > 0


# ---------------- SIGNATURE VALIDATION ----------------
def is_signature_image(filepath):
    img = cv2.imread(filepath)

    if img is None:
        return False

    img = cv2.resize(img, (128, 128))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    std_dev = np.std(img)
    dark_pixels = np.sum(gray < 100) / (128 * 128)

    edges = cv2.Canny(gray, 50, 150)
    edge_density = np.sum(edges) / (128 * 128)

    if std_dev > 60:
        return False

    if dark_pixels < 0.05:
        return False

    if edge_density < 0.01:
        return False

    return True


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

    # Save file
    path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(path)

    # Read & preprocess
    img = cv2.imread(path)
    img = cv2.resize(img, (128, 128))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # ---------------- IMAGE DETECTION ----------------
    if mode == "image":
        pred = image_model.predict(img)[0][0]
        result = "Tampered Image ❌" if pred > 0.5 else "Authentic Image ✅"

    # ---------------- SIGNATURE DETECTION ----------------
    else:

        # 🔥 STEP 1: FACE CHECK (MAIN FIX)
        if contains_face(path):
            return render_template(
                "service.html",
                result="❌ This is a human image, not a signature",
                img_path=f"uploads/{file.filename}",
                mode=mode
            )

        # 🔥 STEP 2: SIGNATURE VALIDATION
        if not is_signature_image(path):
            return render_template(
                "service.html",
                result="❌ Please upload a proper signature image",
                img_path=f"uploads/{file.filename}",
                mode=mode
            )

        # 🔥 STEP 3: MODEL PREDICTION
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