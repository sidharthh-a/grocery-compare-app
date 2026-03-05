from fastapi import FastAPI

app = FastAPI()

products = {
    "milk": {"blinkit": 68, "zepto": 65},
    "eggs": {"blinkit": 90, "zepto": 88},
    "bread": {"blinkit": 45, "zepto": 42}
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