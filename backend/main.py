from fastapi import FastAPI

app = FastAPI(
    title="Vortex API",
    description="Inventory management system for the Vortex project",
    version="0.1.0",
    contact={
        "name": "Emmanuel Cruz",
        "url": "https://emmanuel-cruz.netlify.app/",
        "email": "emmanuelgerr@gmail.com",
    },
)

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI!"}