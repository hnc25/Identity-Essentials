import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Function to fetch identity data
def get_identity_data(time_range):
    # Your data generation logic here
    if time_range == "1 Month":
        return {
            "total_profiles": {
                "Total Profiles": 25000,
                "Matched csCoreID": 18000,
                "Matched csHHId": 10000,
                "Duplicate Records (%)": 10.5,
            },
            "channel_distribution": {
                "Categories": ["Address", "Email", "Phone"],
                "Total Identifiers": [190000, 175000, 165000],
                "Unique Channel Reach (%)": [85, 75, 65],
            },
            "coreid_match_reach": {
                "Match Rate (%)": 67.0,
                "Reach Rate (%)": 90.0,
            },
        }
    # Add other ranges similarly

# Streamlit Layout
st.title("Combined Identity & Hygiene Dashboard")

# Time Range Selection
time_range = st.selectbox("Select Time Range", ["1 Month", "3 Months", "6 Months"], index=0)

# Identity Section
st.header("Identity Reporting")
identity_data = get_identity_data(time_range)

# Total Profiles
st.subheader("Total Profiles")
for key, value in identity_data["total_profiles"].items():
    st.write(f"**{key}:** {value:,}" if "Duplicate" not in key else f"**{key}:** {value}%")

# Channel Distribution
st.subheader("Channel Distribution")
channel_data = identity_data["channel_distribution"]
channel_fig = px.bar(
    x=channel_data["Categories"],
    y=channel_data["Total Identifiers"],
    labels={'x': "Category", 'y': "Total Identifiers"},
    title="Total Identifiers by Channel"
)
st.plotly_chart(channel_fig)

# Unique Channel Reach
st.subheader("Unique Channel Reach (%)")
reach_fig = px.bar(
    x=channel_data["Categories"],
    y=channel_data["Unique Channel Reach (%)"],
    labels={'x': "Category", 'y': "Reach (%)"},
    title="Unique Channel Reach (%)"
)
st.plotly_chart(reach_fig)

# CoreID Match and Reach
st.subheader("CoreID Match and Reach")
match_gauge = go.Figure(go.Indicator(
    mode="gauge+number",
    value=identity_data["coreid_match_reach"]["Match Rate (%)"],
    title={"text": "Match Rate (%)"},
    gauge={"axis": {"range": [0, 100]}},
))
reach_gauge = go.Figure(go.Indicator(
    mode="gauge+number",
    value=identity_data["coreid_match_reach"]["Reach Rate (%)"],
    title={"text": "Reach Rate (%)"},
    gauge={"axis": {"range": [0, 100]}},
))
st.plotly_chart(match_gauge)
st.plotly_chart(reach_gauge)
