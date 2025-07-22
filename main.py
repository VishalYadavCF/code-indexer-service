import uvicorn
from clone_controller import app
from parser.code_parsing_controller import router as parsing_router

app.include_router(parsing_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8015)
