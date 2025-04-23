from functools import lru_cache
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from rest_api.config import Settings
from rest_api.llm import LLM

app = FastAPI()


# == Contracts
class CoverLetterRequest(BaseModel):
    job_description: str
    applicant_name: str


class CoverLetterResponse(BaseModel):
    cover_letter_markdown: str


# == Dependencies
@lru_cache
def get_settings():
    return Settings()


def get_llm(settings: Annotated[Settings, Depends(get_settings)]):
    return LLM(settings.openai_api_key)


# == Endpoints
@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")


@app.post("/coverletters/generate")
async def generate_cover_letter(
    request: CoverLetterRequest,
    llm: Annotated[LLM, Depends(get_llm)],
):
    cover_letter_markdown = await llm.generate_coverletter(
        request.job_description,
        request.applicant_name,
    )

    return CoverLetterResponse(
        cover_letter_markdown=cover_letter_markdown,
    )
