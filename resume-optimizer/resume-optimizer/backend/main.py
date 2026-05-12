from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routes import analyze, automate, optimize, upload
from backend.core.config import settings

app = FastAPI(title=settings.app_name, version='1.0.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(upload.router, prefix='/api/upload', tags=['upload'])
app.include_router(analyze.router, prefix='/api/analyze', tags=['analyze'])
app.include_router(optimize.router, prefix='/api/optimize', tags=['optimize'])
app.include_router(automate.router, prefix='/api/automate', tags=['automate'])


@app.get('/')
def healthcheck() -> dict[str, str]:
    return {'status': 'ok', 'app': settings.app_name}
