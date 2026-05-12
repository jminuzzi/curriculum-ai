from __future__ import annotations

from pydantic import BaseModel, Field
from fastapi import APIRouter, HTTPException

from backend.api.services.job_automation import JobAutomationService

router = APIRouter()


class AutomateRequest(BaseModel):
    platform: str = Field(description='linkedin, gupy ou catho')
    full_name: str
    email: str
    phone: str | None = None
    summary: str | None = None
    dry_run: bool = True


@router.post('/')
def automate_profile(payload: AutomateRequest) -> dict:
    try:
        result = JobAutomationService.run(
            platform=payload.platform,
            profile_data=payload.model_dump(),
            dry_run=payload.dry_run,
        )
        return result
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:  # pragma: no cover
        raise HTTPException(status_code=500, detail=f'Falha na automação: {exc}') from exc
