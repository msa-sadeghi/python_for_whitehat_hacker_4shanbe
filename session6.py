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
app.secret_key = 'rrrrr'

html_form = '''
<form method="post">
{% if message %}
<p style="color:red"> {{ message}} </p>
{% endif %}
Username: <input type="text" name="username"><br>
Password: <input type="password" name="password"><br>
<input type="submit" value="Login">
</form>
'''

correct_username = "user1"
correct_password = "pass1"
attempts = 0
@app.route("/", methods=["GET", "POST"])
def login():
    global attempts

    message = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # فقط یک بار افزایش می‌دهیم
        attempts += 1
        if attempts > 2:
            message = "CAPTCHA created! لطفا ثابت کنید انسان هستید."
        elif username == correct_username and password == correct_password:
            message = "Login success!"
            attempts = 0
        else:
            message = "Invalid username or password."

    print("attempts", attempts)
    return render_template_string(html_form, message=message)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)