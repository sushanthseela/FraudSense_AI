from flask import Flask, render_template, request, redirect, url_for
from ExtractText import extract_text_from_image, classify_text  # Importing from ExtractText.py
from URLTest import predict_url  # Importing from URLTest.py
import random
from matplotlib.figure import Figure
import io
from base64 import b64encode

app = Flask(__name__)

# Confidence score and message mapping based on conditions
def get_confidence_score(text_classification, url_category):
    if text_classification == "Legitimate":
        if url_category == "A":
            return 99, "Both the text and the link look Legitimate and safe to open."
        elif url_category == "B":
            return 85, "The text looks Legitimate but the link may have potential issues."
        elif url_category == "C":
            return 50, "The text may seem Legitimate, but the link is broken."
    else:
        if url_category in ["A", "B"]:
            return 25, "The text is not Legitimate; open the link at your own risk."
        elif url_category == "C":
            return 5, "Both the text and link are not Legitimate. Do not open the link."

# Route for home page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the uploaded image
        image = request.files.get("image")
        if image:
            # Extract text and classify it
            extracted_text = extract_text_from_image(image)
            text_classification = classify_text(extracted_text)

            # Get user-entered URL and classify it
            user_url = request.form.get("url")
            url_category = predict_url(user_url) if user_url != "NA" else "C"
            confidence, message = get_confidence_score(text_classification, url_category[0])

            # Generate the spooky pie chart based on confidence
            fig = Figure()
            ax = fig.subplots()
            ax.pie([confidence, 100 - confidence], labels=['Confidence', 'Uncertainty'], 
                   startangle=90, colors=['#00ff00', '#ff0000'] if confidence > 50 else ['#ffa500', '#000000'])
            buf = io.BytesIO()
            fig.savefig(buf, format="png")
            buf.seek(0)
            pie_chart = b64encode(buf.read()).decode('utf8')

            return render_template("index.html", extracted_text=extracted_text, user_url=user_url, 
                                   message=message, confidence=confidence, pie_chart=pie_chart)
    return render_template("index.html", extracted_text="", user_url="", message="", confidence=0, pie_chart="")

if __name__ == "__main__":
    app.run(debug=True)
