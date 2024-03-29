from flask import Flask, render_template, request, Response
from flask_sqlalchemy import SQLAlchemy
import json
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///system.db'
db = SQLAlchemy(app)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    address = db.Column(db.String(150))

    def to_json(self):
        return {"id": self.id, "name": self.name, "email": self.email, "address": self.address}

# Select All
@app.route('/customers', methods=['GET'])
def get_all_customers():
    customer_data = Customer.query.all()
    customer_json = [data.to_json() for data in customer_data]
    return json.dumps(customer_json)

# Select One
@app.route('/customer/<int:id>', methods=['GET'])
def get_customers(id):
    pass

# Add
@app.route('/customer', methods=['POST'])
def add_customer():
    form = request.form.to_dict(flat=False)
    name = form['name'][0]
    email = form['email'][0]
    address = form['address'][0]

    new_customer = Customer(name=name, email=email, address=address)
    db.session.add(new_customer)   
    db.session.commit()
    customer_data = Customer.query.all()
    return render_template('index.html', data=customer_data)

# Update

# Delete


@app.route('/', methods=['GET'])
def index_html():
    customer_data = Customer.query.all()
    return render_template('index.html', data=customer_data)


if __name__ == '__main__':
    app.run(debug=True)
    print("Server running")
