from flask import Flask, render_template, request, jsonify

app4 = Flask(__name__)

# Dummy data for demonstration
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"}
]

# Get all books 
@app4.route('/books',methods=['GET'])
def get_books():
    return books

# Get a specific book by ID
@app4.route('/books/<int:book_id>',methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id']==book_id:
            return book

# Create a new book
@app4.route('/books',methods=['POST'])
def create_book():
    new_book={'id':len(books)+1, 'title':request.json['title'],'author':request.json['author']}
    books.append(new_book)
    return new_book

# Update a book

@app4.route('/books/<int:book_id>',methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id']==book_id:
          book['title']=request.json['title']
          book['author']=request.json['author']
          return book
    return{'error':'Book not found'}


# Delete a book
@app4.route('/books/<int:book_id>',methods=['DELETE'])
def delete_book(book_id):
    for book in books:
         if book['id']==book_id:
            books.remove(book)
            return{"data":"Book Deleted Successfully"}
    return{'error':'Book not found'} 
        



# run the flask app
if __name__=='__main__':
    app4.run(debug=True)