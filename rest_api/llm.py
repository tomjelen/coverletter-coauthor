from openai import AsyncOpenAI


SYSTEM_PROMPT = """
You are a professional cover letter writer with expertise in various industries.
Your task is to create compelling, tailored cover letters that help applicants stand out.
Always maintain a professional tone and structure. Format output in clean markdown.
Focus on highlighting relevant qualifications without inventing specific details.
Cover letters should be concise but comprehensive, approximately 300-400 words.
Output should be in markdown format, with clear sections for introduction, body, and conclusion.
"""


class LLMError(Exception):
    pass


class LLM:
    def __init__(self, openai_api_key: str):
        self.client = AsyncOpenAI(api_key=openai_api_key)

    async def generate_coverletter(self, job_description, applicant_name):
        user_prompt = f"""
        Create a professional cover letter for {applicant_name} applying for the following job:

        JOB DESCRIPTION:
        {job_description}
        """

        try:
            completion = await self.client.chat.completions.create(
                model="gpt-4.1-nano",
                messages=[
                    {"role": "developer", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
            )
        except Exception as e:
            # TODO: Look deeper in the documentation to find the right exceptions.
            # I'm sure I can tell difference between 400-like and 500-like errors
            # and handle them differently further up.
            raise LLMError(f"Error when calling OpenAI API") from e

        if not completion.choices:
            raise LLMError("No choices returned from OpenAI API")
        if not completion.choices[0].message.content:
            raise LLMError("No content returned from OpenAI API")

        return completion.choices[0].message.content
