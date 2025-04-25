from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv
from typing import Dict, Any

# Load environment variables first
load_dotenv()

# Define models BEFORE they're used
class AgentRequest(BaseModel):
    provider: str  # "vapi" or "retell"
    name: str
    model: str
    voice: str
    prompt: str
    response_engine: Dict[str, Any] = {
        "type": "retell-llm",
        "llm_id": "gpt-3.5-turbo",
        "llm_websocket_url": "wss://retell-llm-demo.retell.ai"
    }

# Then create the app
app = FastAPI()

# Rest of your endpoints...
@app.post("/create-agent")
async def create_agent(request: AgentRequest):
    # Implementation here
    pass

def create_vapi_agent(request: AgentRequest):
    # Implementation here
    pass

def create_retell_agent(request: AgentRequest):
    # Implementation here
    pass
