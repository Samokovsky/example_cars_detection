import cv2
from modules.detector import CarsDetection
from flask import Flask, request, jsonify
import base64
import numpy as np

app = Flask(__name__)


@app.route('/car/detection', methods=['POST'])
def detect_car():
    if 'image' not in request.json:
        return jsonify({'status': 'error', 'car_detected': False}), 400

    cd = CarsDetection()
    img, count = cd.detect_car(
        cv2.imdecode(
            np.frombuffer(
                base64.b64decode(request.json['image']), np.uint8
            ), cv2.IMREAD_UNCHANGED
        )
    )

    if count != 0:
        return jsonify({'status': 'success', 'car_detected': True})
    return jsonify({'status': 'success', 'car_detected': False})


app.run(host='0.0.0.0', port=8080)
