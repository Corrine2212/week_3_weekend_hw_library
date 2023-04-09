from flask import render_template, request, redirect
from app import app
from models.books import books, add_new_book, delete_book, find_book_by_id
from models.book import *
import datetime

@app.route('/books')
def index():
    return render_template('index.html', title='Home', books=books)

@app.route('/books', methods=['POST'])
def add_book():
  new_id = len(books) + 1
  date = request.form['date']
  split_date = date.split('-')
  date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
  title = request.form['title']
  author = request.form['author']
  checkedin = True if 'checkedin' in request.form else False
  genre = request.form['genre']
  description = request.form['description']
  newbook = Book(id=new_id, date=date, title=title, author=author, checkedin=checkedin, genre=genre, description=description)
  add_new_book(newbook)
  return redirect('/books')

@app.route('/books/delete/<title>', methods=['POST'])
def delete(title):
  delete_book(title)
  return redirect('/books')

# @app.route('/books/<int:id>')
# def single_order(book_id):
#     books = find_book_by_id(book_id)
#     return render_template("single_book.html", title="Single Book", books=books)

@app.route('/books/<int:book_id>')
def show_book(book_id):
    books = find_book_by_id(book_id)
    return render_template('single_book.html', book=books)
