from fastapi import FastAPI, HTTPException, status
from backend.schemas.post import PostCreate, PostResponse
from backend.services.post_service import PostService

app = FastAPI(title="Gestão de Redes API")

post_service = PostService()

@app.get("/")
async def read_root() -> dict[str, str]:
    return {"message": "Welcome to Gestão de Redes API"}

@app.post("/posts", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
async def create_post(post_in: PostCreate) -> PostResponse:
    try:
        return await post_service.create_post(post_in)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
