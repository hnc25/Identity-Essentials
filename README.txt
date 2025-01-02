### **Requirements Document: Final Update for the Combined Identity & Hygiene Dashboard**

---

#### **Project Overview**
The **Combined Identity & Hygiene Dashboard** is a fully interactive and dynamic reporting tool built using Dash (Python). It includes two primary sections: **Identity** and **Hygiene**, with features that dynamically update based on the selected date range. This document outlines the requirements and updates made during the final iteration.

---

### **1. Identity Tab**

#### **Functional Requirements**
- **Time Range Dropdown**:
  - Allow users to filter data by the following date ranges:
    - **1 Month**
    - **3 Months**
    - **6 Months**

- **Key Metrics Section**:
  - Display four cards dynamically showing:
    - Total Profiles (e.g., 25,000).
    - Matched csCoreID.
    - Matched csHHId.
    - Duplicate Records (%).

- **Channel Distribution Chart**:
  - Bar chart displaying the **Total Identifiers** across three categories: Address, Email, and Phone.
  - Include values above the bars for clarity (e.g., 190,000).

- **Unique Channel Reach Chart**:
  - Bar chart showing the **percentage reach** for each channel (Address, Email, Phone).
  - Values displayed above each bar (e.g., 85%).

- **CoreID Match and Reach Odometers**:
  - Two odometer charts to display:
    - **Match Rate (%)**.
    - **Reach Rate (%)**.
  - Include a **% suffix** in the odometer numbers.

#### **Dynamic Behavior**
- All metrics, charts, and odometers update dynamically based on the selected time range.

---

### **2. Hygiene Tab**

#### **Functional Requirements**
- **Time Range Dropdown**:
  - Allow users to filter data by the following date ranges:
    - **1 Month**
    - **3 Months**
    - **6 Months**

- **Contact Complete Chart**:
  - Bar chart showing the total number of records completed using Address, Email, and Phone.
  - Values displayed above each bar (e.g., 45,000).

- **Corrections Donut Chart**:
  - Donut chart displaying the proportion of records corrected by:
    - NCOA.
    - PCOA.
    - PCA.
  - Percentages (e.g., "62.5%") displayed on the chart dynamically.

- **Email Validation Pie Chart**:
  - Pie chart displaying the proportions of:
    - **Valid** emails.
    - **Invalid** emails.
  - Dynamically display percentages (e.g., "95.7% Valid").

#### **Dynamic Behavior**
- All charts update dynamically based on the selected time range.

---

### **3. Shared Requirements**

#### **User Experience Enhancements**
- **Commas in Numbers**:
  - Format large numbers with commas for better readability (e.g., 45000 → 45,000).

- **Percentage Formatting**:
  - Display **% suffix** for all relevant numbers, including odometer values.

- **Descriptive Headers and Subsections**:
  - Include descriptive headers and subsections for both tabs to clearly indicate the purpose of each chart or metric.

#### **Tabs and Navigation**
- Two main tabs are available for navigation:
  - **Identity**: Displays identity-related metrics and charts.
  - **Hygiene**: Displays hygiene-related metrics and charts.
- Tabs are accessible via the **dcc.Tabs** component.

---

### **4. Callback Requirements**

#### **Identity Callback**
- Dynamically update the following components based on the selected time range:
  - Total Profiles cards.
  - Channel Distribution bar chart.
  - Unique Channel Reach bar chart.
  - CoreID Match and Reach odometers.

#### **Hygiene Callback**
- Dynamically update the following components based on the selected time range:
  - Contact Complete bar chart.
  - Corrections donut chart.
  - Email Validation pie chart.

---

### **5. Technical Requirements**

- **Framework**: Dash (Python).
- **Dynamic Updates**:
  - All charts and metrics must be driven by dynamic callbacks using the selected date range.
- **Code Structure**:
  - Maintain separate layouts and callbacks for each tab to ensure modularity and scalability.

---

### **6. Final Deliverables**
- Fully functional **Combined Identity & Hygiene Dashboard** with all features listed above.
- All dynamic behaviors implemented as described.
- The dashboard is user-friendly, visually clear, and supports seamless navigation between tabs.

---

This document outlines all updates made during the last iteration. Let me know if you need any additional details or further enhancements! 😊