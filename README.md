# Cover letter co-author

## Initial thoughts

First iteration:

- Basic FastAPI app with a endpoint
  - Request: job description + applicant-name
  - Response: bunch of text
- Select any remote model, claude or openai?
- Get testing going
- Ugh, fileuploads -> multiform + post. Try avoid it yes?
- Use the /docs endpoint as UI or a very basic terminal client

After / parking lot:

- Error handling when interacting with the model
- Dockerize
- Dependency locking
- Think about CORS, auth, etc
- CV instead of applicant name
- Generate questionaire based on CV and JD
- Abstract model interface to make it possible to change it
- Basic throttling on the model usage

## Assumptions

- Developed and executed under linux with python3 and make installed
