from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend requests
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

products = {
    "milk": {"blinkit": 68, "zepto": 65},
    "eggs": {"blinkit": 90, "zepto": 88},
    "bread": {"blinkit": 45, "zepto": 42},
}

@app.get("/")
def home():
    return {"message": "Grocery Compare API running"}

@app.get("/compare/{item}")
def compare(item: str):
    item = item.lower()
    if item in products:
        return products[item]
    return {"error": "Item not found"}