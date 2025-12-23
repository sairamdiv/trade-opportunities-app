from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

@app.get("/analyze/{sector}")
def analyze_sector(
    sector: str,
    Authorization: str = Header(...)
):
    if Authorization != "Bearer secret123":
        raise HTTPException(status_code=401, detail="Invalid token")

    return {
        "sector": sector,
        "summary": f"Trade opportunities analysis for {sector}",
        "opportunities": [
            "Growing domestic demand",
            "Export potential increasing",
            "Government policy support"
        ],
        "risks": [
            "Regulatory changes",
            "Global market volatility"
        ],
        "outlook": "Positive in short to medium term"
    }


