from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

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
