from fastapi import APIRouter

app1 = APIRouter()


@app1.get("/get")
def app1_get():
    return {"app1": "get"}


@app1.post("/post")
def app1_post():
    return {"app1": "post"}
