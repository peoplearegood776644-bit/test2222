import streamlit as st

# Page Configuration
st.set_page_config(page_title="Awais Ahmad - Test App", page_icon="📝")

# Your Required Identification
st.title("📋 Test Application (Google Form Clone)")
st.subheader(f"Developed by: Awais Ahmad")
st.write(f"**Roll Number:** 25-ME-108")
st.divider()

# Creating the Form
with st.form("test_form"):
    st.markdown("### Please fill out the details below")
    
    # Text input (Single line)
    user_name = st.text_input("Full Name")
    
    # Multiple Choice (Radio Buttons)
    department = st.radio(
        "Select your Department:",
        ["Mechanical Engineering", "Civil Engineering", "Electrical Engineering", "Software Engineering"]
    )
    
    # Checkbox for multiple selections
    skills = st.multiselect(
        "Select your Skills:",
        ["Python", "CAD", "Project Management", "Data Analysis"]
    )
    
    # Date Picker
    submission_date = st.date_input("Today's Date")
    
    # Feedback (Paragraph text)
    comments = st.text_area("Any additional comments?")

    # Submit Button - Required for every st.form
    submitted = st.form_submit_button("Submit Response")

# Actions after submission
if submitted:
    if user_name:
        st.success(f"Thank you, {user_name}! Your response has been recorded.")
        st.json({
            "Name": user_name,
            "Department": department,
            "Skills": skills,
            "Date": str(submission_date),
            "Comments": comments
        })
    else:
        st.error("Please enter your name before submitting.")
