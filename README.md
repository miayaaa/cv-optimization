# Resume Optimization Agent

This project helps job seekers automatically optimize their resumes for specific job postings.  
It analyzes job descriptions, evaluates resumes, researches target companies, and produces a tailored resume and interview report — all powered by AI agents.


![Resume Optimization System Architecture](docs/architecture-diagam.svg)

## Project Structure

```bash
resume-optimization-crew/
├── app.py                 # Streamlit UI for resume optimization
├── main.py                # Entry point to run the CrewAI pipeline
├── src/resume_crew/
│   ├── crew.py            # Defines agents and tasks
│   ├── models.py          # Output data models (Pydantic)
│   ├── config/            # YAML files for agents and tasks
│   └── tools/             # Custom tools (PDF reader, scraper, etc.)
├── output/                # AI-generated resume and report
└── README.md              # Project documentation
```

## 🧩 Core Components

### 👥 Agents
- **Resume Analyzer** – Analyzes the resume and provides suggestions
- **Job Analyzer** – Scrapes and analyzes job requirements
- **Company Researcher** – Gathers background info for interview prep
- **Resume Writer** – Generates an optimized resume in markdown
- **Report Generator** – Creates a summary report of all findings

### 📋 Tasks Workflow
1. **Analyze Job** – Extracts job requirements and evaluates candidate fit
2. **Optimize Resume** – Suggests improvements based on the job
3. **Research Company** – Gathers interview-relevant insights
4. **Generate Resume** – Writes a tailored resume
5. **Generate Report** – Compiles all insights and outputs


## 🔄 Data Flow

- **Input:** Job URL, company name, candidate resume (PDF)
- **Processing:** AI agents execute tasks sequentially
- **Output:** JSON files + markdown resume & report in `/output/`

## 🖥️ Streamlit App Interface
A simple web interface is provided via Streamlit, allowing users to upload their resume, enter a job link and company name, and download the results.

▶ How to Run
```bash
streamlit run app.py
```
### 📤 Features

- Upload your resume (PDF)
- Input job URL (e.g., LinkedIn posting)
- Enter target company name
- Click 🚀 Optimize Resume to run all agents
- Download:
    - optimized_resume.md
    - final_report.md

## 🛠 Tools Used

- `SerperDevTool` – Web search for company research
- `ScrapeWebsiteTool` – Scrapes job descriptions
- `PDFKnowledgeSource` – Reads and analyzes the resume PDF
- `CrewAI` – Coordinates task flow and agent orchestration

## 📌 Sample Outputs

- optimized_resume.md – Job-specific improved resume
- final_report.md – AI-generated suggestions, insights & summary
- JSON files – Structured results for further use
