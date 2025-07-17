from fastapi import FastAPI
import uvicorn

from apps.app1.api import app1
from apps.app2.api import app2

app = FastAPI()

app.include_router(app1, prefix="/app1", tags=["App1 接口", ])
app.include_router(app2, prefix="/app2", tags=["App2 接口", ])

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1",
                port=8080, reload=True)
