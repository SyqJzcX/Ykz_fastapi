from fastapi import APIRouter

partner = APIRouter()


@partner.get("/partner")
def get_all_():
    return {"app1": "get"}
