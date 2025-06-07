import streamlit as st
import os
from main import run_with_inputs


st.set_page_config(page_title="Resume Optimization System", layout="centered")
st.title("🧠 Resume Optimization System")

# User inputs
job_url = st.text_input("🔗 Enter the job URL (e.g., LinkedIn)")
company_name = st.text_input("🏢 Enter the company name")
resume_file = st.file_uploader("📄 Upload your resume (PDF)", type="pdf")

if st.button("🚀 Optimize Resume"):
    if not (job_url and company_name and resume_file):

        st.warning("Please complete all fields and upload your resume.")
    else:
        # Save uploaded resume to a temporary file
        resume_path = "temp_resume.pdf"
        with open(resume_path, "wb") as f:
            f.write(resume_file.read())

        # Run the AI agent system
        with st.spinner("Running AI agents... please wait."):
            run_with_inputs(job_url, company_name, resume_path)

        st.success("✅ Resume optimization complete!")

        # Show download options
        if os.path.exists("output/optimized_resume.md"):
            st.download_button(
                "📥 Download Optimized Resume",
                data=open("output/optimized_resume.md").read(),
                file_name="optimized_resume.md"
            )

        if os.path.exists("output/final_report.md"):
            st.download_button(
                "📥 Download Final Report",
                data=open("output/final_report.md").read(),
                file_name="final_report.md"
            )
