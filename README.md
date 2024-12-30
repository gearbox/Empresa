![Logo](static/FastAPI_Template_Logo.png)
# FastAPI template
### Purpose
This template tends to follow best practices and patterns, and it can be used to reduce writing boilerplate code and start project asap or as a starting point in learning FastAPI framework.

### Architecture
It uses:
- `uvicorn` as an Async Server Gateway Interface, 
- `loguru` as a logging system with a prebuilt logs template,
- `fastapi` as a main framework,
- `pydantic` for data validation,
- `pydantic-settings` for the app settings which also support `.env` file with OS env variables.
- `postgresql` as a database,
- `sqlalchemy` as an ORM,
- `alembic` for migrations,
- `redis` as a cache,

Application is split into `schemas`, `routers` and `managers`, which are contained in separate packages. 
`routers` package is used for creating endpoints, `managers` contains business-logic for endpoints.
We have a separate `errors.py` file for custom error handlers, `dependencies.py` file to maintain dependencies and `settings.py` to maintain app's settings.
`logger.py` is used to maintain loguru tuning and initial setup and loguru logs template is in `settings.py`.
You can put .env file in the root of the app's folder (.env.sample is included).

### Endpoints
There are several endpoints which could be used directly or as an example:

| Endpoint URL | Description                                                                                                                                       |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| /            | Is set to show Swagger (OpenAPI) documentation, same as `/docs`                                                                                   |
| /docs        | Default FastAPI Swagger (OpenAPI) documentation endpoint                                                                                          |
| /redoc       | Default FastAPI Redoc documentation endpoint                                                                                                      |
| /healthcheck | Endpoint that could be used to check if App is up and healthy. <br/>It returns the app uptime and start date and time, db and redis health status |
| /info        | Sample endpoint that uses token authorisation method                                                                                              |

