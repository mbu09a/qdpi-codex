from typing import Any, Callable, Dict, List, Tuple, Awaitable, Union
import asyncio

Subscriber = Callable[[str, Any], Union[Any, Awaitable[Any]]]

class MemoryBus:
    """In‑memory pub/sub with simple request‑reply pattern."""
    def __init__(self) -> None:
        self._events: List[Tuple[str, Any]] = []
        self._subs: Dict[str, List[Subscriber]] = {}

    def subscribe(self, direction: str, fn: Subscriber) -> None:
        self._subs.setdefault(direction, []).append(fn)

    async def publish(self, direction: str, payload: Any) -> Any:
        self._events.append((direction, payload))
        results: List[Any] = []

        for fn in self._subs.get(direction, []):
            res = fn(direction, payload)
            if asyncio.iscoroutine(res):
                res = await res
            results.append(res)

        # Return first non‑None reply or echo
        return next((r for r in results if r is not None), payload)

bus = MemoryBus()

# --- TEMP default subscriber ---
def upper_echo(_dir: str, data: Any) -> Any:
    if isinstance(data, str):
        return data.upper()
bus.subscribe("ask", upper_echo) 