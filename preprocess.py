import numpy as np
from PIL import Image
import io

IMG_SIZE = (224, 224)

def preprocess_image(image_bytes: bytes) -> np.ndarray:
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize(IMG_SIZE)
    # Tidak perlu normalisasi manual (/255) karena preprocess_input
    # sudah ter-embed di dalam graph model saat training.
    # VGG16 → applications.vgg16.preprocess_input (BGR + mean subtraction)
    # DenseNet121 → applications.densenet.preprocess_input (scale ke [-1,1])
    array = np.array(image, dtype=np.float32)
    return np.expand_dims(array, axis=0)  # shape: (1, 224, 224, 3)