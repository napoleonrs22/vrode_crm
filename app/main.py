from fastapi import FastAPI
from app.routers import lead_router
#from app.routers import user_router

app = FastAPI(
    title="CRM API",
    version="1.0.0"
)

app.include_router(lead_router.router)

#app.include_router(user_router.router)


@app.get("/")
def health_check():
    return {"status": "ok"}