# import datetime
# from fastapi import FastAPI, status
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# from .endpoints import router as endpoints_router
# from .router import api_router

# api = FastAPI(
#     title="ETICatalogue API",
# )

# api.include_router(router=api_router)

# @api.get("/", status_code=status.HTTP_200_OK)
# def health_check():
#     return datetime.datetime.now()

# api.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# if __name__ == "__main__":
#     uvicorn.run(
#         api=api,
#         host="0.0.0.0", 
#         port=8000
#     )


from fastapi import FastAPI
from api.routes import product

api = FastAPI( title="ETICatalogue API", description= "This API provides data for our ETICatalogue catalog", version="0.1.0" )


routers = [
    product.router
]

for router in routers:
    api.include_router(router=router)