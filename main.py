from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_order')
def new_order():
    return render_template('new_order.html')

@app.route('/all_orders')
def all_orders():
    return render_template('all_orders.html')

@app.route('/clients')
def clients():
    return render_template('clients.html')

@app.route('/payments')
def payments():
    return render_template('payments.html')

if __name__ == '__main__':
    app.run(debug=True)