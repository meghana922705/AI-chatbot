import streamlit as st

st.title("Job Application Form")


name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")


qualification = st.selectbox(
    "Qualification",
    ["10th", "Intermediate", "B.Tech", "B.Sc", "MCA", "MBA"]
)

skills = st.multiselect(
    "Skills",
    ["HTML", "CSS", "JavaScript", "Python", "Java", "SQL"]
)

# Resume
resume = st.file_uploader("Upload Resume", type=["pdf", "docx"])

# Status Component
status = st.selectbox(
    "Status",
    ["Applied", "Under Review", "Shortlisted", "Selected", "Rejected"]
)

# Message Component
message = st.text_area("Message", placeholder="Enter your message")

# Submit
if st.button("Submit Application"):

    if name and email and phone:
        st.success("Application submitted successfully!")

        st.write("### Application Details")
        st.write("Name:", name)
        st.write("Email:", email)
        st.write("Phone:", phone)
        st.write("Qualification:", qualification)
        st.write("Skills:", ", ".join(skills))
        st.write("Status:", status)
        st.write("Message:", message)

        if resume:
            st.write("Resume:", resume.name)

    else:
        st.error("Please fill in all required fields.")
