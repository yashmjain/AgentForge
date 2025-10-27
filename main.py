from fastapi import FastAPI, Request

from health.router import health_router

app = FastAPI(title="Agent Forge APIs")

app.include_router(health_router)






if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:app", host="0.0.0.0", port=8010, log_level="debug", reload=True)

