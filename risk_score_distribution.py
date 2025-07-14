import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

st.title("📈 Fraud Risk Score Distribution")

@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\AmlanC\OneDrive\Desktop\new database\credit_card_fraud_dataset.csv")
    df['transaction_timestamp'] = pd.to_datetime(df['transaction_timestamp'])
    df['fraud_flag'] = df['fraud_flag'].astype(int)
    df['hour'] = df['transaction_timestamp'].dt.hour
    df['weekday'] = df['transaction_timestamp'].dt.weekday
    return df

df = load_data()
df_model = df.drop(columns=['transaction_id', 'transaction_timestamp', 'ip_address', 'card_number',
                            'user_id', 'merchant_id', 'device_id'])
for col in ['currency', 'merchant_category_code', 'geo_location', 'channel', 'txn_type', 'txn_status']:
    df_model[col] = LabelEncoder().fit_transform(df_model[col])

X = df_model.drop('fraud_flag', axis=1)
y = df_model['fraud_flag']
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X, y)
df['risk_score'] = model.predict_proba(X)[:, 1]

fig, ax = plt.subplots()
sns.histplot(df['risk_score'], bins=30, kde=True, ax=ax)
st.pyplot(fig)
