
# Packages
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load the Model
interpreter = tf.lite.Interpreter(model_path='ThunderModel/movenet_thunder.tflite')
interpreter.allocate_tensors()

# Web Cam Application
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()

    # Reshape Image
    img = frame.copy()
    img = tf.image.resize_with_pad(np.expand_dims(img, axis=0), 256, 256)
    input_image = tf.cast(img, dtype=tf.float32)

    # Setup input and output

    # Predict

    cv2.imshow('Movenet Thunder', frame)

    if cv2.waitKey(10) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
