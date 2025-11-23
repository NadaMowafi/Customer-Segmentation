# Customer Segmentation Using K-Means

## 1. Description
This project demonstrates how unsupervised machine learning can identify meaningful customer segments based on purchasing behavior, engagement, and demographics.  
The segmentation provides actionable insights for marketing teams, customer retention planning, and personalized strategies.

---

## 2. Dataset
**Customer Segmentation Dataset — Kaggle**  
Contains demographic information, product spending, purchase frequency, web activity, and recency.

---

## 3. Goals
- Perform exploratory data analysis  
- Engineer useful features (Age, Total Spending, Tenure, etc.)  
- Apply feature scaling  
- Determine the optimal number of clusters using the Elbow Method  
- Train a K-Means clustering model  
- Visualize clusters in 2D  
- Analyze income and spending across segments  
- Compare K-Means with DBSCAN  
- Deploy a prediction app using Streamlit  

---

## 4. Tools & Libraries
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  
- Joblib  
- Streamlit  
- Jupyter Notebook  

---

## 5. Results and Business Insights

K-Means clustering was applied to the engineered features:

**Age, Income, Total_Spending, NumStorePurchases, NumWebPurchases, NumWebVisitsMonth, Recency**

Using the Elbow Method, the optimal number of clusters was determined to be **6**.

### Customer Segments

#### Cluster 0 – Low-Value Inactive Customers
Low income, low spending, high recency, minimal engagement.

#### Cluster 1 – Affluent Multi-Channel Spenders
High income, strong spending, active in both online and in-store channels.

#### Cluster 2 – Active Mid-Value Shoppers
Moderate income and spending, balanced purchase patterns, low recency.

#### Cluster 3 – Top-Tier High-Value Customers
Highest income and spending. Premium customers suited for loyalty programs.

#### Cluster 4 – Senior Low-Activity Customers
Older demographic with modest income and low engagement.

#### Cluster 5 – New or Recently Active Low-Spend Customers
Recent activity but low spending. Ideal for onboarding and upselling.

---

## 6. Installation

Clone the repository:

```bash
git clone <your-repo-url>
cd Customer-Segmentation
```

Install dependencies:

```bash
pip install -r requirements.txt
```
Run the Streamlit app:
```bash
streamlit run src/segmentation.py
```

