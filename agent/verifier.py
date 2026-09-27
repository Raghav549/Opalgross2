from pydantic import BaseModel

class VerificationResult(BaseModel):
    success: bool
    evidence: list[str]
    failures: list[str] = []
    assumptions: list[str] = []

def verify_claim(claim: str, evidence: list[str]) -> VerificationResult:
    if not evidence:
        return VerificationResult(success=False, evidence=[], failures=[f"No evidence found for: {claim}"])
    return VerificationResult(success=True, evidence=evidence)
