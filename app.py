from flask import Flask, render_template, request, redirect

app = Flask(__name__)

orders =  []

pwd = 'fake_password'  # Change this to your desired password
authToken = 0

@app.route('/check_orders')
def check_orders():
    global orders
    return {'orders': orders}

@app.route('/')
def index():
    return render_template('display.html', orders=orders)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    req = None
    if authToken == 0:
        return redirect('/login')
    if request.method == 'POST':
        print("POST request received")
        req = {"order_name": request.form.get('order_name')}
        print("Request:", req)
        if 'add' in request.form and req:
            print("Add request received")
            orders.append(req['order_name'])
            print("Order added:", req['order_name'])
        elif 'remove' in request.form and req:
            print("Remove request received")
            try:
                orders.remove(req['order_name'])
            except ValueError:
                pass
    return render_template('admin.html', orders=orders)

@app.route('/login', methods=['GET', 'POST'])
def login():
    global authToken
    if authToken == 1:
        return redirect('/admin')
    if request.method == 'POST':
        password = request.form.get('password')
        if password == pwd:
            authToken = 1
            return redirect('/admin')
        else:
            return "Password incorrect"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
