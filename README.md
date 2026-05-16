# Fintech Behavioral Segmentation API

A production-ready REST API built with **FastAPI** that serves a KMeans behavioral segmentation model trained on 278,932 transactions from an Indonesian digital payment platform (March–May 2024).

## Segments

| Cluster | Segment Name | Description |
|---------|-------------|-------------|
| 0 | Gaming Casuals | Low spend, high gaming ratio, infrequent transactions |
| 1 | Active Explorers | High diversity, frequent transactions across many categories |
| 2 | Established Regulars | High total spend, consistent behavior, loyalty-oriented |
| 3 | Food-Focused Occasionals | Restaurant/fast food dominant, occasional usage |

## Tech Stack

- **FastAPI** — REST API framework
- **scikit-learn** — KMeans model (k=4, 31 features)
- **Pydantic** — Request validation
- **Uvicorn** — ASGI server

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/segments` | List all 4 segments |
| POST | `/predict` | Predict segment for a user |

## Run Locally

```bash
# Activate virtual environment
venv\Scripts\activate

# Start server
uvicorn main:app --reload
```

API docs available at `http://127.0.0.1:8000/docs`

## Model Details

- **Algorithm:** KMeans (k=4)
- **Features:** 31 behavioral features (spend patterns, category ratios, temporal behavior)
- **Dataset:** 278,932 transactions, 24,321 users
- **Scaler:** StandardScaler
