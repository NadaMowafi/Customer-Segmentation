# Models

This folder contains the trained K-Means model and the scaler used
during preprocessing. These files allow the segmentation pipeline
to be reused without retraining.

- `kmeans_model.pkl` – trained K-Means clustering model  
- `scaler.pkl` – StandardScaler used to transform the numerical features  

Both are loaded in `src/segmentation.py` for inference.
