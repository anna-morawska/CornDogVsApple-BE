import json
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd 

client = vision.ImageAnnotatorClient()

def classify_image(uploaded_file):
    image = types.Image(content=uploaded_file)
    response = client.label_detection(image=image)
    labels = response.label_annotations

    df = pd.DataFrame(columns=['description', 'score', 'topicality'])
    for label in labels:
        df = df.append(
            dict(
                description = label.description,
                score = label.score,
                topicality = label.topicality,
            ), ignore_index=True
        )
    
    df = json.loads(df.to_json())

    return df
