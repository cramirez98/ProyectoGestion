from flask import Flask, render_template, request
from transformers import pipeline
from markupsafe import escape
from os import environ
MODEL = environ['MODEL']
classifier = pipeline(task='sentiment-analysis', model = MODEL)
app = Flask(__name__)

@app.route("/sentimentanalysis", methods=["GET"])
def nlp():
    return classifier(request.args.get("texto"))

@app.route("/")
def home():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0')
