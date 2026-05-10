from huggingface_hub import hf_hub_download
import tensorflow as tf
import numpy as np
import os

models = {}

HF_REPO = "almer1426/pneumonia-models"

def load_models():
    for name in ["densenet121_best.keras", "vgg16_best.keras"]:
        path = hf_hub_download(repo_id=HF_REPO, filename=name)
        models[name.replace("_best.keras", "")] = tf.keras.models.load_model(path)
    print("Models loaded.")

def predict(image_array: np.ndarray, model_name: str = "densenet121") -> dict:
    model = models.get(model_name)
    if model is None:
        raise ValueError(f"Model '{model_name}' not found.")

    raw_output = model.predict(image_array, verbose=0)  # shape: (1, 1)
    confidence = float(raw_output[0][0])

    # Model output: sigmoid → nilai mendekati 1 = PNEUMONIA, mendekati 0 = NORMAL
    label = "PNEUMONIA" if confidence >= 0.5 else "NORMAL"
    confidence_score = confidence if label == "PNEUMONIA" else 1 - confidence

    return {
        "label": label,
        "confidence": round(confidence_score, 4)
    }