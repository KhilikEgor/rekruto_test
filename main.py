from fastapi import FastAPI, Response

from typing import Optional

import uvicorn

app = FastAPI()


@app.get('/')
async def hello_page(name: Optional[str] = '', message: Optional[str] = ''):
    if name:
        return Response(
            f'Hello, {name}! '
            f'{message}', media_type='text/html'
        )
    
    return Response(
        f'Privet',
        media_type='text/html'
    )


if __name__ == '__main__':
    print('Server is starting...')
    uvicorn.run('main:app', reload=True)
    
