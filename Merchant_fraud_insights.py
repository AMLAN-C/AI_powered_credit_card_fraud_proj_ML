import streamlit as st
import pandas as pd

st.title("🛍️ Merchant Fraud Risk Insights")

df = pd.read_csv(r"C:\Users\AmlanC\OneDrive\Desktop\new database\credit_card_fraud_dataset.csv")

# Group by merchant MCC and risk
merchant_stats = df.groupby('merchant_category_code')['fraud_flag'].agg(
    total_txns='count',
    fraud_txns='sum',
    fraud_rate=lambda x: round(x.mean()*100, 2)
).reset_index().sort_values(by='fraud_rate', ascending=False)

st.dataframe(merchant_stats, use_container_width=True)

top_mcc = st.selectbox("Select MCC for drill-down", merchant_stats['merchant_category_code'].unique())
filtered = df[df['merchant_category_code'] == top_mcc]
st.write(f"Transactions for MCC: {top_mcc}")
st.dataframe(filtered.head(20))
