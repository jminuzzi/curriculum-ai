from __future__ import annotations

from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, File, HTTPException, UploadFile

from backend.core.config import settings

router = APIRouter()


@router.post('/')
async def upload_resume(file: UploadFile = File(...)) -> dict:
    suffix = Path(file.filename or '').suffix.lower()
    if suffix not in {'.pdf', '.txt'}:
        raise HTTPException(status_code=400, detail='Envie apenas PDF ou TXT.')

    file_id = f'{uuid4().hex}{suffix}'
    target_path = Path(settings.upload_dir) / file_id
    content = await file.read()

    if len(content) > settings.max_upload_size_mb * 1024 * 1024:
        raise HTTPException(status_code=400, detail='Arquivo acima do limite permitido.')

    target_path.write_bytes(content)

    return {
        'message': 'Upload concluído com sucesso.',
        'file_id': file_id,
        'file_path': str(target_path),
        'original_name': file.filename,
    }
