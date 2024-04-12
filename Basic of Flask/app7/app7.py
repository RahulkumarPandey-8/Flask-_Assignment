
# Q7. Integrate a SQLite database with Flask to perform CRUD operations on a list of items.

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app7 = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('items.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize database
def init_db():
    conn = get_db_connection()
    with app7.open_resource('schema.sql', mode='r') as f:
        conn.cursor().executescript(f.read())
    conn.commit()
    conn.close()

# Check if database exists, if not, initialize it
if not os.path.exists('items.db'):
    init_db()

@app7.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    conn.close()
    return render_template('index.html', items=items)

@app7.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO items (name, price) VALUES (?, ?)', (name, price))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')

@app7.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit(item_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items WHERE id = ?', (item_id,))
    item = cursor.fetchone()
    conn.close()
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        cursor = conn.cursor()
        cursor.execute('UPDATE items SET name = ?, price = ? WHERE id = ?', (name, price, item_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('edit.html', item=item)

@app7.route('/delete/<int:item_id>', methods=['GET', 'POST'])
def delete(item_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM items WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app7.run(debug=True)
