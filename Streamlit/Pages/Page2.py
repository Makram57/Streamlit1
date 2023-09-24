import pandas as pd
import streamlit as st
import plotly.express as px


df22 = pd.read_csv(r"C:\Users\USER\Desktop\Data Visualization course\Mall_Customers.csv")

st.header("The following plot shows a Mall Customer Behavior versus their Annual Income, Spending Score, and Age",divider='rainbow')

AnnualIncome_filter = st.slider("Select Annual Income Range", min_value=int(df22['Annual Income (k$)'].min()), max_value=int(df22['Annual Income (k$)'].max()), value=(int(df22['Annual Income (k$)'].min()), int(df22['Annual Income (k$)'].max())))


filtered_df = df22[(df22['Annual Income (k$)'] >= AnnualIncome_filter[0]) & (df22['Annual Income (k$)'] <= AnnualIncome_filter[1])]


fig = px.scatter(filtered_df, x="Age", y="Spending Score (1-100)", color="Annual Income (k$)",
                 size="Spending Score (1-100)")
fig.update_layout(title="Mall Customers Behavior")

st.header("",divider='rainbow')

st.write(fig)

