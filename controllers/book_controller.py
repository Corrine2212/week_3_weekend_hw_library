from flask import render_template, request, redirect
from app import app
from models.books import books, add_new_book, delete_book
from models.book import *

@app.route('/books')
def all_books():
    return render_template('/index.html', title="Home", books=books)

@app.route('/books/add', methods=['POST'])
def add_new_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    description = request.form['description']
    new_book = Book(title=title, author=author, genre=genre, description=description)
    add_new_book(new_book)
    return redirect('/books')

@app.route('/books/delete/<title>', methods=['POST'])
def delete(title):
    delete_book(title)
    return redirect('/books')