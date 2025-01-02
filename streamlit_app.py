from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go

# Initialize Dash app
app = Dash(__name__, suppress_callback_exceptions=True)

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

# Identity Layout
def get_identity_layout():
    return html.Div([
        html.H2("Identity Reporting", style={"textAlign": "center"}),
        html.P("This section reports the uniqueness of profiles managed within the Identity Essentials product.", style={"textAlign": "center"}),

        # Dropdown
        html.Label("Time Range:", style={"fontWeight": "bold"}),
        dcc.Dropdown(
            id="identity-time-range",
            options=[
                {"label": "1 Month", "value": "1 Month"},
                {"label": "3 Months", "value": "3 Months"},
                {"label": "6 Months", "value": "6 Months"},
            ],
            value="1 Month",
            style={"width": "50%", "marginBottom": "20px"}
        ),

        # Totals Section
        html.Div(id="identity-total-profiles-cards", style={"display": "flex", "justifyContent": "space-around", "marginBottom": "20px"}),

        # Channel Distribution
        html.H3("Channel Distribution"),
        html.P("This section shows the unique reach across marketing channels."),
        dcc.Graph(id="identity-channel-bar"),

        # Unique Channel Reach
        html.H3("Unique Channel Reach"),
        html.P("Displays the percentage reach of unique individuals across channels."),
        dcc.Graph(id="identity-channel-percentage-bar"),

        # CoreID Match and Reach Gauges
        html.H3("CoreID Match and Reach"),
        html.P("Shows the match and reach rates in digital channels."),
        html.Div([
            dcc.Graph(id="identity-coreid-match-gauge", style={"display": "inline-block", "width": "48%"}),
            dcc.Graph(id="identity-coreid-reach-gauge", style={"display": "inline-block", "width": "48%"}),
        ]),
    ])

# Hygiene Layout
def get_hygiene_layout():
    return html.Div([
        html.H2("Hygiene Reporting", style={"textAlign": "center"}),
        html.P("This section evaluates the validation, enrichment, and standardization of customer contact data.", style={"textAlign": "center"}),

        # Dropdown
        html.Label("Time Range:", style={"fontWeight": "bold"}),
        dcc.Dropdown(
            id="hygiene-time-range",
            options=[
                {"label": "1 Month", "value": "1 Month"},
                {"label": "3 Months", "value": "3 Months"},
                {"label": "6 Months", "value": "6 Months"},
            ],
            value="1 Month",
            style={"width": "50%", "marginBottom": "20px"}
        ),

        # Contact Complete
        html.H3("Contact Complete"),
        html.P("Shows the number of records completed using address, email, and phone."),
        dcc.Graph(id="hygiene-contact-complete-bar"),

        # Corrections Donut Chart
        html.H3("Standardization and Corrections"),
        html.P("Displays records that were standardized, corrected, or moved."),
        dcc.Graph(id="hygiene-corrections-pie"),

        # Email Validation Pie Chart
        html.H3("Email Standardization"),
        html.P("Shows the status of standardized email records."),
        dcc.Graph(id="hygiene-email-validation-pie"),
    ])

# Main Layout
app.layout = html.Div([
    html.H1("Combined Identity & Hygiene Dashboard", style={"textAlign": "center"}),

    dcc.Tabs(id="tabs", value="identity", children=[
        dcc.Tab(label="Identity", value="identity"),
        dcc.Tab(label="Hygiene", value="hygiene"),
    ]),

    html.Div(id="tab-content")
])

# Tab Switching Callback
@app.callback(
    Output("tab-content", "children"),
    Input("tabs", "value")
)
def render_tab_content(tab):
    if tab == "identity":
        return get_identity_layout()
    elif tab == "hygiene":
        return get_hygiene_layout()

# Identity Callback
@app.callback(
    [
        Output("identity-total-profiles-cards", "children"),
        Output("identity-channel-bar", "figure"),
        Output("identity-channel-percentage-bar", "figure"),
        Output("identity-coreid-match-gauge", "figure"),
        Output("identity-coreid-reach-gauge", "figure"),
    ],
    Input("identity-time-range", "value"),
)
def update_identity(time_range):
    data = get_identity_data(time_range)

    # Totals Section
    total_profiles = data["total_profiles"]
    cards = [
        html.Div([
            html.H4(metric, style={"textAlign": "center"}),
            html.P(f"{value:,}" if "Duplicate" not in metric else f"{value}%", style={"textAlign": "center"})
        ], style={"padding": "20px", "border": "1px solid #ccc", "borderRadius": "5px", "margin": "10px", "width": "23%"})
        for metric, value in total_profiles.items()
    ]

    # Channel Bar Chart
    channel_data = data["channel_distribution"]
    channel_bar_fig = px.bar(
        x=channel_data["Categories"],
        y=channel_data["Total Identifiers"],
        text=[f"{v:,}" for v in channel_data["Total Identifiers"]],
        title="Total Identifiers"
    )
    channel_bar_fig.update_traces(textposition="outside")

    # Unique Channel Reach Bar Chart
    channel_percentage_fig = px.bar(
        x=channel_data["Categories"],
        y=channel_data["Unique Channel Reach (%)"],
        text=[f"{v}%" for v in channel_data["Unique Channel Reach (%)"]],
        title="Unique Channel Reach (%)"
    )
    channel_percentage_fig.update_traces(textposition="outside")

    # Match and Reach Gauges
    match_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=data["coreid_match_reach"]["Match Rate (%)"],
        title={"text": "Match Rate (%)"},
        number={"suffix": "%"},
        gauge={"axis": {"range": [0, 100]}, "bar": {"color": "green"}}
    ))
    reach_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=data["coreid_match_reach"]["Reach Rate (%)"],
        title={"text": "Reach Rate (%)"},
        number={"suffix": "%"},
        gauge={"axis": {"range": [0, 100]}, "bar": {"color": "green"}}
    ))

    return cards, channel_bar_fig, channel_percentage_fig, match_gauge, reach_gauge

# Hygiene Callback
@app.callback(
    [
        Output("hygiene-contact-complete-bar", "figure"),
        Output("hygiene-corrections-pie", "figure"),
        Output("hygiene-email-validation-pie", "figure"),
    ],
    Input("hygiene-time-range", "value"),
)
def update_hygiene(time_range):
    data = get_hygiene_data(time_range)

    # Contact Complete Bar Chart
    contact_data = data["contact_complete"]
    contact_fig = px.bar(
        x=list(contact_data.keys()),
        y=list(contact_data.values()),
        text=[f"{v:,}" for v in contact_data.values()],
        title="Contact Complete"
    )
    contact_fig.update_traces(textposition="outside")

    # Corrections Donut Chart
    corrections = data["corrections"]
    corrections_fig = px.pie(
        names=list(corrections.keys()),
        values=list(corrections.values()),
        title="Corrections"
    )
    corrections_fig.update_traces(hole=0.4, textinfo="percent+label")

    # Email Validation Pie Chart
    email_data = data["email_standardization"]
    email_fig = px.pie(
        names=["Valid", "Invalid"],
        values=[email_data["Valid"], email_data["Invalid"]],
        title="Email Validation"
    )
    email_fig.update_traces(textinfo="percent+label")

    return contact_fig, corrections_fig, email_fig

# Run the App
if __name__ == "__main__":
    app.run_server(debug=True)
