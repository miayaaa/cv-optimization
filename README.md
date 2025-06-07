# Resume Optimization System

This project helps job seekers automatically optimize their resumes for specific job postings.  
It analyzes job descriptions, evaluates resumes, researches target companies, and produces a tailored resume and interview report — all powered by AI agents.


![Resume Optimization System Architecture](docs/architecture-diagam.svg)

## Project Structure

```bash
resume-optimization-crew/
│
├── main.py # Entry point: run the crew with job URL & company name
├── crew.py # Defines ResumeCrew (agents & tasks)
├── models.py # Pydantic models for structured outputs
├── config/ # Agent roles and task descriptions
├── tools/ # Custom tools (e.g. PDF reader, web scraper)
└── output/ # Generated markdown files and analysis
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


## 🛠 Tools Used

- `SerperDevTool` – Web search for company research
- `ScrapeWebsiteTool` – Scrapes job descriptions
- `PDFKnowledgeSource` – Reads and analyzes the resume PDF
- `CrewAI` – Coordinates task flow and agent orchestration

## 📌 Sample Outputs

- optimized_resume.md – Job-specific improved resume
- final_report.md – AI-generated suggestions, insights & summary
- JSON files – Structured results for further use
