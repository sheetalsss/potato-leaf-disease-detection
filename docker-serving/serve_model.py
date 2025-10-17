import tensorflow as tf
import numpy as np
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Load model
model_path = '/app/models/1'
print(f"Loading model from: {model_path}")

# Check if model exists
if not os.path.exists(model_path):
    print(f"ERROR: Model path {model_path} does not exist!")
    print("Contents of /app/models:")
    if os.path.exists('/app/models'):
        for item in os.listdir('/app/models'):
            print(f"  - {item}")
    else:
        print("  /app/models directory does not exist!")
else:
    print(f"Model path exists: {os.path.exists(model_path)}")
    print(f"Contents of model directory: {os.listdir(model_path)}")

model = tf.saved_model.load(model_path)
infer = model.signatures['serving_default']
print("Model loaded successfully!")


@app.route('/v1/models/potatoes_model:predict', methods=['POST'])  # CHANGED TO potatoes_model
@app.route('/v1/models/potato_model:predict', methods=['POST'])  # KEEP BOTH FOR FLEXIBILITY
def predict():
    try:
        data = request.get_json()
        print("Received prediction request")

        instances = data['instances']
        input_tensor = tf.constant(instances, dtype=tf.float32)
        predictions = infer(input_tensor)

        output_key = list(predictions.keys())[0]
        output = predictions[output_key].numpy().tolist()

        print(f"Prediction completed successfully")
        return jsonify({'predictions': output})

    except Exception as e:
        print(f"Prediction error: {str(e)}")
        return jsonify({'error': str(e)}), 400


@app.route('/v1/models/potatoes_model', methods=['GET'])
@app.route('/v1/models/potato_model', methods=['GET'])
def model_info():
    return jsonify({
        'model_version': '1',
        'status': 'available'
    })


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})


if __name__ == '__main__':
    print("Starting TensorFlow Serving compatible server on port 8601...")
    print("Server ready to accept requests!")
    app.run(host='0.0.0.0', port=8601, debug=False)