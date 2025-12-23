# Trade Opportunities API

FastAPI application that provides sector-based trade opportunity analysis.

## How to run
pip install -r requirements.txt
uvicorn app.main:app --reload

## API Endpoint
GET /analyze/{sector}

Example:
GET /analyze/pharmaceuticals
