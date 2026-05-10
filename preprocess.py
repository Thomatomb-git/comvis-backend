import numpy as np
from PIL import Image
import io

IMG_SIZE = (224, 224)

def preprocess_image(image_bytes: bytes) -> np.ndarray:
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize(IMG_SIZE)
    array = np.array(image, dtype=np.float32) / 255.0
    return np.expand_dims(array, axis=0)  # shape: (1, 224, 224, 3)