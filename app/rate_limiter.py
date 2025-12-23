import time
from fastapi import HTTPException

requests = {}
WINDOW = 60
LIMIT = 5

def rate_limit():
    now = time.time()
    count, start = requests.get("global", (0, now))

    if now - start > WINDOW:
        requests["global"] = (1, now)
        return

    if count >= LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    requests["global"] = (count + 1, start)
