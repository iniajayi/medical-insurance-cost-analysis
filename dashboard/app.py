import streamlit as st
import pandas as pd
import plotly.express as px

# Load the cleaned insurance dataset
df = pd.read_csv("data/cleaned_insurance.csv")

# Set up the Streamlit page
st.set_page_config(
    page_title="Medical Insurance Cost Dashboard",
    layout="wide"
)

# Basic custom styling for the dashboard
st.markdown("""
<style>

.stApp {
    background-color: #fff0f6;
}

section[data-testid="stSidebar"] {
    background-color: white;
    border-right: 2px solid #f8bbd0;
}

h1 {
    color: #880e4f !important;
    font-weight: 700;
}

h2 {
    color: #ad1457 !important;
}

h3 {
    color: #c2185b !important;
}

html, body, [class*="css"] {
    color: #880e4f;
}

p {
    color: #880e4f;
}

label {
    color: #ad1457 !important;
    font-weight: 600;
}

section[data-testid="stSidebar"] * {
    color: #880e4f !important;
}

div[data-testid="metric-container"] {
    background-color: #ffe3ef;
    border: 2px solid #f48fb1;
    padding: 15px;
    border-radius: 12px;
    color: #880e4f !important;
}

div[data-testid="metric-container"] label {
    color: #880e4f !important;
}

.stButton > button {
    background-color: #ec407a;
    color: white;
    border-radius: 10px;
    border: none;
}

.stMultiSelect div[data-baseweb="select"] {
    background-color: white !important;
    border-radius: 10px;
    border: 1px solid #f8bbd0;
}

[data-testid="stDataFrame"] {
    background-color: white !important;
    border-radius: 10px;
    padding: 10px;
    border: 2px solid #f8bbd0;
}

[data-testid="stDataFrame"] table {
    background-color: white !important;
    color: #880e4f !important;
}

[data-testid="stDataFrame"] th {
    background-color: #ffe3ef !important;
    color: #880e4f !important;
    font-weight: bold !important;
}

[data-testid="stDataFrame"] td {
    background-color: white !important;
    color: #880e4f !important;
}

[data-testid="stPlotlyChart"] {
    background-color: white !important;
    padding: 0 !important;
    border-radius: 12px;
    border: 2px solid #f8bbd0;
    overflow: hidden;
}

</style>
""", unsafe_allow_html=True)

# Main dashboard heading
st.title("Medical Insurance Cost Dashboard")

st.write("""
This dashboard looks at how lifestyle and demographic factors may influence medical insurance charges.
""")

# Sidebar filters
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

# Filter the data based on the options selected by the user
filtered_df = df[
    (df["region"].isin(selected_region)) &
    (df["smoker"].isin(selected_smoker)) &
    (df["bmi_category"].isin(selected_bmi_category))
]

# Show headline metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Customers", f"{len(filtered_df):,}")
col2.metric("Average Charge", f"£{filtered_df['charges'].mean():,.2f}")
col3.metric("Average BMI", f"{filtered_df['bmi'].mean():.2f}")
col4.metric("Average Age", f"{filtered_df['age'].mean():.1f}")

st.divider()

# Compare charges for smokers and non-smokers
fig1 = px.box(
    filtered_df,
    x="smoker",
    y="charges",
    color="smoker",
    color_discrete_sequence=["#ff69b4", "#c2185b"],
    title="Insurance Charges by Smoking Status",
    labels={
        "smoker": "Smoker",
        "charges": "Insurance Charges"
    }
)

fig1.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(color="#880e4f", size=14),
    title=dict(font=dict(color="#880e4f", size=22)),
    margin=dict(l=80, r=50, t=90, b=80),
    legend=dict(
        title=dict(text="Smoker", font=dict(color="#880e4f")),
        font=dict(color="#880e4f", size=13),
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    xaxis=dict(
        title=dict(font=dict(color="#880e4f", size=16)),
        tickfont=dict(color="#880e4f", size=13)
    ),
    yaxis=dict(
        title=dict(font=dict(color="#880e4f", size=16)),
        tickfont=dict(color="#880e4f", size=13)
    )
)

st.plotly_chart(fig1, use_container_width=True)

# Check the relationship between BMI and charges
fig2 = px.scatter(
    filtered_df,
    x="bmi",
    y="charges",
    color="smoker",
    color_discrete_sequence=["#ff69b4", "#c2185b"],
    title="BMI vs Insurance Charges",
    labels={
        "bmi": "BMI",
        "charges": "Insurance Charges",
        "smoker": "Smoker"
    }
)

fig2.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(color="#880e4f", size=14),
    title=dict(font=dict(color="#880e4f", size=22)),
    margin=dict(l=80, r=50, t=90, b=80),
    legend=dict(
        title=dict(text="Smoker", font=dict(color="#880e4f")),
        font=dict(color="#880e4f", size=13),
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    xaxis=dict(
        title=dict(font=dict(color="#880e4f", size=16)),
        tickfont=dict(color="#880e4f", size=13)
    ),
    yaxis=dict(
        title=dict(font=dict(color="#880e4f", size=16)),
        tickfont=dict(color="#880e4f", size=13)
    )
)

st.plotly_chart(fig2, use_container_width=True)

# Calculate average charges by age group
age_summary = (
    filtered_df
    .groupby("age_group")["charges"]
    .mean()
    .reset_index()
)

# Show the average charge for each age group
fig3 = px.bar(
    age_summary,
    x="age_group",
    y="charges",
    color_discrete_sequence=["#ec407a"],
    title="Average Insurance Charge by Age Group",
    labels={
        "age_group": "Age Group",
        "charges": "Average Insurance Charge"
    }
)

fig3.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(color="#880e4f", size=14),
    title=dict(font=dict(color="#880e4f", size=22)),
    margin=dict(l=80, r=50, t=90, b=80),
    showlegend=False,
    xaxis=dict(
        title=dict(font=dict(color="#880e4f", size=16)),
        tickfont=dict(color="#880e4f", size=13)
    ),
    yaxis=dict(
        title=dict(font=dict(color="#880e4f", size=16)),
        tickfont=dict(color="#880e4f", size=13)
    )
)

st.plotly_chart(fig3, use_container_width=True)

# Show the filtered data table
st.subheader("Filtered Data Preview")

st.dataframe(
    filtered_df,
    use_container_width=True
)