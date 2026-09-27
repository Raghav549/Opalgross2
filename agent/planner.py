from pydantic import BaseModel
from .state import TaskState

class PlanStep(BaseModel):
    id: str
    objective: str
    tool: str | None = None
    verification: str | None = None

class Planner:
    def plan(self, state: TaskState) -> list[PlanStep]:
        goal = state.goal.lower()
        steps: list[PlanStep] = []
        if any(k in goal for k in ("search", "research", "web", "find")):
            steps.append(PlanStep(id="research", objective="Gather and compare relevant sources", tool="web.search", verification="Check source relevance and corroboration"))
        if any(k in goal for k in ("code", "build", "app", "website", "debug")):
            steps.append(PlanStep(id="inspect-code", objective="Inspect the existing project before editing", tool="repo.inspect", verification="Confirm affected files and dependencies"))
        if any(k in goal for k in ("3d", "shader", "webgpu", "three.js")):
            steps.append(PlanStep(id="design-3d", objective="Design the scene, rendering pipeline and performance strategy", tool="creative.3d", verification="Run visual/technical checks"))
        if not steps:
            steps.append(PlanStep(id="respond", objective="Understand intent and respond naturally"))
        steps.append(PlanStep(id="verify", objective="Verify important outputs and report limitations", tool="verifier", verification="No success claim without evidence"))
        return steps
