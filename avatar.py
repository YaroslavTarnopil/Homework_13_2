from fastapi import File, UploadFile

@app.post("/user/avatar/")
async def upload_avatar(file: UploadFile = File(...)):
    result = cloudinary.uploader.upload(file.file)
    return {"url": result["url"]}
