from flask import Flask, request, jsonify
from db import get_connection

app = Flask(__name__)

@app.route('/')
def home():
    return "Library API is running "

# 👉 ADD BOOK API
@app.route('/add-book', methods=['POST'])
def add_book():
    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO book (title, author, price, pages, publisher, edition, status)
    VALUES (%s, %s, %s, %s, %s, %s, 'available')
    """

    values = (
        data['title'],
        data['author'],
        data['price'],
        data['pages'],
        data['publisher'],
        data['edition']
    )

    cursor.execute(sql, values)
    conn.commit()

    return jsonify({"message": "Book added successfully"})

if __name__ == "__main__":
    app.run(debug=True)