# def login(password):
#     correct_password = "1234"
#     if password == correct_password:
#         return"success"
#     else:
#         return"unsuccess"

# def brute_force():
#     passwords = ["123", "password", "admin", "1234", "abcd"]
#     for p in passwords:
#         if login(p) == "success":
#             print(f"password is : {p}")
#             break
#     else:
#         print("password not found")

# brute_force()



from flask import Flask, request, render_template_string, session
app = Flask(__name__)
app.secret_key = 'rrrrr'
html_form = '''
<form method="post">
{% if message %}
<p style="color:red"> {{ message}} </p>
{% endif %}
username : <input type="text" name="username"><br>
password : <input type="password" name="password"><br>
<input type ="submit" value="login">
</form>
'''
correct_username = "user1"
correct_password = "pass1"
@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if "attempts" not in session:
        session["attempts"] = 0
    if request.method == "POST":
        session["attempts"] += 1
        username = request.form.get("username")
        password = request.form.get("password")
        if session["attempts"] > 2:
            message = "captcha created"
            print("========================")
        elif username == correct_username and password == correct_password:
            message = "login success"
            session["attempts"] = 0
        else:
            session["attempts"] += 1
            return "invalid" 
    return render_template_string(html_form, message = message)
app.run(debug=True)