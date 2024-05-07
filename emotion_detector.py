# emotion_detection.py

import requests

def emotion_detector(text_to_analyze):
    """
    Function that analyzes the emotion of a given text using the Watson NLP Library's Emotion Predict API.

    Parameters:
    text_to_analyze (str): The text content that needs emotion detection analysis.

    Returns:
    dict: Contains scores for various emotions and the dominant emotion.
    """

    # Set up the URL and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    # Construct the input JSON structure
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Make the API call using a POST request
    response = requests.post(url, headers=headers, json=payload)

    # Handle possible errors
    if response.status_code == 200:
        # Extract the response as a JSON dictionary
        result = response.json()
        #print("Full Response:", result)  # For debugging purposes

        # Access the "emotion" field inside the first element of "emotionPredictions"
        predictions = result.get("emotionPredictions", [])
        if predictions:
            emotions = predictions[0].get("emotion", {})
        else:
            raise Exception("No emotion predictions found in the response.")

        # Extract individual emotion scores
        anger_score = emotions.get("anger", 0)
        disgust_score = emotions.get("disgust", 0)
        fear_score = emotions.get("fear", 0)
        joy_score = emotions.get("joy", 0)
        sadness_score = emotions.get("sadness", 0)

        # Find the dominant emotion by comparing the scores
        scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(scores, key=scores.get)

        # Return the structured result
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }

    elif response.status_code ==400:
        return{
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': "Invalid text! Please try again!"
        }
    else:
        # Handle errors (e.g., invalid response from the server)
        raise Exception(f"Error: {response.status_code}, {response.text}")

# Example usage:
if __name__ == "__main__":
    # Test the function with some sample text
    text = "I love new technology."
    try:
        result = emotion_detector(text)
        print("Emotion Analysis Result:", result)
    except Exception as e:
        print(f"An error occurred: {e}")
