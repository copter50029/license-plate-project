import os
from fastapi import FastAPI
import base64
app = FastAPI()


@app.get("/")
def read_root():
    path = "D:\github_repo\license-plate-project\main\images"
    images = {}
    for i in os.listdir(path):
        with open(os.path.join(path, i), "rb") as f:
            img_bytes = f.read()
            img_b64 = base64.b64encode(img_bytes).decode("utf-8")
            images[f"{i}"] = img_b64
    return images
