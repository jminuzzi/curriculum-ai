from __future__ import annotations

from pathlib import Path
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException

from backend.api.services.cv_optimizer import CVOptimizer
from backend.api.services.pdf_extractor import PDFExtractor
from backend.core.config import settings

router = APIRouter()


class OptimizeRequest(BaseModel):
    file_id: str
    target_role: str | None = None


@router.post('/')
def optimize_resume(payload: OptimizeRequest) -> dict:
    file_path = Path(settings.upload_dir) / payload.file_id
    if not file_path.exists():
        raise HTTPException(status_code=404, detail='Arquivo não encontrado.')

    extracted_text = PDFExtractor.extract_text(file_path)
    result = CVOptimizer.optimize_text(extracted_text, payload.target_role)
    return {
        'file_id': payload.file_id,
        **result,
    }
