"""
server.py
A Flask server to analyze emotions in user-provided text using the 
Watson NLP Library's Emotion Predict API.
"""

from flask import Flask, request, render_template, jsonify
from final_project.emotion_detector import emotion_detector

# Create a Flask app instance
app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the index page.

    Returns:
        str: The HTML content of the index page.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Analyze the input text to detect emotions and provide a response.

    Returns:
        dict: A JSON object containing the detected emotions or an error message.
    """
    # Get the statement input from the request form
    statement = request.form.get('statement')

    # Process the statement using the emotion detector
    results = emotion_detector(statement)

    # Check if the dominant emotion is a specific error message
    if results['dominant_emotion'] == "Invalid text! Please try again!":
        return jsonify({'message': "Invalid text! Please try again!"})

    # Prepare a formatted response message
    response_message = (
        f"For the given statement, the system response is 'anger': {results['anger']}, "
        f"'disgust': {results['disgust']}, 'fear': {results['fear']}, "
        f"'joy': {results['joy']} and 'sadness': {results['sadness']}. "
        f"The dominant emotion is {results['dominant_emotion']}."
    )

    return jsonify({'message': response_message})

if __name__ == "__main__":
    # Run the Flask app on localhost port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
