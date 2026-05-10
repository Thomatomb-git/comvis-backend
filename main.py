from fastapi import FastAPI, File, UploadFile, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from model import load_models, predict
from preprocess import preprocess_image

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_models()
    yield

app = FastAPI(
    title="Pneumonia Detection API",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
async def predict_image(file: UploadFile = File(...), model: str = Query(default="densenet121", enum=["densenet121", "vgg16"])):
    if file.content_type not in ["image/jpeg", "image/png", "image/jpg"]:
        raise HTTPException(status_code=400, detail="File harus berupa JPEG atau PNG.")

    image_bytes = await file.read()
    image_array = preprocess_image(image_bytes)
    result = predict(image_array, model_name=model)

    return {
        "model": model,
        "label": result["label"],
        "confidence": result["confidence"]
    }