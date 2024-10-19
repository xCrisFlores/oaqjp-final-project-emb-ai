"""This module provides a Flask application for emotion detection."""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template('index.html')

@app.route("/emotionDetector", methods=["GET"])
def analyze_emotion():
    """Analyze the provided text to detect emotions.

    Returns:
        JSON: A JSON object containing the analyzed text and the response
        from the emotion detector or an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return jsonify({"error": "No text provided for analysis"}), 400

    response, status_code = emotion_detector(text_to_analyze)

    if status_code == 400:
        return jsonify({"text": None, "response": None}), 400

    if response["dominant_emotion"] is None:
        return jsonify({
            "text": text_to_analyze,
            "response": "Invalid text! Please try again!"
        }), 400

    return jsonify({
        "text": text_to_analyze,
        "response": response
    })

if __name__ == "__main__":
    app.run(debug=True)
