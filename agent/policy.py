from enum import Enum
from pydantic import BaseModel

class ActionRisk(str, Enum):
    READ = "read"
    WRITE_EXTERNAL = "write_external"
    DESTRUCTIVE = "destructive"
    AUTH_CHANGE = "auth_change"

class ActionDecision(BaseModel):
    allowed: bool
    requires_confirmation: bool
    reason: str

def authorize(risk: ActionRisk, user_confirmed: bool = False) -> ActionDecision:
    if risk == ActionRisk.READ:
        return ActionDecision(allowed=True, requires_confirmation=False, reason="Read-only action")
    if user_confirmed:
        return ActionDecision(allowed=True, requires_confirmation=False, reason="Explicit user authorization received")
    return ActionDecision(
        allowed=False,
        requires_confirmation=True,
        reason="Consequential external action requires explicit user confirmation",
    )
