from fastapi import FastAPI
import uvicorn

from apps.work.data import partner

app = FastAPI()

app.include_router(partner, prefix="/work", tags=["Work 接口", ])

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", reload=True)
