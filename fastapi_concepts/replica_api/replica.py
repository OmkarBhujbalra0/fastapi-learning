from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Welcome to Replica API."}

books_list = []

#Displays all the books in the list

@app.get('/books')
def display():
    return books_list

# Searches specific book from the list

@app.get('/books/{book_name}')
def search(book_name:str):
    if book_name in books_list:
        return {"book" : book_name}
    return {"error":"book not found"}

# Adds the book into the list

@app.post('/books')
def add_book(book_name:str):
    books_list.append(book_name)
    return {"message":"Book added successfully"} 

# Update the list

@app.put('/books/{book_name}')
def update(book_name:str,new_book:str):
    for i in range(0,len(books_list)):
            if books_list[i] == book_name:
                 books_list[i] = new_book
            return {"message":"Book updated successfully"}
    return {"error":"Book not found"}

# Deletes item from list

@app.delete('/books/{book_name}')
def deletes(book_name: str):
    for i in range(0,len(books_list)):
        if books_list[i] == book_name:
            books_list.remove(books_list[i])
            return {"message":f"{book_name} removed successfully."}
    return {"error":f"{book_name} not found"}