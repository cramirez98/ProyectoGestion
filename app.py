from flask import Flask, render_template, request
from transformers import pipeline
from markupsafe import escape

classifier = pipeline('sentiment-analysis')

app = Flask(__name__)

@app.route("/NLP", methods=["POST"])
def nlp():
    return classifier(f"{escape(request.form['texto'])}")

@app.route("/")
def home():
    return render_template('nlp.html')