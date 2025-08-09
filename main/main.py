import easyocr
import os
image_folder = "..\image"
reader = easyocr.Reader(['th', 'en'], gpu=True)
# reader.readtext(path, detail=0)

for i in os.listdir(image_folder):
    if i.endswith(".jpg") or i.endswith(".png"):
        image_path = os.path.join(image_folder, i)
        result = reader.readtext(image_path, detail=0)
        print(f"Results for {i}: {result}")