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



from flask import Flask, request, render_template_string
app = Flask(__name__)
html_form = '''
<form method="post">
username : <input type="text" name="username"><br>
password : <input type="password" name="password"><br>
<input type ="submit" value="login">
</form>
'''
correct_username = "user1"
correct_password = "pass1"
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == correct_username and password == correct_password:
            return "login success"
        else:
            return "invalid" 
    return render_template_string(html_form)
app.run(debug=True)