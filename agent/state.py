from typing import Any
from pydantic import BaseModel, Field

class TaskState(BaseModel):
    goal: str
    plan: list[str] = Field(default_factory=list)
    completed_steps: list[str] = Field(default_factory=list)
    observations: list[dict[str, Any]] = Field(default_factory=list)
    artifacts: list[str] = Field(default_factory=list)
    blockers: list[str] = Field(default_factory=list)
    assumptions: list[str] = Field(default_factory=list)
    verified_claims: list[str] = Field(default_factory=list)

    def record_observation(self, source: str, content: str, verified: bool = False) -> None:
        self.observations.append({"source": source, "content": content, "verified": verified})
        if verified:
            self.verified_claims.append(content)
