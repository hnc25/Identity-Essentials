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


# Hygiene Data
def get_hygiene_data(time_range):
    if time_range == "1 Month":
        return {
            "contact_complete": {
                "Address": 45000,
                "Email": 36000,
                "Phone": 24000,
            },
            "corrections": {
                "NCOA": 5000,
                "PCOA": 2000,
                "PCA": 1000,
            },
            "email_standardization": {
                "Valid": 90000,
                "Invalid": 4000,
            }
        }
    elif time_range == "3 Months":
        return {
            "contact_complete": {
                "Address": 135000,
                "Email": 108000,
                "Phone": 72000,
            },
            "corrections": {
                "NCOA": 15000,
                "PCOA": 6000,
                "PCA": 3000,
            },
            "email_standardization": {
                "Valid": 270000,
                "Invalid": 12000,
            }
        }
    elif time_range == "6 Months":
        return {
            "contact_complete": {
                "Address": 270000,
                "Email": 216000,
                "Phone": 144000,
            },
            "corrections": {
                "NCOA": 30000,
                "PCOA": 12000,
                "PCA": 6000,
            },
            "email_standardization": {
                "Valid": 540000,
                "Invalid": 24000,
            }
        }


# Streamlit Layout for Identity
def display_identity_data():
    st.subheader("Identity Reporting")
    st.write("The Identity Reporting Dashboard provides actionable insights into the audience universe and reach. Select a time range to dynamically update metrics and visualizations.")

    time_range = st.selectbox("Select Time Range:", ["1 Month", "3 Months", "6 Months"], index=0)
    data = get_identity_data(time_range)

    # Total Profiles Section with Table
    st.subheader("Total Profiles")
    st.write("Displays audience profiles, matched records, and duplication.")
    st.markdown("**Business Goal:** How many unique individuals and households exist in my universe?")
    total_profiles = pd.DataFrame([data["total_profiles"]])
    st.table(total_profiles)

    # Channel Distribution
    st.subheader("Channel Distribution")
    st.write("Breaks down total audience identifiers by categories.")
    st.markdown("**Business Goal:** How much unique reach exists across channels?")
    channel_data = data["channel_distribution"]
    channel_bar_fig = px.bar(
        x=channel_data["Categories"],
        y=channel_data["Total Identifiers"],
        title="Total Identifiers by Channel",
        text_auto=True
    )
    st.plotly_chart(channel_bar_fig)

    # CoreID Match & Reach
    st.subheader("CoreID Match and Reach")
    st.write("Shows match and reach performance in digital channels.")
    st.markdown("**Business Goal:** How much unique reach do I have in digital channels?")
    col1, col2 = st.columns(2)
    col1.metric("Match Rate (%)", f"{data['coreid_match_reach']['Match Rate (%)']}%")
    col2.metric("Reach Rate (%)", f"{data['coreid_match_reach']['Reach Rate (%)']}%")


# Streamlit Layout for Hygiene
def display_hygiene_data():
    st.subheader("Hygiene Reporting")
    st.write("The Hygiene Dashboard evaluates contact data validation and enrichment for better engagement.")

    time_range = st.selectbox("Select Time Range:", ["1 Month", "3 Months", "6 Months"], index=0)
    data = get_hygiene_data(time_range)

    # Contact Complete
    st.subheader("Contact Complete")
    st.write("Tracks completed records using Address, Email, and Phone.")
    st.markdown("**Business Goal:** How complete is my contact data?")
    contact_data = pd.DataFrame(data["contact_complete"], index=["Values"]).T
    st.table(contact_data)

    # Corrections Donut Chart
    st.subheader("Standardization and Corrections")
    st.write("Summarizes standardized or corrected records.")
    corrections = data["corrections"]
    corrections_fig = px.pie(
        names=corrections.keys(),
        values=corrections.values(),
        title="Corrections"
    )
    st.plotly_chart(corrections_fig)

    # Email Validation
    st.subheader("Email Standardization")
    st.write("Tracks validation of email records.")
    email_data = data["email_standardization"]
    email_fig = px.pie(
        names=["Valid", "Invalid"],
        values=[email_data["Valid"], email_data["Invalid"]],
        title="Email Validation"
    )
    st.plotly_chart(email_fig)


# Main App
def main():
    st.title("Identity Essentials Reporting")

    tab = st.sidebar.selectbox("Select a Tab:", ["Identity", "Hygiene"])

    if tab == "Identity":
        display_identity_data()
    elif tab == "Hygiene":
        display_hygiene_data()


if __name__ == "__main__":
    main()
