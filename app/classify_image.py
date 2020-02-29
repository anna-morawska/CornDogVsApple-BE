import os, io, json
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd 

client = vision.ImageAnnotatorClient()

def classify_image(image_save_path):
    with io.open(image_save_path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
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

    if os.path.exists(image_save_path):
        os.remove(image_save_path)     


    return df
