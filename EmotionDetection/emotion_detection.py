import requests  
import json

def emotion_detector(text_to_analyse): 
    if not text_to_analyse:
        return {"dominant_emotion": None}, 400  # Retorna un código de error si no hay texto

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }  
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    try:
        response = requests.post(url, json=myobj, headers=headers)
        response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        return {"dominant_emotion": None}, 400 

    f_response = json.loads(response.text)

    if not f_response.get('emotionPredictions'):
        return {"dominant_emotion": None}, 400 

    emotions = f_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
    
    emotion_result = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
        'dominant_emotion': dominant_emotion
    }
    
    return emotion_result, 200 
