from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nairafoods.db'
db = SQLAlchemy(app)

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Food('{self.id}', '{self.name}', '{self.price}','{self.category}')"

@app.route('/')
def index():
    foods = Food.query.all()
    return render_template('index.html', foods=foods)

@app.route('/food/<int:id>')
def food(id):
    food = Food.query.get(id)
    return render_template('food.html', food=food)

@app.route('/menu')
def menu():
    categories = Food.query.with_entities(Food.category).distinct()
    return render_template('menu.html', categories=categories)

@app.route('/menu/<string:category>')
def food_by_category(category):
    foods = Food.query.filter_by(category=category)
    return render_template('menu.html', foods=foods, category=category)

@app.route('/cart')
def cart():
    foods = Food.query.filter(Food.id.in_(request.args.getlist('food_id')))
    return render_template('cart.html', foods=foods)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    food_id = request.form.get('food_id')
    return redirect(url_for('cart', food_id=food_id))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
