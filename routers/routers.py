from fastapi import APIRouter

router = APIRouter(tags=["테스트"])

@router.get("/hello", summary="테스트", description="진짜 테스트임")
def test_route():
    return {"message": "Hello, world!"}