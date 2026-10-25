## constructAuditAi

проект для автоматизаций анализа строительной документаций

## Stack;

Python 3.12

## Develpment

Work in progress

---

## Local Development

### 1. Create a new enviroment

python -m -venv .venv

### 2. Archivate enviroment

.\.venv\Script\Archivate.ps1

### 3. Initial dependencies

python -m pip install -r requirements.txt

### 4. Run backend

python -m uvicorn app.main:app --reload

### 5. Api Endpoints

Health: http://127.0.0.1:8000/health

Docs: http://127.0.0.1:8000/docs
