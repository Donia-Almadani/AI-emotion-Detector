"""
This module provides a Flask web application for AI emotion detection.
"""
from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector
app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the index.html the home page.

    Returns:

        str: Rendered to HTML.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """
    Handle the GET request .

    Returns:
     A JSON response with the emotion detector results .
    """
    text_to_analyze = request.args.get('textToAnalyze', '')
    emotion_text = emotion_detector(text_to_analyze)
    if emotion_text.get('dominant_emotion') is None:
        response_text = "Invalid text! Please try again!"
    else:
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {emotion_text.get('anger')}, "
            f"'disgust': {emotion_text.get('disgust')}, "
            f"'fear': {emotion_text.get('fear')}, "
            f"'joy': {emotion_text.get('joy')}, "
            f"and 'sadness': {emotion_text.get('sadness')}. "
            f"The dominant emotion is {emotion_text.get('dominant_emotion')}.")   
    return jsonify({"response": response_text})
if __name__ == "__main__":
    app.run(port=5001)
