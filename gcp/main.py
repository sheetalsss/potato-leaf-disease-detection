from google.cloud import storage
import tensorflow as tf
from PIL import Image
import numpy as np
import functions_framework
import os

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

BUCKET_NAME = 'tf-models-24'  # Fixed: removed space
class_names = ['Early blight', 'Late blight', 'Healthy']

model = None


def download_blob(bucket_name, source_blob_name, destination_file_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)


@functions_framework.http
def predict(request):
    global model

    if model is None:
        # Use /tmp directory (correct path for Cloud Functions)
        model_path = '/tmp/potatoes.h5'  # Fixed path, no space
        download_blob(BUCKET_NAME, 'models/potatoes.h5', model_path)
        model = tf.keras.models.load_model(model_path)

    # Handle GET requests
    if request.method == 'GET':
        return {'status': 'ready', 'message': 'Model loaded successfully'}, 200

    # Handle POST requests with image
    if 'file' not in request.files:
        return {'error': 'No file provided'}, 400

    try:
        image_file = request.files['file']
        image = Image.open(image_file).convert('RGB').resize((256, 256))
        image = np.array(image) / 255.0
        image = tf.expand_dims(image, axis=0)

        predictions = model.predict(image)
        predicted_class = class_names[np.argmax(predictions[0])]
        confidence = round(100 * (np.max(predictions[0])), 2)

        return {
            'class': predicted_class,
            'confidence': confidence,
            'status': 'success'
        }, 200

    except Exception as e:
        return {'error': str(e)}, 500