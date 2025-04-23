from openai import AsyncOpenAI


class LLM:
    def __init__(self, openai_api_key: str):
        self.client = AsyncOpenAI(api_key=openai_api_key)

    async def generate_coverletter(self, job_description, applicant_name):
        response = await self.client.responses.create(
            model="gpt-4.1-nano",
            input="Write a one-sentence bedtime story about a unicorn.",
        )

        return response.output_text
