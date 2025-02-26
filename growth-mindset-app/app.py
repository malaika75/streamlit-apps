import streamlit as st
import os
import pandas as pd

st.title("📊 CSV Generator & Viewer")

# Ensure folder exists
os.makedirs("csv_data", exist_ok=True)

# Categories Dropdown
st.write("### 📂 Choose a Category to Create a CSV Format")

categories = {
    "Select a Category": [],
    "E-commerce": ["Product Name", "Category", "Price", "Stock Quantity", "Rating", "Brand Name", "Return Policy"],
    "Personal Profile": ["Full Name", "Date of Birth", "Email", "Phone Number", "Education", "Skills", "LinkedIn Profile"],
    "Real Estate": ["Property Title", "Location", "Price", "Size", "Bedrooms", "Bathrooms", "Parking Available"],
    "Job Listings": ["Company Name", "Job Title", "Location", "Salary", "Job Type", "Experience Required", "Application Link"],
    "Event Management": ["Event Name", "Date & Time", "Venue", "Ticket Price", "Organizer Contact", "Guest List", "Entertainment Details"]
}

selected_category = st.selectbox("🔽 Choose Category", list(categories.keys()), index=0)

# Show Fields Only If a Category is Selected
if selected_category != "Select a Category":
    st.write(f"### 🏷️ Fill Details for {selected_category}")

    data = {}
    for field in categories[selected_category]:
        data[field] = st.text_input(f"Enter {field}")

    # Save CSV
    if st.button("💾 Save & Download CSV"):
        csv_filename = f"{selected_category.lower().replace(' ', '_')}.csv"
        csv_path = os.path.join("csv_data", csv_filename)

        if os.path.exists(csv_path):
            df_existing = pd.read_csv(csv_path)
            df_new = pd.DataFrame([data])
            df_final = pd.concat([df_existing, df_new], ignore_index=True)
        else:
            df_final = pd.DataFrame([data])

        df_final.to_csv(csv_path, index=False)

        with open(csv_path, "rb") as f:
            st.download_button("📥 Download CSV", f, file_name=csv_filename)

# CSV Visualization Feature
st.write("### 📊 View Existing CSV Data")
uploaded_csv = st.file_uploader("Upload a CSV file to view", type=["csv"])

if uploaded_csv is not None:
    df = pd.read_csv(uploaded_csv)
    st.write("#### CSV Data Preview")
    st.dataframe(df)



















