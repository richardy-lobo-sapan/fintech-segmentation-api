from fastapi import FastAPI, HTTPException
from schemas import UserFeatures, PredictionResponse
from model import predict_segment, segment_names, segment_descriptions

app = FastAPI(
    title="Fintech Behavioral Segmentation API",
    description="Predicts customer segments from behavioral features of Indonesian fintech users.",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is running"}

@app.get("/segments")
def get_segments():
    return {
        "segments": [
            {
                "cluster_id": cluster_id,
                "name": name,
                "description": segment_descriptions[name]
            }
            for cluster_id, name in segment_names.items()
        ]
    }

@app.post("/predict", response_model=PredictionResponse)
def predict(features: UserFeatures):
    try:
        result = predict_segment(features.dict())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))