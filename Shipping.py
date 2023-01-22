class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    shipping_address = db.Column(db.String(200), nullable=False)
    tracking_number = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    order = db.relationship("Order", back_populates="shipments")

@app.route('/shipments')
def shipments():
    shipments = Shipment.query.all()
    return render_template('shipments.html', shipments=shipments)

@app.route('/shipment/<int:shipment_id>')
def shipment(shipment_id):
    shipment = Shipment.query.get(shipment_id)
    return render_template('shipment.html', shipment=shipment)

@app.route('/create_shipment', methods=['POST'])
def create_shipment():
    order_id = request.form.get('order_id')
    shipping_address = request.form.get('shipping_address')
    tracking_number = request.form.get('tracking_number')
    status = request.form.get('status')
    shipment = Shipment(order_id=order_id, shipping_address=shipping_address, tracking_number=tracking_number, status=status)
    db.session.add
