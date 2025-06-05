from fastapi import FastAPI, UploadFile, File
from app.classifier import classify_input
from app.router import route_action

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    metadata = classify_input(file.filename, content)
    result = route_action(metadata, content)
    return {"result": result}
