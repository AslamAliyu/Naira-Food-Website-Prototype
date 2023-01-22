class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    total_cost = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    foods = db.relationship('Food', secondary=order_items, backref=db.backref('orders', lazy=True))
    customer = db.relationship("Customer", back_populates="orders")

@app.route('/orders')
def orders():
    orders = Order.query.all()
    return render_template('orders.html', orders=orders)

@app.route('/order/<int:order_id>')
def order(order_id):
    order = Order.query.get(order_id)
    return render_template('order.html', order=order)

@app.route('/create_order', methods=['POST'])
def create_order():
    customer_id = request.form.get('customer_id')
    total_cost = request.form.get('total_cost')
    status = request.form.get('status')
    foods = request.form.getlist('foods')
    order = Order(customer_id=customer_id, total_cost=total_cost, status=status, foods=foods)
    db.session.add(order)
   
