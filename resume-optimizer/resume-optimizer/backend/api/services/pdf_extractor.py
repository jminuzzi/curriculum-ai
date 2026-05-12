from __future__ import annotations

from pathlib import Path

import fitz  # PyMuPDF


class PDFExtractor:
    @staticmethod
    def extract_text(file_path: str | Path) -> str:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f'Arquivo não encontrado: {path}')

        if path.suffix.lower() == '.txt':
            return path.read_text(encoding='utf-8', errors='ignore')

        if path.suffix.lower() != '.pdf':
            raise ValueError('Formato não suportado. Envie PDF ou TXT.')

        text_parts: list[str] = []
        with fitz.open(path) as doc:
            for page in doc:
                text_parts.append(page.get_text())
        return '\n'.join(text_parts).strip()
