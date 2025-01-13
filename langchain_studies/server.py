from fastapi import FastAPI
from langserve import add_routes
from main import chain

app = FastAPI(title='My IA App', description='Translate the text')

add_routes(app, chain, path='/translate')

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='localhost', port=8000)
