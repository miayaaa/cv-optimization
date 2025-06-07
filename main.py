#!/usr/bin/env python
import sys
import warnings

from resume_crew.crew import ResumeCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run_with_inputs(job_url: str, company_name: str, resume_path: str):
    """
    Run the resume optimization crew with custom inputs.
    """
    inputs = {
        "job_url": job_url,
        "company_name": company_name,
        "resume_path": resume_path
    }
    ResumeCrew().crew().kickoff(inputs=inputs)


def run():
    # Default local testing
    run_with_inputs(
        job_url="https://www.linkedin.com/jobs/view/artificial-intelligence-engineer-at-spark-new-zealand-4230208966/",
        company_name="Spark New Zealand",
        resume_path="resume.pdf"
    )


if __name__ == "__main__":
    run()
