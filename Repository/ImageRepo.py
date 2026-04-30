import os
import uuid
import shutil
from fastapi import UploadFile

from fastapi.responses import FileResponse


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def save_image(file: UploadFile):

    file_ext = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{file_ext}"

    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return filename

def get_image_path(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        return None

    return file_path

