from flask import render_template
from app import app


@app.route('/books')
def index():
    return render_template('index.html', title='Home', books=books)