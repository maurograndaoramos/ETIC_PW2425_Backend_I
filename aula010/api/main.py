from fastapi import FastAPI, status
import uvicorn


api = FastAPI(
    title="ETICapi",
)

@api.get("/", status_code=status.HTTP_200_OK)
def health_check():
    return

if __name__ == "__main__":
    uvicorn.run(
        api=api,
        host="0.0.0.0", 
        port=8000
    )