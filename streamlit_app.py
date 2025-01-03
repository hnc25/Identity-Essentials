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

# Streamlit Layout for Identity
def display_identity_data():
    st.subheader("Identity Reporting")
    st.write("The Identity Reporting Dashboard in Connect 2.0 provides clients with actionable insights into their audience universe and unique reach across various channels.")

    time_range = st.selectbox("Select Time Range:", ["1 Month", "3 Months", "6 Months"], index=0)
    data = get_identity_data(time_range)

    st.subheader("Total Profiles")
    st.markdown("**Business Goal:** How many unique individuals and households exist in my universe?")
    
    total_profiles = data["total_profiles"]
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
            <div style="border: 1px solid lightgray; border-radius: 5px; padding: 10px; background-color: #f9f9f9; text-align: center;">
                <strong>Total Profiles</strong><br>
                <span style="font-size: 24px;">{total_profiles['Total Profiles']:,}</span>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <div style="border: 1px solid lightgray; border-radius: 5px; padding: 10px; background-color: #f9f9f9; text-align: center;">
                <strong>Matched csCoreID</strong><br>
                <span style="font-size: 24px;">{total_profiles['Matched csCoreID']:,}</span>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
            <div style="border: 1px solid lightgray; border-radius: 5px; padding: 10px; background-color: #f9f9f9; text-align: center;">
                <strong>Matched csHHId</strong><br>
                <span style="font-size: 24px;">{total_profiles['Matched csHHId']:,}</span>
            </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
            <div style="border: 1px solid lightgray; border-radius: 5px; padding: 10px; background-color: #f9f9f9; text-align: center;">
                <strong>Duplicate Records (%)</strong><br>
                <span style="font-size: 24px;">{total_profiles['Duplicate Records (%)']}%</span>
            </div>
        """, unsafe_allow_html=True)

    # Remaining sections of Identity Reporting...
    # (Add charts and other components here)


# Streamlit Layout for Hygiene
def display_hygiene_data():
    st.subheader("Hygiene Reporting")
    st.write("The Hygiene Summary dashboard evaluates the validation, enrichment, and standardization of customer contact data, including email, phone, ZIP/Name, and address records. It enables users to monitor data quality, track corrections and standardizations, and ensure completed contact records for improved engagement.")

    time_range = st.selectbox("Select Time Range:", ["1 Month", "3 Months", "6 Months"], index=0, key="hygiene")
    data = get_hygiene_data(time_range)

    st.subheader("Contact Complete")
    st.write("How many records were completed (validated, matched, or enriched) across email, phone, ZIP/Name, and TAC data?")
    # Contact Complete Chart...
    # Add corrections and email standardization sections...


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
