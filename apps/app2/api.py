from fastapi import APIRouter

app2 = APIRouter()


@app2.get("/get")
def app2_get():
    return {"app2": "get"}


@app2.post("/post")
def app1_post():
    return {"app2": "post"}

