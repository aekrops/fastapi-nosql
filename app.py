import requests
from fastapi import FastAPI
import uvicorn
from models import Link
from strategies.strategy_manager import StrategyManager

app = FastAPI()


@app.post('/upload-data')
async def load_file(file: Link):
    has_next_chunk = False
    read_limit = 1000
    if not (file_url := file.url):
        return {'message': 'Provide dataset url'}
    if data := get_file_response(file_url, read_limit):
        has_next_chunk = True

    manager = StrategyManager(file_url)

    if manager.is_file_uploaded():
        return {'message': 'File is uploaded already'}
    manager.start_processing_data()
    while has_next_chunk:
        if file_response := next(data):
            await manager.process_data(file_response)
        else:
            has_next_chunk = False
    manager.finish_processing_data()
    return {'message': 'File was uploaded'}


def get_file_response(file_url: str, limit: int):
    offset = 0
    while True:
        yield requests.get(f"{file_url}?$limit={limit}&$offset={offset}").json()
        offset += limit


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
