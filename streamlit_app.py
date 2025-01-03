import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

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
                "NCOA": 5500,
                "PCOA": 2200,
                "PCA": 1100,
            },
            "email_standardization": {
                "Valid": 90500,
                "Invalid": 4500,
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
                "NCOA": 15500,
                "PCOA": 6200,
                "PCA": 3100,
            },
            "email_standardization": {
                "Valid": 270800,
                "Invalid": 12400,
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
                "NCOA": 30300,
                "PCOA": 12500,
                "PCA": 6100,
            },
            "email_standardization": {
                "Valid": 540500,
                "Invalid": 24600,
            }
        }

# Identity Reporting
def display_identity_data():
    st.subheader("Identity Reporting")
    st.write("The Identity Reporting Dashboard in Connect 2.0 provides clients with actionable insights into their audience universe and unique reach across various channels.")

    time_range = st.selectbox("Select Time Range:", ["1 Month", "3 Months", "6 Months"], index=0, key="identity")
    data = get_identity_data(time_range)

    total_profiles = data["total_profiles"]

    # Boxed-out metrics with uniform size and grayed-out background
    st.markdown(
        """
        <style>
        .metric-box {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            background-color: #f8f9fa;
            border: 1px solid #ddd;
            border-radius: 10px;
            width: 200px;
            height: 120px;
            padding: 10px;
            margin: 5px;
            text-align: center;
        }
        .metric-box .metric-title {
            font-weight: bold;
            font-size: 1.2em;
            margin-bottom: 5px;
        }
        .metric-box .metric-value {
            font-size: 1.5em;
            color: #333;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-title">Total Profiles</div>
                <div class="metric-value">{total_profiles['Total Profiles']:,}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-title">Matched csCoreID</div>
                <div class="metric-value">{total_profiles['Matched csCoreID']:,}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-title">Matched csHHId</div>
                <div class="metric-value">{total_profiles['Matched csHHId']:,}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col4:
        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-title">Duplicate Records (%)</div>
                <div class="metric-value">{total_profiles['Duplicate Records (%)']}%</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Charts for Identity
    st.subheader("Channel Distribution")
    channel_data = data["channel_distribution"]
    channel_bar_fig = px.bar(
        x=channel_data["Categories"],
        y=channel_data["Total Identifiers"],
        text=[f"{v:,}" for v in channel_data["Total Identifiers"]],
        labels={'x': "Category", 'y': "Total Identifiers"},
        title="Total Identifiers by Channel"
    )
    channel_bar_fig.update_traces(textposition="outside")
    st.plotly_chart(channel_bar_fig)

    st.subheader("Unique Channel Reach (%)")
    unique_channel_fig = px.bar(
        x=channel_data["Categories"],
        y=channel_data["Unique Channel Reach (%)"],
        text=[f"{v}%" for v in channel_data["Unique Channel Reach (%)"]],
        labels={'x': "Category", 'y': "Reach (%)"},
        title="Unique Channel Reach (%)"
    )
    unique_channel_fig.update_traces(textposition="outside")
    st.plotly_chart(unique_channel_fig)

    st.subheader("CoreID Match and Reach")
    match_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=data["coreid_match_reach"]["Match Rate (%)"],
        title={"text": "Match Rate (%)"},
        gauge={"axis": {"range": [0, 100]}}
    ))
    reach_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=data["coreid_match_reach"]["Reach Rate (%)"],
        title={"text": "Reach Rate (%)"},
        gauge={"axis": {"range": [0, 100]}}
    ))
    st.plotly_chart(match_gauge)
    st.plotly_chart(reach_gauge)

# Hygiene Reporting
def display_hygiene_data():
    st.subheader("Hygiene Reporting")
    st.write("The Hygiene Summary dashboard evaluates the validation, enrichment, and standardization of customer contact data, including email, phone, ZIP/Name, and address records. It enables users to monitor data quality, track corrections and standardizations, and ensure completed contact records for improved engagement.")

    time_range = st.selectbox("Select Time Range:", ["1 Month", "3 Months", "6 Months"], index=0, key="hygiene")
    data = get_hygiene_data(time_range)

    st.subheader("Contact Complete")
    contact_data = data["contact_complete"]
    contact_fig = px.bar(
        x=list(contact_data.keys()),
        y=list(contact_data.values()),
        text=[f"{val:,}" for val in contact_data.values()],
        labels={'x': "Category", 'y': "Records"},
        title="Contact Complete"
    )
    st.plotly_chart(contact_fig)

    st.subheader("Standardization and Corrections")
    corrections = data["corrections"]
    corrections_fig = px.pie(
        names=list(corrections.keys()),
        values=list(corrections.values()),
        title="Corrections"
    )
    corrections_fig.update_traces(textinfo='percent+label')
    st.plotly_chart(corrections_fig)

    st.subheader("Email Standardization")
    email_data = data["email_standardization"]
    email_fig = px.pie(
        names=["Valid", "Invalid"],
        values=[email_data["Valid"], email_data["Invalid"]],
        title="Email Validation"
    )
    email_fig.update_traces(textinfo='percent+label')
    st.plotly_chart(email_fig)

# Main App
def main():
    st.title("Identity Essentials Reporting")

    tab = st.sidebar.selectbox("Select a Tab:", ["Identity Reporting", "Hygiene Reporting"])

    if tab == "Identity Reporting":
        display_identity_data()
    elif tab == "Hygiene Reporting":
        display_hygiene_data()

if __name__ == "__main__":
    main()
