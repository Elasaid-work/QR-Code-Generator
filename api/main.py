from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import qrcode
from fastapi.staticfiles import StaticFiles
import os
from io import BytesIO
from urllib.parse import quote


app = FastAPI()

# Allowing CORS for local testing
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Serve static files (QR codes)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/generate-qr/")
async def generate_qr(url: str):
    try:
        # Generate QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Ensure the local folder exists
        local_dir = "static/qr_codes"
        os.makedirs(local_dir, exist_ok=True)
        file_name = f"{url.split('//')[-1]}.png"
        file_path = os.path.join(local_dir, f"{url.split('//')[-1]}.png")
        img.save(file_path)

        # Return local file path or serve via a static route
        s3_url = f"http://localhost:8000/static/qr_codes/{file_name}"
        return {"qr_code_url": s3_url}
    
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

