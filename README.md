# SentimentOps

Progetto MLOps per Profession AI: pipeline e pratiche operative per sentiment analysis (focus su CI/CD, tracking, monitoring, evaluation).  
W1: setup repo, qualità base (lint/test) e MLflow tracking “hello run”.

## Prerequisiti
- Python 3.14.x
- Git
- (Windows) PowerShell

## Quick Start (Windows / PowerShell)
```powershell
cd C:\Users\cpmin\Projects\sentimentops

python -m venv .venv
.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

ruff check src tests
pytest tests -v

