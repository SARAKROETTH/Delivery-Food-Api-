from fastapi import APIRouter, UploadFile, File,HTTPException
from Repository.ImageRepo import save_image,get_image_path
from Schemas.ImageSchemas import UploadResponse
from fastapi.responses import FileResponse

router = APIRouter()

@router.post("/upload", response_model=UploadResponse)
async def upload_image(file: UploadFile = File(...)):

    filename = save_image(file)

    return UploadResponse(
        filename=filename,
        url=f"http://127.0.0.1:8000/image/{filename}"
    )

@router.get("/image/{filename}")
def get_image(filename: str):   # ✅ no async needed

    file_path = get_image_path(filename)

    if not file_path:
        raise HTTPException(status_code=404, detail="Image not found")

    return FileResponse(file_path)
