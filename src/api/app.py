import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Any, Literal
from src.bus.memory_bus import bus

class QuadPayload(BaseModel):
    direction: Literal["read", "ask", "receive", "index"]
    payload:   Any

app = FastAPI(title="qdpi‑codex API")

@app.post("/quad")
async def quad(payload: QuadPayload):
    """Echo endpoint — first step toward quad‑direction bus."""
    result = bus.publish(payload.direction, payload.payload)
    return {"result": result} 