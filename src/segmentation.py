import streamlit as st
import pandas as pd
import joblib

# -------------------- Page config --------------------
st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="🧩",
    layout="wide"
)

# -------------------- Load model & scaler --------------------
kmeans = joblib.load("../Models/kmeans_model.pkl")
scaler = joblib.load("../Models/scaler.pkl")

# Cluster labels (personas)
cluster_labels = {
    0: "Low-Value Inactive Customers",
    1: "Affluent Multi-Channel Spenders",
    2: "Active Mid-Value Shoppers",
    3: "Top-Tier High-Value Customers",
    4: "Senior Low-Activity Customers",
    5: "New or Recently Active Low-Spend Customers"
}

cluster_descriptions = {
    0: "Lower income and low spending, not very active recently.",
    1: "High income, high spending and active on both web and store.",
    2: "Good income and spending, recently engaged across channels.",
    3: "Highest income and spending – VIP customers.",
    4: "Older customers with modest spending and lower activity.",
    5: "Recently active customers with currently low spending."
}

# -------------------- Layout: header --------------------
st.title("🧩 Customer Segmentation Prediction")
st.markdown(
    "Use this tool to simulate a customer profile and see which **segment/persona** "
    "the trained K-Means model assigns."
)

st.markdown("---")

# -------------------- Sidebar: inputs --------------------
st.sidebar.header("🧍 Customer Profile")

Age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=35)
Annual_Income = st.sidebar.number_input("Annual Income", min_value=10, max_value=200000, value=50000)
total_spending = st.sidebar.number_input("Total Spending (sum of purchases)", min_value=0, max_value=5000, value=1000)
num_store_purchases = st.sidebar.number_input("Number of Store Purchases", min_value=0, max_value=100, value=10)
num_web_purchases = st.sidebar.number_input("Number of Web Purchases", min_value=0, max_value=100, value=10)
num_web_visits_month = st.sidebar.number_input("Number of Web Visits per Month", min_value=0, max_value=50, value=5)
recency = st.sidebar.number_input("Recency (days since last purchase)", min_value=0, max_value=365, value=30)

predict_button = st.sidebar.button("🔮 Predict Segment")

# -------------------- Prepare input data --------------------
input_data = pd.DataFrame({
    "Age": [Age],
    "Income": [Annual_Income],
    "Total_Spending": [total_spending],
    "NumStorePurchases": [num_store_purchases],
    "NumWebPurchases": [num_web_purchases],
    "NumWebVisitsMonth": [num_web_visits_month],
    "Recency": [recency]
})

# -------------------- Main area: prediction & display --------------------
col_left, col_right = st.columns([1.2, 1])

with col_left:
    st.subheader("📊 Current Input Summary")
    st.dataframe(input_data.style.format({"Income": "{:,.0f}", "Total_Spending": "{:,.0f}"}))

    if predict_button:
        # Scale and predict
        scaled = scaler.transform(input_data)
        cluster = int(kmeans.predict(scaled)[0])
        persona = cluster_labels.get(cluster, "Unknown Segment")
        desc = cluster_descriptions.get(cluster, "")

        st.markdown("---")
        st.subheader("✅ Prediction Result")
        st.success(f"Predicted cluster: **{cluster}**")
        st.markdown(f"### 🧍 Customer Persona: **{persona}**")
        st.write(desc)

with col_right:
    st.subheader("ℹ️ How to read this app")
    st.markdown(
        """
        - Use the controls in the **sidebar** to simulate a customer's behaviour.  
        - Click **Predict Segment** to see which cluster they belong to.  
        - Each cluster is mapped to a **business-friendly persona name**, not just a number.  

        **Features used by the model:**
        - Age  
        - Income  
        - Total Spending  
        - Store Purchases  
        - Web Purchases  
        - Web Visits per Month  
        - Recency (days since last purchase)  
        """
    )
