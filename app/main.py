from fastapi import FastAPI
from app.database import AsyncSessionLocal
from app.routers import auth_router, comment_router, lead_router
from app.service.auth_service import AuthService


app = FastAPI(
    title="CRM API",
    version="1.0.0",
)

auth_service = AuthService()


@app.on_event("startup")
async def on_startup():
    async with AsyncSessionLocal() as session:
        await auth_service.ensure_admin_user(session)


app.include_router(auth_router.router)
app.include_router(lead_router.router)
app.include_router(comment_router.router)


@app.get("/")
def health_check():
    return {"status": "ok"}
