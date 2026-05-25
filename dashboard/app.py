import streamlit as st
import pandas as pd
import plotly.express as px

# Load cleaned data.
df = pd.read_csv("data/cleaned_insurance.csv")

# Set dashboard page settings.
st.set_page_config(
    page_title="Medical Insurance Cost Dashboard",
    layout="wide"
)

# Dashboard title.
st.title("Medical Insurance Cost Dashboard")

st.write("""
This dashboard explores how age, BMI, smoking status, number of children and region relate to medical insurance charges.
""")

# Sidebar filters.
st.sidebar.header("Filters")

selected_region = st.sidebar.multiselect(
    "Select region",
    options=df["region"].unique(),
    default=df["region"].unique()
)

selected_smoker = st.sidebar.multiselect(
    "Select smoking status",
    options=df["smoker"].unique(),
    default=df["smoker"].unique()
)

selected_bmi_category = st.sidebar.multiselect(
    "Select BMI category",
    options=df["bmi_category"].unique(),
    default=df["bmi_category"].unique()
)

# Apply filters.
filtered_df = df[
    (df["region"].isin(selected_region)) &
    (df["smoker"].isin(selected_smoker)) &
    (df["bmi_category"].isin(selected_bmi_category))
]

# KPI section.
col1, col2, col3, col4 = st.columns(4)

col1.metric("Customers", f"{len(filtered_df):,}")
col2.metric("Average Charge", f"£{filtered_df['charges'].mean():,.2f}")
col3.metric("Average BMI", f"{filtered_df['bmi'].mean():.2f}")
col4.metric("Average Age", f"{filtered_df['age'].mean():.1f}")

st.divider()

# Chart 1: charges by smoker.
fig1 = px.box(
    filtered_df,
    x="smoker",
    y="charges",
    title="Insurance Charges by Smoking Status",
    labels={
        "smoker": "Smoker",
        "charges": "Insurance Charges"
    }
)

st.plotly_chart(fig1, use_container_width=True)

# Chart 2: BMI versus charges.
fig2 = px.scatter(
    filtered_df,
    x="bmi",
    y="charges",
    color="smoker",
    title="BMI vs Insurance Charges",
    labels={
        "bmi": "BMI",
        "charges": "Insurance Charges",
        "smoker": "Smoker"
    }
)

st.plotly_chart(fig2, use_container_width=True)

# Chart 3: average charge by age group.
age_summary = (
    filtered_df
    .groupby("age_group")["charges"]
    .mean()
    .reset_index()
)

fig3 = px.bar(
    age_summary,
    x="age_group",
    y="charges",
    title="Average Insurance Charge by Age Group",
    labels={
        "age_group": "Age Group",
        "charges": "Average Insurance Charge"
    }
)

st.plotly_chart(fig3, use_container_width=True)

# Data table.
st.subheader("Filtered Data Preview")
st.dataframe(filtered_df)