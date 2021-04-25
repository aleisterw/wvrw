from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI(docs_url="/docs", redoc_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/items/{item_id}", response_class=HTMLResponse)
async def read_item(request: Request, item_id: str):
    return templates.TemplateResponse("item.html", {"request": request, "item_id": item_id})

@app.get("/")
async def root():
    return {"message": "Hello World"}
