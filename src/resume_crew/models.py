from typing import List, Dict, Optional
from pydantic import BaseModel, Field


class SkillScore(BaseModel):
    skill_name: str = Field(description="Name of the skill being scored")
    required: bool = Field(
        description="Whether this skill is required or nice-to-have")
    match_level: float = Field(
        ge=0.0, le=1.0, description="How well the candidate's experience matches (0–1)")
    years_experience: Optional[float] = Field(
        default=None,
        description="Years of experience with this skill"
    )
    context_score: float = Field(
        default=0.5,
        ge=0.0,
        le=1.0,
        description="How relevant the skill usage context is to the job requirements"
    )


class JobMatchScore(BaseModel):
    overall_match: float = Field(
        ge=0.0, le=100.0, description="Overall match percentage (0–100)")
    technical_skills_match: float = Field(
        ge=0.0, le=100.0, description="Technical skills match percentage")
    soft_skills_match: float = Field(
        ge=0.0, le=100.0, description="Soft skills match percentage")
    experience_match: float = Field(
        ge=0.0, le=100.0, description="Experience level match percentage")
    education_match: float = Field(
        ge=0.0, le=100.0, description="Education requirements match percentage")
    industry_match: float = Field(
        ge=0.0, le=100.0, description="Industry experience match percentage")

    skill_details: List[SkillScore] = Field(
        default_factory=list,
        description="Detailed scoring for each skill"
    )
    strengths: List[str] = Field(
        default_factory=list,
        description="List of areas where candidate exceeds requirements"
    )
    gaps: List[str] = Field(
        default_factory=list,
        description="List of areas needing improvement"
    )
    scoring_factors: Dict[str, float] = Field(
        default_factory=lambda: {
            "technical_skills": 0.35,
            "soft_skills": 0.20,
            "experience": 0.25,
            "education": 0.10,
            "industry": 0.10
        },
        description="Weights used for different scoring components"
    )


class JobRequirements(BaseModel):
    technical_skills: List[str] = Field(
        description="List of required technical skills",
        default_factory=list
    )
    soft_skills: List[str] = Field(
        description="List of required soft skills",
        default_factory=list
    )
    experience_requirements: List[str] = Field(
        description="List of experience requirements",
        default_factory=list
    )
    key_responsibilities: List[str] = Field(
        description="List of key job responsibilities",
        default_factory=list
    )
    education_requirements: List[str] = Field(
        description="List of education requirements",
        default_factory=list
    )
    nice_to_have: List[str] = Field(
        description="List of preferred but not required skills",
        default_factory=list
    )
    job_title: str = Field(
        description="Official job title",
        default=""
    )
    department: Optional[str] = Field(
        description="Department or team within the company",
        default=None
    )
    reporting_structure: Optional[str] = Field(
        description="Who this role reports to and any direct reports",
        default=None
    )
    job_level: Optional[str] = Field(
        description="Level of the position (e.g., Entry, Senior, Lead)",
        default=None
    )
    location_requirements: Dict[str, str] = Field(
        description="Location details including remote/hybrid options",
        default_factory=dict
    )
    work_schedule: Optional[str] = Field(
        description="Expected work hours and schedule flexibility",
        default=None
    )
    travel_requirements: Optional[str] = Field(
        description="Expected travel frequency and scope",
        default=None
    )
    compensation: Dict[str, str] = Field(
        description="Salary range and compensation details if provided",
        default_factory=dict
    )
    benefits: List[str] = Field(
        description="List of benefits and perks",
        default_factory=list
    )
    tools_and_technologies: List[str] = Field(
        description="Specific tools, software, or technologies used",
        default_factory=list
    )
    industry_knowledge: List[str] = Field(
        description="Required industry-specific knowledge",
        default_factory=list
    )
    certifications_required: List[str] = Field(
        description="Required certifications or licenses",
        default_factory=list
    )
    security_clearance: Optional[str] = Field(
        description="Required security clearance level if any",
        default=None
    )
    team_size: Optional[str] = Field(
        description="Size of the immediate team",
        default=None
    )
    key_projects: List[str] = Field(
        description="Major projects or initiatives mentioned",
        default_factory=list
    )
    cross_functional_interactions: List[str] = Field(
        description="Teams or departments this role interacts with",
        default_factory=list
    )
    career_growth: List[str] = Field(
        description="Career development and growth opportunities",
        default_factory=list
    )
    training_provided: List[str] = Field(
        description="Training or development programs offered",
        default_factory=list
    )
    diversity_inclusion: Optional[str] = Field(
        description="D&I statements or requirements",
        default=None
    )
    company_values: List[str] = Field(
        description="Company values mentioned in the job posting",
        default_factory=list
    )
    job_url: str = Field(
        description="URL of the job posting",
        default=""
    )
    posting_date: Optional[str] = Field(
        description="When the job was posted",
        default=None
    )
    application_deadline: Optional[str] = Field(
        description="Application deadline if specified",
        default=None
    )
    special_instructions: List[str] = Field(
        description="Any special application instructions or requirements",
        default_factory=list
    )
    match_score: JobMatchScore = Field(
        description="Detailed scoring of how well the candidate matches the job requirements",
        default_factory=JobMatchScore
    )
    score_explanation: List[str] = Field(
        description="Detailed explanation of how scores were calculated",
        default_factory=list
    )


class ResumeOptimization(BaseModel):
    content_suggestions: List[Dict[str, str]] = Field(
        description="List of content optimization suggestions with 'before' and 'after' examples",
        default_factory=list
    )
    skills_to_highlight: List[str] = Field(
        description="List of skills that should be emphasized based on job requirements",
        default_factory=list
    )
    achievements_to_add: List[str] = Field(
        description="List of achievements that should be added or modified",
        default_factory=list
    )
    keywords_for_ats: List[str] = Field(
        description="List of important keywords for ATS optimization",
        default_factory=list
    )
    formatting_suggestions: List[str] = Field(
        description="List of formatting improvements",
        default_factory=list
    )


class CompanyResearch(BaseModel):
    recent_developments: List[str] = Field(
        description="List of recent company news and developments",
        default_factory=list
    )
    culture_and_values: List[str] = Field(
        description="Key points about company culture and values",
        default_factory=list
    )
    market_position: Dict[str, List[str]] = Field(
        description="Information about market position, including competitors and industry standing",
        default_factory=dict
    )
    growth_trajectory: List[str] = Field(
        description="Information about company's growth and future plans",
        default_factory=list
    )
    interview_questions: List[str] = Field(
        description="Strategic questions to ask during the interview",
        default_factory=list
    )
