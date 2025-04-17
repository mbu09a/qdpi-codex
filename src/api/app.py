from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Any, Literal
from src.bus.memory_bus import bus  # via pyright path mapping / ts-node esm

class QuadPayload(BaseModel):
    direction: Literal["read", "ask", "receive", "index"]
    payload:   Any

app = FastAPI(title="qdpi‑codex API")

@app.post("/quad")
async def quad(payload: QuadPayload):
    """Echo endpoint — first step toward quad‑direction bus."""
    result = bus.publish(payload.direction, payload.payload)
    return {"result": result} 