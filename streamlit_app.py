import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Identity Data
def get_identity_data(time_range):
    if time_range == "1 Month":
        return {
            "total_profiles": {
                "Total Profiles": 25000,
                "Matched csCoreID": 18000,
                "Matched csHHId": 10000,
                "Duplicate Records (%)": 10.5,
            },
            "channel_distribution": {
                "Total Identifiers": [190000, 175000, 165000],
                "Unique Identifiers": [180000, 170000, 150000],
                "Categories": ["Address", "Email", "Phone"],
                "Unique Channel Reach (%)": [85, 75, 65],
            },
            "coreid_match_reach": {
                "Match Rate (%)": 67.0,
                "Reach Rate (%)": 90.0,
            },
        }
    elif time_range == "3 Months":
        return {
            "total_profiles": {
                "Total Profiles": 75000,
                "Matched csCoreID": 60000,
                "Matched csHHId": 30000,
                "Duplicate Records (%)": 12.0,
            },
            "channel_distribution": {
                "Total Identifiers": [450000, 525000, 420000],
                "Unique Identifiers": [360000, 420000, 300000],
                "Categories": ["Address", "Email", "Phone"],
                "Unique Channel Reach (%)": [80, 75, 71],
            },
            "coreid_match_reach": {
                "Match Rate (%)": 72.0,
                "Reach Rate (%)": 88.0,
            },
        }
    elif time_range == "6 Months":
        return {
            "total_profiles": {
                "Total Profiles": 150000,
                "Matched csCoreID": 120000,
                "Matched csHHId": 60000,
                "Duplicate Records (%)": 14.0,
            },
            "channel_distribution": {
                "Total Identifiers": [900000, 1050000, 840000],
                "Unique Identifiers": [720000, 840000, 600000],
                "Categories": ["Address", "Email", "Phone"],
                "Unique Channel Reach (%)": [80, 77, 71],
            },
            "coreid_match_reach": {
                "Match Rate (%)": 75.0,
                "Reach Rate (%)": 92.0,
            },
        }


# Streamlit Layout for Identity
def display_identity_data():
    st.subheader("Identity Reporting")
    st.write("The Identity Reporting Dashboard in Connect 2.0 provides clients with actionable insights into their audience universe and unique reach across various channels. Select a time range to view dynamically updated metrics, graphs, and visualizations.")

    time_range = st.selectbox("Select Time Range:", ["1 Month", "3 Months", "6 Months"], index=0)
    data = get_identity_data(time_range)

    st.subheader("Total Profiles")
    st.write("Displays the total number of audience profiles ingested into the system, including matched individuals and households, and accounts for duplication.")
    st.markdown("**Business Goal:** How many unique individuals and households exist in my universe?")
    
    # Convert total profiles data into a table
    total_profiles = data["total_profiles"]
    total_profiles_df = pd.DataFrame([total_profiles])
    total_profiles_df = total_profiles_df.rename(index={0: "Values"}).T.reset_index()
    total_profiles_df.columns = ["Metric", "Value"]
    st.table(total_profiles_df)

    st.subheader("Channel Distribution")
    st.write("Bar chart showing total identifiers across different categories (Address, Email, Phone).")
    st.markdown("**Business Goal:** How much unique reach exists across owned marketing channels?")

    channel_data = data["channel_distribution"]
    channel_bar_fig = px.bar(
        x=channel_data["Categories"],
        y=channel_data["Total Identifiers"],
        text=[f"{val:,}" for val in channel_data["Total Identifiers"]],
        labels={'x': "Category", 'y': "Total Identifiers"},
        title="Total Identifiers by Channel"
    )
    st.plotly_chart(channel_bar_fig)

    st.subheader("Unique Channel Reach (%)")
    st.write("Breaks down the total audience reach across owned marketing channels (Address, Email, Phone) and highlights unique reach percentages.")
    st.markdown("**Business Goal:** How much unique reach do I have across owned marketing channels?")

    channel_percentage_fig = px.bar(
        x=channel_data["Categories"],
        y=channel_data["Unique Channel Reach (%)"],
        text=[f"{val}%" for val in channel_data["Unique Channel Reach (%)"]],
        labels={'x': "Category", 'y': "Reach (%)"},
        title="Unique Channel Reach (%)"
    )
    st.plotly_chart(channel_percentage_fig)

    st.subheader("CoreID Match and Reach")
    st.write("Highlights audience reach in Epsilon’s digital channels by showing match rates, actual reach, and performance percentages.")
    st.markdown("**Business Goal:** How much unique reach do I have in Epsilon’s digital channels?")

    col1, col2 = st.columns(2)
    with col1:
        match_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=data["coreid_match_reach"]["Match Rate (%)"],
            title={"text": "Match Rate (%)"},
            number={"suffix": "%"},
            gauge={"axis": {"range": [0, 100]}, "bar": {"color": "green"}},
        ))
        st.plotly_chart(match_gauge, use_container_width=True)
    with col2:
        reach_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=data["coreid_match_reach"]["Reach Rate (%)"],
            title={"text": "Reach Rate (%)"},
            number={"suffix": "%"},
            gauge={"axis": {"range": [0, 100]}, "bar": {"color": "green"}},
        ))
        st.plotly_chart(reach_gauge, use_container_width=True)


# Main App
def main():
    st.title("Identity Essentials Reporting")

    tab = st.sidebar.selectbox("Select a Tab:", ["Identity"])

    if tab == "Identity":
        display_identity_data()


if __name__ == "__main__":
    main()
