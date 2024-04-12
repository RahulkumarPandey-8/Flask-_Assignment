
# Q7. Integrate a SQLite database with Flask to perform CRUD operations on a list of items.



from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
db = SQLAlchemy(app)

# Define Item model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return f"Item(id={self.id}, name='{self.name}', description='{self.description}')"

# Create the database tables
db.create_all()

# Routes for CRUD operations
@app.route('/')
def index():
    # Fetch all items from the database
    items = Item.query.all()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    name = request.form['name']
    description = request.form['description']
    new_item = Item(name=name, description=description)
    db.session.add(new_item)    
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = Item.query.get_or_404(item_id)
    if request.method == 'POST':
        item.name = request.form['name']
        item.description = request.form['description']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', item=item)

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
