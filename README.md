# Fintech Behavioral Segmentation API

A production-ready REST API that serves a KMeans behavioral segmentation model trained on **278,932 transactions** from an Indonesian digital payment platform (March–May 2024).

🚀 **Live API:** https://fintech-segmentation-api-production.up.railway.app

📖 **Interactive Docs:** https://fintech-segmentation-api-production.up.railway.app/docs

---

## Customer Segments

| Cluster | Segment | Description |
|---------|---------|-------------|
| 0 | Gaming Casuals | Low spend, high gaming ratio, infrequent transactions |
| 1 | Active Explorers | High diversity, frequent transactions across many categories |
| 2 | Established Regulars | High total spend, consistent behavior, loyalty-oriented |
| 3 | Food-Focused Occasionals | Restaurant/fast food dominant, occasional usage |

---

## Tech Stack

- **FastAPI** — REST API framework
- **scikit-learn** — KMeans clustering model (k=4, 31 features)
- **Pydantic** — Request validation
- **Uvicorn** — ASGI server
- **Docker** — Containerization
- **Railway** — Cloud deployment

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/segments` | List all 4 segments |
| POST | `/predict` | Predict segment for a user |

---

## Example Request

```bash
curl -X POST \
  https://fintech-segmentation-api-production.up.railway.app/predict \
  -H "Content-Type: application/json" \
  -d '{
    "avg_spend": 150000,
    "cv_spend": 0.5,
    "transaction_count": 45,
    "total_spend": 6750000,
    "weekend_ratio": 0.3,
    "payday_spike_ratio": 0.2,
    "active_days": 20,
    "tx_per_active_day": 2.25,
    "weekday_diversity": 0.7,
    "monthly_spend_std": 500000,
    "merchant_diversity": 0.6,
    "category_diversity": 0.5,
    "discount_ratio": 0.1,
    "loyalty_ratio": 0.3,
    "failed_tx_ratio": 0.05,
    "notes_ratio": 0.1,
    "credit_card_ratio": 0.2,
    "device_score": 0.8,
    "mobility_radius": 5.0,
    "restaurant_ratio": 0.3,
    "grocery_ratio": 0.1,
    "fast_food_ratio": 0.2,
    "pharmacy_ratio": 0.05,
    "fuel_ratio": 0.05,
    "electronics_ratio": 0.02,
    "travel_ratio": 0.01,
    "beauty_ratio": 0.02,
    "fashion_ratio": 0.02,
    "gaming_ratio": 0.1,
    "education_ratio": 0.01,
    "books_ratio": 0.01
  }'
```

## Example Response

```json
{
  "segment": "Active Explorers",
  "cluster_id": 1,
  "description": "..."
}
```

---

## Run Locally

```bash
# Clone the repo
git clone https://github.com/richardy-lobo-sapan/fintech-segmentation-api.git
cd fintech-segmentation-api

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs`

---

## Run with Docker

```bash
# Build image
docker build -t fintech-segmentation-api .

# Run container
docker run -p 8000:8000 fintech-segmentation-api
```

---

## Model Details

| Detail | Value |
|--------|-------|
| Algorithm | KMeans |
| Clusters | 4 |
| Features | 31 behavioral features |
| Dataset | 278,932 transactions |
| Users | 24,321 |
| Period | March - May 2024 |
| Scaler | StandardScaler |

---

## Project Structure
fintech-segmentation-api/
├── main.py              # FastAPI app and endpoints
├── model.py             # Model loading and prediction
├── schemas.py           # Pydantic request/response models
├── requirements.txt     # Python dependencies
├── Dockerfile           # Container configuration
├── .dockerignore        # Docker ignore rules
└── models/
├── kmeans_model.pkl
├── scaler.pkl
└── segment_names.pkl

---

## Author

**Richardy Lobo' Sapan**
- GitHub: [@richardy-lobo-sapan](https://github.com/richardy-lobo-sapan)
- LinkedIn: [https://www.linkedin.com/in/richardylobosapan/]