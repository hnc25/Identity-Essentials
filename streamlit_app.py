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
        st.markdown(
            f"""
            <div style="background-color: #f9f9f9; padding: 15px; border-radius: 5px; text-align: center;">
                <h6 style="font-size: 14px;">Total Profiles</h6>
                <p style="font-size: 20px; font-weight: bold;">{total_profiles['Total Profiles']:,}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f"""
            <div style="background-color: #f9f9f9; padding: 15px; border-radius: 5px; text-align: center;">
                <h6 style="font-size: 14px;">Matched csCoreID</h6>
                <p style="font-size: 20px; font-weight: bold;">{total_profiles['Matched csCoreID']:,}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            f"""
            <div style="background-color: #f9f9f9; padding: 15px; border-radius: 5px; text-align: center;">
                <h6 style="font-size: 14px;">Matched csHHId</h6>
                <p style="font-size: 20px; font-weight: bold;">{total_profiles['Matched csHHId']:,}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col4:
        st.markdown(
            f"""
            <div style="background-color: #f9f9f9; padding: 15px; border-radius: 5px; text-align: center;">
                <h6 style="font-size: 14px;">Duplicate Records (%)</h6>
                <p style="font-size: 20px; font-weight: bold;">{total_profiles['Duplicate Records (%)']}%</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.subheader("Channel Distribution")
    st.markdown("**Business Goal:** How much unique reach exists across my owned marketing channels?")
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
    channel_percentage_fig = px.bar(
        x=channel_data["Categories"],
        y=channel_data["Unique Channel Reach (%)"],
        text=[f"{val}%" for val in channel_data["Unique Channel Reach (%)"]],
        labels={'x': "Category", 'y': "Reach (%)"},
        title="Unique Channel Reach (%)"
    )
    st.plotly_chart(channel_percentage_fig)

    st.subheader("CoreID Match and Reach")
    st.markdown("**Business Goal:** How much unique reach do I have in Epsilon’s digital channels?")
    col1, col2 = st.columns(2)
    with col1:
        match_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=data["coreid_match_reach"]["Match Rate (%)"],
            title={"text": "Match Rate (%)"},
            number={"suffix": "%", "font": {"size": 30}},
            gauge={"axis": {"range": [0, 100]}, "bar": {"color": "green"}},
        ))
        st.plotly_chart(match_gauge, use_container_width=True)
    with col2:
        reach_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=data["coreid_match_reach"]["Reach Rate (%)"],
            title={"text": "Reach Rate (%)"},
            number={"suffix": "%", "font": {"size": 30}},
            gauge={"axis": {"range": [0, 100]}, "bar": {"color": "green"}},
        ))
        st.plotly_chart(reach_gauge, use_container_width=True)


# Streamlit Layout for Hygiene
def display_hygiene_data():
    st.subheader("Hygiene Reporting")
    st.write("The Hygiene Summary dashboard evaluates the validation, enrichment, and standardization of customer contact data, including email, phone, ZIP/Name, and address records. It enables users to monitor data quality, track corrections and standardizations, and ensure completed contact records for improved engagement.")

    time_range = st.selectbox("Select Time Range:", ["1 Month", "3 Months", "6 Months"], index=0, key="hygiene")
    data = get_hygiene_data(time_range)

    st.subheader("Contact Complete")
    st.write("How many records were completed (validated, matched, or enriched) across email, phone, ZIP/Name, and Trade Area data?")

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
    st.write("What is the total number of records that were standardized, corrected, or moved?")

    corrections = data["corrections"]
    corrections_fig = px.pie(
        names=list(corrections.keys()),
        values=list(corrections.values()),
        title="Corrections",
        hole=0.4
    )
    corrections_fig.update_traces(textinfo='percent+label')
    st.plotly_chart(corrections_fig)

    st.subheader("Email Standardization")
    st.write("What is the total number of email records that were standardized?")

    email_data = data["email_standardization"]
    email_fig = px.pie(
        names=["Valid", "Invalid"],
        values=[email_data["Valid"], email_data["Invalid"]],
        title="Email Validation",
        hole=0.4
    )
    email_fig.update_traces(textinfo='percent+label')
    st.plotly_chart(email_fig)


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
        st.write(f"<div style='background-color: #f8f9fa; padding: 10px; text-align: center; border-radius: 5px;'><b>Total Profiles</b><br>{total_profiles['Total Profiles']:,}</div>", unsafe_allow_html=True)
    with col2:
        st.write(f"<div style='background-color: #f8f9fa; padding: 10px; text-align: center; border-radius: 5px;'><b>Matched csCoreID</b><br>{total_profiles['Matched csCoreID']:,}</div>", unsafe_allow_html=True)
    with col3:
        st.write(f"<div style='background-color: #f8f9fa; padding: 10px; text-align: center; border-radius: 5px;'><b>Matched csHHId</b><br>{total_profiles['Matched csHHId']:,}</div>", unsafe_allow_html=True)
    with col4:
        st.write(f"<div style='background-color: #f8f9fa; padding: 10px; text-align: center; border-radius: 5px;'><b>Duplicate Records (%)</b><br>{total_profiles['Duplicate Records (%)']}%</div>", unsafe_allow_html=True)

    st.subheader("Channel Distribution")
    st.markdown("**Business Goal:** How much unique reach exists across my owned marketing channels?")

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

    channel_percentage_fig = px.bar(
        x=channel_data["Categories"],
        y=channel_data["Unique Channel Reach (%)"],
        text=[f"{val}%" for val in channel_data["Unique Channel Reach (%)"]],
        labels={'x': "Category", 'y': "Reach (%)"},
        title="Unique Channel Reach (%)"
    )
    st.plotly_chart(channel_percentage_fig)

    st.subheader("CoreID Match and Reach")
    st.markdown("**Business Goal:** How much unique reach do I have in Epsilon’s digital channels?")

    col1, col2 = st.columns(2)
    with col1:
        match_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=data["coreid_match_reach"]["Match Rate (%)"],
            title={"text": "Match Rate (%)"},
            number={"suffix": "%", "font": {"size": 30}},
            gauge={"axis": {"range": [0, 100]}, "bar": {"color": "green"}},
        ))
        st.plotly_chart(match_gauge, use_container_width=True)
    with col2:
        reach_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=data["coreid_match_reach"]["Reach Rate (%)"],
            title={"text": "Reach Rate (%)"},
            number={"suffix": "%", "font": {"size": 30}},
            gauge={"axis": {"range": [0, 100]}, "bar": {"color": "green"}},
        ))
        st.plotly_chart(reach_gauge, use_container_width=True)


# Streamlit Layout for Hygiene
def display_hygiene_data():
    st.subheader("Hygiene Reporting")
    st.write("The Hygiene Summary dashboard evaluates the validation, enrichment, and standardization of customer contact data, including email, phone, ZIP/Name, and address records. It enables users to monitor data quality, track corrections and standardizations, and ensure completed contact records for improved engagement.")

    time_range = st.selectbox("Select Time Range:", ["1 Month", "3 Months", "6 Months"], index=0, key="hygiene")
    data = get_hygiene_data(time_range)

    st.subheader("Contact Complete")
    st.write("How many records were completed (validated, matched, or enriched) across email, phone, ZIP/Name, and Trade Area data?")

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
    st.write("What is the total number of records that were standardized, corrected, or moved?")

    corrections = data["corrections"]
    corrections_total = sum(corrections.values())
    corrections_fig = px.pie(
        names=list(corrections.keys()),
        values=list(corrections.values()),
        title="Corrections",
        hole=0.4
    )
    corrections_fig.update_traces(textinfo='percent+label')
    st.plotly_chart(corrections_fig)

    st.subheader("Email Standardization")
    st.write("What is the total number of email records that were standardized?")

    email_data = data["email_standardization"]
    email_fig = px.pie(
        names=["Valid", "Invalid"],
        values=[email_data["Valid"], email_data["Invalid"]],
        title="Email Validation",
        hole=0.4
    )
    email_fig.update_traces(textinfo='percent+label')
    st.plotly_chart(email_fig)


# Main App
def main():
    st.title("Identity Essentials Reporting")
    st.sidebar.header("Choose a report")
    tab = st.sidebar.radio("", ["Identity", "Hygiene"], index=0)

    if tab == "Identity":
        display_identity_data()
    elif tab == "Hygiene":
        display_hygiene_data()


if __name__ == "__main__":
    main()
