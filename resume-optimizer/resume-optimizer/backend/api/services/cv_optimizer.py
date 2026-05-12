from __future__ import annotations

from pathlib import Path
import re
from textwrap import dedent

from backend.core.config import settings


class CVOptimizer:
    @staticmethod
    def optimize_text(raw_text: str, target_role: str | None = None) -> dict:
        lines = [line.strip() for line in raw_text.splitlines() if line.strip()]
        clean_text = '\n'.join(lines)
        top_skills = []
        for skill in ['Python', 'SQL', 'JavaScript', 'React', 'FastAPI', 'Git', 'Docker', 'Scrum', 'Kanban']:
            if skill.lower() in clean_text.lower():
                top_skills.append(skill)

        summary = 'Profissional com foco em organização, execução e melhoria contínua.'
        if target_role:
            summary = (
                f'Profissional em desenvolvimento com foco em {target_role}, '
                'com experiência prática em projetos, organização de tarefas e aprendizado rápido.'
            )

        optimized = dedent(f'''
        RESUMO PROFISSIONAL
        {summary}

        COMPETÊNCIAS-CHAVE
        {' | '.join(top_skills) if top_skills else 'Comunicação | Organização | Aprendizado rápido | Resolução de problemas'}

        EXPERIÊNCIAS E PROJETOS
        {CVOptimizer._rewrite_bullets(clean_text)}

        FORMAÇÃO E INFORMAÇÕES ADICIONAIS
        {CVOptimizer._extract_education_or_fallback(clean_text)}
        ''').strip()

        file_name = f'optimized_{re.sub(r"[^a-zA-Z0-9_-]+", "_", (target_role or "resume").lower())}.txt'
        output_path = Path(settings.output_dir) / file_name
        output_path.write_text(optimized, encoding='utf-8')

        return {
            'optimized_text': optimized,
            'saved_to': str(output_path),
        }

    @staticmethod
    def _rewrite_bullets(text: str) -> str:
        chunks = [c.strip(' -•\t') for c in text.splitlines() if len(c.strip()) > 20][:8]
        bullets: list[str] = []
        for chunk in chunks:
            if not re.match(r'^(desenvolvi|implementei|criei|otimizei|liderei|configurei)', chunk.lower()):
                chunk = 'Atuei em ' + chunk[0].lower() + chunk[1:]
            bullets.append(f'- {chunk}')
        if not bullets:
            bullets = [
                '- Desenvolvi atividades com foco em organização, qualidade e entrega.',
                '- Colaborei com equipes e acompanhei tarefas do início até a validação.',
            ]
        return '\n'.join(bullets)

    @staticmethod
    def _extract_education_or_fallback(text: str) -> str:
        candidates = [
            line.strip() for line in text.splitlines()
            if any(token in line.lower() for token in ['curso', 'graduação', 'faculdade', 'ensino', 'tecnólogo'])
        ]
        if candidates:
            return '\n'.join(f'- {line}' for line in candidates[:4])
        return '- Adicione aqui curso, instituição, previsão de conclusão e certificações relevantes.'
