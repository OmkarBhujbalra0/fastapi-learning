from fastapi import FastAPI,HTTPException,Request
from pydantic import BaseModel
import time

app = FastAPI()

@app.middleware('http')
async def request_log(request:Request,call_next):
    start_time = time.time()

    response = await call_next(request)
    duration = time.time() - start_time
    print(f"{request.url.path},{duration},{request.client.host}")
    return response

class Book(BaseModel):
    title: str
    author: str
    subject: str

library = []

@app.get('/')
def home():
    return {"message":"We're going to deal with Middleware."}

@app.get('/books')
def display():
    return library

@app.get('/books/{book_title}')
def search(book_title:str):
    for i in library:
        if i.title == book_title:
            return i
    raise HTTPException(
        status_code=404, detail="Book not Found"
    )

@app.post('/books')
def adds(book:Book):
    if book not in library:
        library.append(book)
        return {"message":"Book added Successfully."}
    return {"error":"Book already exists."}

@app.put('/books/{book_title}')
def update(book_title:str, new_book:Book):
    for i in library:
        if i.title == book_title:
            i.title = new_book.title
            i.author = new_book.author
            i.subject = new_book.subject
            return {"message":"Book updated successfully."}
    raise HTTPException(
        status_code=404,detail="Book not Found."
    )

@app.delete('/books/{book_title}')
def deletes(book_title:str):
    for i in library:
        if i.title == book_title:
            library.remove(i)
            return {"message":"Book removed successfully."}
    raise HTTPException(
        status_code=404,detail="Book not Found."
    )