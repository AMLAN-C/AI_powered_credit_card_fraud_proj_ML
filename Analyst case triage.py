import streamlit as st
import pandas as pd

st.title("🕵️ Analyst Case Triage Simulator")

df = pd.read_csv(r"C:\Users\AmlanC\OneDrive\Desktop\new database\credit_card_fraud_dataset.csv")
df = df.sample(10).reset_index(drop=True)

df['Suspected Flags'] = df.apply(lambda x:
    "⚠️ High Amount" if x['amount'] > 50000 else
    "🔎 Risky MCC" if x['merchant_category_code'] in ['7995', '4829'] else
    "✅ Normal", axis=1)

for i, row in df.iterrows():
    st.markdown(f"### Case {i+1}")
    st.write(row[['amount', 'channel', 'merchant_category_code', 'geo_location', 'Suspected Flags']])
    decision = st.radio(f"Action for Case {i+1}", ['Approve', 'Review', 'Block'], key=f"decision_{i}")
    st.markdown("---")
