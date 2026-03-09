import pandas as pd
import streamlit as st

data = pd.read_csv("dataset/
hospital_billing.csv")

missing_claims =
data[data["Claim_Submitted"] == "No"]

data["Underpaid"] = 
data["Expected_Amount"] - 
data["Paid_Amount"]

underpaid_claims = data[data["Underpaid"]
> 0]

st.title("AI Revenue Leakage Detection System")

st.subheader("Missing Claims")
st.write(missing_claims)

st.subheader("Underpaid Claims")
st.write(underpaid_claims)

total_loss = data["Underpaid"].sum()

st.subheader("Estimated Revenue Loss")
st.write(total_loss)
