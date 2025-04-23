# Cover letter co-author

A rest service with a single endpoint `coverletters/generate` that uses the `gpt-4.1-nano` from OpenAI to generate coverletters.

The endpoint accepts a job-description and a applicant-name. The response contains the coverletter as markdown text.

Run the rest service with `make serve-dev` and access the endpoint in your browser to test it with the served Swagger-UI. Alternatively use the `demo.ipynb`-notebook.

## Assumptions

- Developed and executed under linux with python3 and make installed

## Getting started

1. Add a `.env`-file with an `OPENAI_API_KEY` entry
1. Run `make test` to execute the unit-tests
1. Run `make serve-dev` to start the application
1. Open `http://127.0.0.1:55446` in a browser


## Parking lot

- Dockerization with production setup
- Dependency locking
- Think about CORS, auth, etc. Depending on how the API is to be used and deployed.
- Use a CV instead of applicant-name/specific fields
- Additional endpoint to generate questionaire based on CV and JD. This additional info could be supplied in `coverletters/generate`.
- Abstract model interface so that you can also run against a local llm
- snake_casing vs camelCasing.. It is apparently still a thing in FastAPI. Investigate pydantic stuff
