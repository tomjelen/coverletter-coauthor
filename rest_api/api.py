from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from rest_api.config import Settings
from rest_api.llm import LLM

app = FastAPI()


class CoverLetterRequest(BaseModel):
    job_description: str
    applicant_name: str


class CoverLetterResponse(BaseModel):
    cover_letter_markdown: str


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")


@app.post("/coverletters/generate")
async def generate_cover_letter(request: CoverLetterRequest):
    return CoverLetterResponse(
        cover_letter_markdown=f"Cover letter for {request.applicant_name}",
    )


@app.post("/hi-openai")
async def llm(request: CoverLetterRequest):
    settings = Settings()
    llm = LLM(settings.openai_api_key)

    return CoverLetterResponse(
        cover_letter_markdown=await llm.generate_coverletter(
            request.job_description, request.applicant_name
        ),
    )
