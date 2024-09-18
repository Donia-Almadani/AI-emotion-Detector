import requests
import json 

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=headers, json=input_json)
    if response.status_code==400:
         return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    dicText = json.loads(response.text)
    emotion_data = dicText['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion_data, key=emotion_data.get)
    emotion_data['dominant_emotion'] = dominant_emotion
    return emotion_data