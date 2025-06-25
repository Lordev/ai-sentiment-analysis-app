import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}
    
    response = requests.post(url, json=myobj, headers=headers)

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        output = {}
        for emotion_name in emotions:
            output[emotion_name] = emotions[emotion_name]
        output["dominant_emotion"] = max(emotions, key=emotions.get)
        return output
    elif response.status_code == 400:
        output = {
            "anger": None,
            "disgust":  None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

