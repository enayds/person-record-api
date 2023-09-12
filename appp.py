from flask import Flask, jsonify, request

app = Flask(__name__)

# sample data to use

books = [
    {"id":1, "title":"Book 1", "author": "Author 1"},
    {"id":2, "title":"Book 2", "author": "Author 2"},
    {"id":3, "title":"Book 3", "author": "Author 3"},
]

# Get all books
@app.route('/', methods = ["GET"])
def get_books():
    return books

# Get a specific book based on ID supplied
@app.route('/books/<int:book_id>', methods = ["GET"])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return book
    return '{"error, book not found"}, 404'

# create a book
@app.route('/books', methods = ["POST"])
def create_book():
    new_book =  {"id":len(books) + 1, "title":request.json['title'], "author": request.json["author"]}
    books.append(new_book)
    return {"Insertion Succesful": new_book}


# update a book
@app.route('/books/<int:book_id>', methods = ["PUT"])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            book['title'] = request.json['title']
            book['author'] = request.json['author']
            return {"Update Succesful": book}
    return '{"error, book not found"}, 404'

# delete a book
@app.route('/books/<int:book_id>', methods = ["DELETE"])
def delete_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {"Deletion Succesful": book}
    return '{"error, book not found"}, 404'

if __name__ == "__main__":
    app.run(debug=True)