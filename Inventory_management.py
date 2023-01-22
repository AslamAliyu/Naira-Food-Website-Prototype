class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_id = db.Column(db.Integer, db.ForeignKey('food.id'), nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    reorder_level = db.Column(db.Integer, nullable=False)

@app.route('/inventory')
def inventory():
    inventory = Inventory.query.all()
    return render_template('inventory.html', inventory=inventory)

@app.route('/inventory/<int:food_id>')
def food_inventory(food_id):
    inventory = Inventory.query.filter_by(food_id=food_id).first()
    return render_template('food_inventory.html', inventory=inventory)

@app.route('/update_inventory', methods=['POST'])
def update_inventory():
    food_id = request.form.get('food_id')
    stock_quantity = request.form.get('stock_quantity')
    reorder_level = request.form.get('reorder_level')
    inventory = Inventory.query.filter_by(food_id=food_id).first()
    inventory.stock_quantity = stock_quantity
    inventory.reorder_level = reorder_level
    db.session.commit()
    return redirect(url_for('inventory'))

@app.route('/add_to_inventory', methods=['POST'])
def add_to_inventory():
    food_id = request.form.get('food_id')
    stock_quantity = request.
