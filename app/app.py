import streamlit as st
from google.cloud import bigquery

st.title("🚨 Fraud Detection Alerts")

client = bigquery.Client(project='975291545274')

query = """
SELECT * FROM `975291545274.fraud_detection_7.fraud_alerts`
ORDER BY timestamp DESC
LIMIT 100
"""
df = client.query(query).to_dataframe()
st.dataframe(df)
