import stripe

stripe.api_key = "sk_test_your_api_key"

@app.route('/checkout', methods=['POST'])
def checkout():
    # Get the payment token submitted by the form:
    token = request.form['stripeToken']

    # Create a charge: this will charge the user's card
    try:
        charge = stripe.Charge.create(
            amount=999,
            currency='naira',
            description='Example charge',
            source=token,
        )
    except stripe.error.CardError as e:
        # The card has been declined
        pass
    # Create an order in the database
    order = Order(customer_id=current_user.id, total_cost=charge.amount, status='success')
    db.session.add(order)
    db.session.commit()
    return redirect(url_for('order', order_id=order.id))
