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
    st.header("Identity Essentials Reporting")
    st.write("This section reports the uniqueness of profiles managed within the Identity Essentials product.")

    time_range = st.selectbox("Select Time Range:", ["1 Month", "3 Months", "6 Months"], index=0)
    data = get_identity_data(time_range)

    st.subheader("Total Profiles")
    st.write("This section shows the key metrics for total profiles.")

    total_profiles = data["total_profiles"]
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Profiles", f"{total_profiles['Total Profiles']:,}")
    col2.metric("Matched csCoreID", f"{total_profiles['Matched csCoreID']:,}")
    col3.metric("Matched csHHId", f"{total_profiles['Matched csHHId']:,}")
    col4.metric("Duplicate Records (%)", f"{total_profiles['Duplicate Records (%)']}%")

    st.subheader("Channel Distribution")
    st.write("Bar chart showing total identifiers across different categories.")

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
    st.write("Displays the percentage reach for each channel.")

    channel_percentage_fig = px.bar(
        x=channel_data["Categories"],
        y=channel_data["Unique Channel Reach (%)"],
        text=[f"{val}%" for val in channel_data["Unique Channel Reach (%)"]],
        labels={'x': "Category", 'y': "Reach (%)"},
        title="Unique Channel Reach (%)"
    )
    st.plotly_chart(channel_percentage_fig)

    st.subheader("CoreID Match and Reach")
    st.write("Displays match rate and reach rate as odometers.")

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


# Streamlit Layout for Hygiene
def display_hygiene_data():
    st.header("Hygiene Reporting")
    st.write("This section evaluates the validation, enrichment, and standardization of customer contact data.")

    time_range = st.selectbox("Select Time Range:", ["1 Month", "3 Months", "6 Months"], index=0, key="hygiene")
    data = get_hygiene_data(time_range)

    st.subheader("Contact Complete")
    st.write("Shows the total number of records completed using Address, Email, and Phone.")

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
    st.write("Displays records that were standardized or corrected.")

    corrections = data["corrections"]
    corrections_fig = px.pie(
        names=list(corrections.keys()),
        values=list(corrections.values()),
        title="Corrections"
    )
    st.plotly_chart(corrections_fig)

    st.subheader("Email Standardization")
    st.write("Shows the validation status of email records.")

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
