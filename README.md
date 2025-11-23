Customer Segmentation Using K-Means
1. Overview

This project applies unsupervised learning to group customers based on their purchasing behavior, demographics, and engagement metrics. The goal is to identify actionable customer segments that support marketing decisions such as targeting, retention, and personalized campaigns.

2. Dataset

Mall Customer Segmentation (Kaggle)
Includes demographic features (age, income), purchase behavior (web/store purchases), spending categories, website visits, and recency of last purchase.

3. Workflow

Exploratory Data Analysis (EDA)

Handling missing values

Feature engineering (Age, Total Spending, Customer Tenure, etc.)

Standard scaling

Determining optimal clusters using the Elbow Method

Training a K-Means model

Visualizing clusters

Saving the trained model and scaler

Deploying a prediction app using Streamlit

4. Features Used for Clustering

The final clustering model uses the following numerical features:

Age

Income

Total_Spending

NumStorePurchases

NumWebPurchases

NumWebVisitsMonth

Recency

These features were scaled using StandardScaler before clustering.

5. Customer Segments (K-Means Results)

Cluster 0 – Low-Value Inactive Customers
Low income and spending; low activity; high recency.

Cluster 1 – Affluent Multi-Channel Spenders
High income and high spending; active across store and web channels.

Cluster 2 – Active Mid-Value Shoppers
Moderate income and spending; engaged and balanced in purchasing behavior.

Cluster 3 – Top-Tier High-Value Customers
Highest income and spending; strong and consistent activity.

Cluster 4 – Senior Low-Activity Customers
Higher age group; modest spending and lower engagement.

Cluster 5 – New / Recently Active Low-Spend Customers
Recently active but with low spending; early lifecycle stage.

6. Streamlit App

The model and scaler are saved using joblib and loaded into a Streamlit application for real-time customer segment prediction.

Run locally:

pip install -r requirements.txt
streamlit run src/segmentation.py

7. Project Structure
Customer-Segmentation/
│
├── Models/
│   ├── kmeans_model.pkl
│   └── scaler.pkl
│
├── Notebooks/
│   └── Analysis_Model.ipynb
│
├── src/
│   └── segmentation.py
│
├── requirements.txt
└── README.md
