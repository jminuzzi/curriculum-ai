from __future__ import annotations

from pathlib import Path
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException

from backend.api.services.ai_analyzer import AIAnalyzer
from backend.api.services.pdf_extractor import PDFExtractor
from backend.core.config import settings

router = APIRouter()


class AnalyzeRequest(BaseModel):
    file_id: str
    target_role: str | None = None


@router.post('/')
def analyze_resume(payload: AnalyzeRequest) -> dict:
    file_path = Path(settings.upload_dir) / payload.file_id
    if not file_path.exists():
        raise HTTPException(status_code=404, detail='Arquivo não encontrado.')

    extracted_text = PDFExtractor.extract_text(file_path)
    if not extracted_text:
        raise HTTPException(status_code=400, detail='Não foi possível extrair texto do currículo.')

    analysis = AIAnalyzer.analyze(extracted_text, payload.target_role)
    return {
        'file_id': payload.file_id,
        'text_preview': extracted_text[:1500],
        'analysis': analysis,
    }
