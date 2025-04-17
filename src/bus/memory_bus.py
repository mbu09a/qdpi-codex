from typing import Any, Dict, List

class MemoryBus:
    def __init__(self) -> None:
        self.events: List[Dict[str, Any]] = []

    def publish(self, direction: str, payload: Any) -> Any:
        self.events.append({"direction": direction, "payload": payload})
        # TEMP stub: echo upper‑cased string payloads
        if isinstance(payload, str):
            return payload.upper()
        return payload

bus = MemoryBus() 