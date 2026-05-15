import pickle
import numpy as np

with open('models/kmeans_model.pkl', 'rb') as f:
    kmeans = pickle.load(f)

with open('models/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('models/segment_names.pkl', 'rb') as f:
    segment_names = pickle.load(f)

segment_descriptions = {
    'Active Explorers': 'Highest-value users. Frequent, high-spend, wide merchant diversity. Platform power users.',
    'Established Regulars': 'Largest segment. Stable, routine-driven adults. Predictable spending on pharmacy, fuel, fashion.',
    'Gaming Casuals': 'Smallest segment. Defined entirely by gaming spending. Young, predominantly male.',
    'Food-Focused Occasionals': 'Least active segment. Narrow food-centric spending. Low frequency, low spend.'
}

feature_order = [
    'avg_spend', 'cv_spend', 'transaction_count', 'total_spend',
    'weekend_ratio', 'payday_spike_ratio', 'active_days', 'tx_per_active_day',
    'weekday_diversity', 'monthly_spend_std', 'merchant_diversity', 'category_diversity',
    'discount_ratio', 'loyalty_ratio', 'failed_tx_ratio', 'notes_ratio',
    'credit_card_ratio', 'device_score', 'mobility_radius', 'restaurant_ratio',
    'grocery_ratio', 'fast_food_ratio', 'pharmacy_ratio', 'fuel_ratio',
    'electronics_ratio', 'travel_ratio', 'beauty_ratio', 'fashion_ratio',
    'gaming_ratio', 'education_ratio', 'books_ratio'
]

def predict_segment(features: dict) -> dict:
    X = np.array([[features[f] for f in feature_order]])
    X_scaled = scaler.transform(X)
    cluster_id = int(kmeans.predict(X_scaled)[0])
    segment = segment_names[cluster_id]

    return {
        'segment': segment,
        'cluster_id': cluster_id,
        'description': segment_descriptions[segment]
    }