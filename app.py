from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import StreamingResponse
from dotenv import load_dotenv
import json
import asyncio
from crews.basic_crew import BasicCrew

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="CrewAI Assistant")

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Initialize crew
crew = BasicCrew()

def yield_event(event_type, message=""):
    """Helper function to yield formatted events"""
    return json.dumps({"type": event_type, "message": str(message)}) + "\n"

@app.get("/")
async def root(request: Request):
    """Render the main page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/run_crew")
async def run_crew_endpoint(request: Request, user_input: str = Form(...)):
    """Handle the crew execution request with streaming updates"""
    async def generate():
        try:
            async for update in crew.run_crew(user_input):
                yield json.dumps(update) + "\n"
        except Exception as e:
            print(f"Error in run_crew_endpoint: {str(e)}")
            yield json.dumps({"type": "error", "message": str(e)}) + "\n"

    return StreamingResponse(generate(), media_type="text/event-stream")