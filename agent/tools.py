from dataclasses import dataclass
from typing import Callable
from .policy import ActionRisk, authorize

@dataclass
class ToolSpec:
    name: str
    description: str
    risk: ActionRisk
    handler: Callable

class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, ToolSpec] = {}

    def register(self, spec: ToolSpec) -> None:
        self._tools[spec.name] = spec

    def list(self) -> list[ToolSpec]:
        return list(self._tools.values())

    def execute(self, name: str, *args, user_confirmed: bool = False, **kwargs):
        spec = self._tools[name]
        decision = authorize(spec.risk, user_confirmed=user_confirmed)
        if not decision.allowed:
            return {"status": "authorization_required", "reason": decision.reason}
        return spec.handler(*args, **kwargs)
