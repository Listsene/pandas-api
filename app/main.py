from fastapi import FastAPI, HTTPException

from app.models.question import Question
from app.services.pandas_ai_service import PandasAIService

app = FastAPI()
pandas_service = PandasAIService()


@app.get("/")
async def root():
  return {"message": "Hello World"}


@app.post("/ask")
async def ask_question(question: Question):
    try:
        response = pandas_service.ask_question(question.text)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Optional: Add a route to get data preview
@app.get("/preview")
async def get_preview():
    try:
        return pandas_service.get_data_preview()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
