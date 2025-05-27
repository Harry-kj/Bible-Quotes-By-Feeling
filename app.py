<<<<<<< HEAD
from flask import Flask, render_template, jsonify, request
import json
import random
import os

app = Flask(__name__)

# Load JSON data once when app starts
with open('emotion_verses.json', encoding='utf-8') as f:
    emotion_verses = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verse/<emotion>')
def get_verse(emotion):
    verses = emotion_verses.get(emotion, [])
    if not verses:
        return jsonify({"error": "No verses found for this emotion"}), 404
    verse = random.choice(verses)
    return jsonify(verse)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
=======
from flask import Flask, render_template, jsonify, request
import json
import random
import os

app = Flask(__name__)

# Load JSON data once when app starts
with open('emotion_verses.json', encoding='utf-8') as f:
    emotion_verses = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verse/<emotion>')
def get_verse(emotion):
    verses = emotion_verses.get(emotion, [])
    if not verses:
        return jsonify({"error": "No verses found for this emotion"}), 404
    verse = random.choice(verses)
    return jsonify(verse)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
>>>>>>> d9a72738d026b7896c8c5261de303b03c492d8e8
