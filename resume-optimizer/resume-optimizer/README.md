# Resume Optimizer

MVP em Python para:
- subir currículo em PDF/TXT;
- extrair texto;
- analisar pontos fortes e fracos;
- gerar uma versão otimizada em TXT;
- preparar preenchimento assistido para LinkedIn, Gupy e Catho.

## Estrutura

- `backend/`: API FastAPI
- `frontend/`: interface Streamlit
- `automation/`: drivers e utilitários de preenchimento assistido
- `data/uploads/`: currículos enviados
- `output/`: arquivos otimizados gerados

## Como rodar

### 1) Instalar dependências

```bash
pip install -r requirements.txt
```

### 2) Iniciar backend

```bash
uvicorn backend.main:app --reload
```

### 3) Iniciar frontend

Em outro terminal:

```bash
streamlit run frontend/app.py
```

## Build

Para gerar executável da interface:

```bash
python build.py
```

> Observação: o `.exe` precisa ser gerado no Windows com PyInstaller. Neste pacote eu deixei a estrutura pronta e o script de build.

## Limites do MVP

- Extração focada em PDF com texto selecionável e TXT.
- A parte de automação está em modo seguro/assistido (`dry_run`).
- Login, captcha e envio final continuam manuais.
