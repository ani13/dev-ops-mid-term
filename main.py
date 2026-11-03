from fastapi import FastAPI, HTTPException
from fibonacci import fibonacci

app = FastAPI(
    title="Fibonacci API",
    description="A simple API that calculates Fibonacci numbers.",
    version="1.0.0"
)


@app.get("/fibonacci/{n}")
def get_fibonacci(n: int):
    if n < 0:
        raise HTTPException(
            status_code=422,
            detail="Number must be non-negative"
        )

    return {
        "n": n,
        "result": fibonacci(n)
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }