from typing import List
from typing import Optional

import io
from fastapi.staticfiles import StaticFiles
from starlette.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile,  Response
from fastapi.responses import HTMLResponse, StreamingResponse, FileResponse

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}