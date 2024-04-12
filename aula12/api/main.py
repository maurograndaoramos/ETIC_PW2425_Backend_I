from fastapi import FastAPI

from api.routes import alumni


api = FastAPI(
    title="School API",
    description="This API provides data from a school",
)

routers = [
    alumni.router
]

for router in routers:
    api.include_router(router=router)

