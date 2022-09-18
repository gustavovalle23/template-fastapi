# Utils commands

## Project Download
git clone https://github.com/gustavovalle23/template-fastapi.git

## Access the project directory
cd template-fastapi

## Initialization of the virtual environment
python -m venv venv && source venv/bin/activate && pip install --upgrade pip

## Installation of requirements
pip install -r requirements.txt

## Start the local server (will be available at http://127.0.0.1:8000 or localhost:8000)
uvicorn app.main:app --reload

## Run tests
python -m pytest tests/user.py -s -vv
