from fastapi import FastAPI

app = FastAPI()

@app.get("/mcp/about")
def about():
    return {
        "name": "Anannya Mahajan MCP Server",
        "description": "Resume & validation server for Puch AI"
    }

@app.get("/mcp/validate")
def validate():
    return {"phone": "918485055001"}  # your number without '+'

@app.get("/mcp/resume")
def resume():
    return {
        "resume": "https://drive.google.com/uc?export=download&id=1Kxyn3eYBMFN3nQ-HfExLSNO_IOTzO98T"
    }
