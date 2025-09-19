from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Health check endpoint
@app.get("/mcp")
def mcp_root():
    return {"message": "MCP Server running successfully!"}

# Resume endpoint
@app.get("/mcp/resume")
def get_resume():
    resume = {
        "name": "Anannya Mahajan",
        "email": "anannyamahajan00@gmail.com",
        "phone": "918485055001",  # format: countrycode + number, no '+'
        "linkedin": "https://linkedin.com/in/anannya-mahajan",
        "github": "https://github.com/anannya-mahajan",
        "leetcode": "https://leetcode.com/u/Anannyamahajan/",
        "summary": "Results-driven Computer Science & Engineering undergraduate with expertise in software development, full-stack engineering, and data-driven applications.",
        "skills": {
            "languages_frameworks": ["Python", "Java", "JavaScript", "C", "HTML5", "CSS3", "Bootstrap", "Streamlit"],
            "databases": ["MySQL", "Snowflake"],
            "tools_libraries": ["Pandas", "Chart.js", "OpenAI API", "Figma", "Git", "yfinance", "IBM Qiskit"],
            "core_areas": ["Full-Stack Development", "REST APIs", "AI Agents", "Data Visualization", "Responsive Web Design", "Cloud Integration", "Debugging & Optimization", "Quantum Algorithms"]
        },
        "education": [
            {"degree": "B.Tech – Computer Science & Engineering", "institution": "Ramdeobaba University", "years": "2024–2028"},
            {"degree": "B.Sc – Data Science", "institution": "IIT Madras", "years": "Ongoing"}
        ],
        "projects": [
            {"title": "Finance Dashboard (Hackathon)", "description": "Engineered a full-stack finance web app with real-time stock APIs; implemented interactive data visualizations and chatbot support; improved user insight delivery by 30%.", "tech": ["Python", "REST APIs", "Chart.js", "MySQL"]},
            {"title": "College Admission Portal (UI/UX Design)", "description": "Designed and prototyped an accessible admission system; optimized navigation flow to improve user experience for students.", "tech": ["Figma", "UI/UX", "Accessibility"]},
            {"title": "Music Website", "description": "Developed a responsive front-end application with playlists, embedded audio players, and artist highlights; improved engagement through modern CSS styling.", "tech": ["HTML5", "CSS3", "Responsive Design"]},
            {"title": "E-commerce Shopping App", "description": "Built a Python-based application with browsing, cart, and checkout; applied object-oriented programming and file handling for efficiency.", "tech": ["Python", "OOP", "File Systems"]},
            {"title": "DSA Visualizers", "description": "Created algorithm visualization tools for searching/sorting; used by peers for technical interview preparation.", "tech": ["Python", "Data Structures", "Algorithms"]},
            {"title": "Informational Website (Live Project)", "description": "Deployed and customized a live informational website with optimized content management.", "tech": ["GoDaddy Builder", "Web Hosting"]}
        ],
        "achievements_certifications": [
            "Hackathons — Delivered full-stack and UI/UX solutions in competitions; recognized for innovative design and teamwork.",
            "Rust Fundamentals — Coursera (2025)",
            "UX Design — Coursera (2025)",
            "Website Redesign — IIT Madras (2024)"
        ]
    }
    return resume

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
