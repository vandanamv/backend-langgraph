from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "LangGraph backend is alive!"}

print("Backend LangGraph app is running.")