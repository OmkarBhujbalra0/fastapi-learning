from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Structure of Input

class Book(BaseModel):
    book_title: str
    author: str
    published: int

@app.get('/')
def home():
    return {"message":"Welcome to Library API."}

books_list = []

# Display all the books

@app.get('/books')
def display():
    return books_list

# Add new book

@app.post('/books')
def adds(book: Book):
    if book not in books_list:
        books_list.append(book)
        return {"message":"Book added successfully."}
    return {"error":"Book already added."}

# Search a book

@app.get('/books/{book_title}')
def search(book_title:str):
    for i in books_list:
        if book_title == i.book_title:
            return {"Book":i}
    return {"error":"Book Not Found"}

# Update the book

@app.put('/books/{book_title}')
def update(book_title:str,new:Book):
    for i in books_list:
        if book_title == i.book_title:
            i.book_title = new.book_title
            i.author = new.author
            i.published = new.published
            return {"message":"Book updated successfully."}
    return {"error":"Book not Found"}

# delete the book

@app.delete('/books/{book_title}')
def deletes(book_title:str):
    for i in books_list:
        if i.book_title == book_title:
            books_list.remove(i)
            return {"message":"Book Removed"}
    return {"message":"Book not Found"}