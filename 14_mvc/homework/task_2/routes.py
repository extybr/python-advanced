from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

from typing import List

from models import init_db, get_all_books, DATA, insert_db

app: Flask = Flask(__name__)


class RegistrationForm(FlaskForm):
    book_title = StringField(validators=[InputRequired('не должно быть пустым')])
    author_name = StringField(validators=[InputRequired('не должно быть пустым')])


def _get_html_table_for_books(books: List[dict]) -> str:
    table = """
<table>
    <thead>
    <tr>
        <th>ID</td>
        <th>Title</td>
        <th>Author</td>
    </tr>
    </thead>
    <tbody>
        {books_rows}
    </tbody>
</table>
"""
    rows: str = ''
    for book in books:
        rows += '<tr><td>{id}</tb><td>{title}</tb><td>{author}</tb></tr>'.format(
            id=book['id'], title=book['title'], author=book['author']
        )
    return table.format(books_rows=rows)


@app.route('/books')
def all_books() -> str:
    return render_template('index.html', books=get_all_books())


@app.route('/books/form', methods=['GET', 'POST'])
def get_books_form() -> str:
    form = RegistrationForm()
    match request.method:
        case 'GET':
            return render_template('add_book.html')
        case 'POST':
            if form.validate_on_submit():
                insert_db(form.data)
                return "<h1><font color='green'>Book added to library</font></h1>"
    error: str = ''
    for key, value in form.errors.items():
        error += f"<p>{key}: <font color='red'>{value[0]}</font></p>"
    return f"<h1>Invalid input,{error}</h1>"



if __name__ == '__main__':
    init_db(DATA)
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
