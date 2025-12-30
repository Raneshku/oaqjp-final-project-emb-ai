import requests
import json

def emotion_detector(text_to_analyse):
    # URL of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the emotion analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the emotion analysis API
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract emotion label and score from the response
    if response.status_code == 200:
        # Save all emotion values
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        dominant_emotion = max(formatted_response['emotionPredictions'][0]['emotion'], key=emotions.get)
    # If the response status code is 400, set emotions to None
    elif response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None

    # Returning a dictionary containing emotion analysis results
    return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
            }