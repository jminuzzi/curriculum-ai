from __future__ import annotations

import re
from collections import Counter


class AIAnalyzer:
    TECH_KEYWORDS = {
        'python', 'java', 'javascript', 'typescript', 'sql', 'react', 'node', 'docker',
        'aws', 'azure', 'git', 'linux', 'api', 'fastapi', 'django', 'flask', 'scrum',
        'kanban', 'trello', 'power bi', 'excel', 'c#', '.net', 'html', 'css'
    }

    ACTION_VERBS = {
        'desenvolvi', 'implementei', 'criei', 'otimizei', 'automatizei', 'liderei',
        'analisei', 'projetei', 'configurei', 'mantive', 'reduzi', 'aumentei', 'gerenciei'
    }

    @classmethod
    def analyze(cls, text: str, target_role: str | None = None) -> dict:
        normalized = ' '.join(text.lower().split())
        words = re.findall(r'[\w\.#+-]+', normalized)
        keyword_hits = sorted({k for k in cls.TECH_KEYWORDS if k in normalized})
        action_hits = sorted({v for v in cls.ACTION_VERBS if v in normalized})
        email_found = bool(re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', text))
        phone_found = bool(re.search(r'(\+?\d{2,3}\s?)?(\(?\d{2}\)?\s?)?\d{4,5}-?\d{4}', text))
        linkedin_found = 'linkedin.com' in normalized

        problems: list[str] = []
        suggestions: list[str] = []

        if len(text.strip()) < 400:
            problems.append('Currículo muito curto para demonstrar experiência e resultados.')
            suggestions.append('Adicione projetos, experiências, tecnologias e resultados mensuráveis.')
        if not email_found or not phone_found:
            problems.append('Informações de contato parecem incompletas.')
            suggestions.append('Inclua e-mail profissional e telefone com DDD.')
        if not linkedin_found:
            suggestions.append('Adicione o link do LinkedIn ou portfólio, se tiver.')
        if len(keyword_hits) < 5:
            problems.append('Poucas palavras-chave técnicas identificadas.')
            suggestions.append('Inclua tecnologias e ferramentas compatíveis com a vaga alvo.')
        if len(action_hits) < 3:
            suggestions.append('Use verbos de ação para destacar o que você fez de fato.')

        freq = Counter(words)
        repeated = [w for w, c in freq.items() if c > 8 and len(w) > 5][:8]
        if repeated:
            suggestions.append(f'Evite repetir em excesso termos como: {", ".join(repeated)}.')

        score = 50
        score += min(len(keyword_hits) * 4, 24)
        score += 10 if email_found else 0
        score += 10 if phone_found else 0
        score += 6 if linkedin_found else 0
        score = min(score, 100)

        target_alignment = []
        if target_role:
            role_tokens = [t for t in re.findall(r'\w+', target_role.lower()) if len(t) > 3]
            matched = [t for t in role_tokens if t in normalized]
            if matched:
                target_alignment.append(f'O currículo já conversa com a vaga em: {", ".join(sorted(set(matched)))}.')
            else:
                target_alignment.append('O currículo ainda não está bem alinhado à vaga alvo informada.')
                suggestions.append('Inclua no resumo profissional e nos projetos os termos centrais da vaga.')

        return {
            'score': score,
            'keywords_found': keyword_hits,
            'action_verbs_found': action_hits,
            'problems': problems,
            'suggestions': suggestions,
            'target_alignment': target_alignment,
        }
