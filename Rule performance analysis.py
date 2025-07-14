import streamlit as st
import pandas as pd

st.title("🧠 Rule-Based Fraud Detection Insights")

df = pd.read_csv(r"C:\Users\AmlanC\OneDrive\Desktop\new database\credit_card_fraud_dataset.csv")

# Example rules
df['rule_high_amt'] = df['amount'] > 50000
df['rule_risky_mcc'] = df['merchant_category_code'].isin(['7995', '4829', '5967'])

rule_stats = {
    'High Amount > ₹50k': df[df['rule_high_amt']]['fraud_flag'].mean(),
    'Risky MCC': df[df['rule_risky_mcc']]['fraud_flag'].mean()
}
st.write("📊 Rule Effectiveness (Fraud Rate):")
for rule, rate in rule_stats.items():
    st.metric(rule, f"{rate * 100:.2f}%")