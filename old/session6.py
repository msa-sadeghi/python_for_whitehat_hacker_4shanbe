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


from flask import Flask, request, render_template_string, send_file
from PIL import Image, ImageDraw, ImageFont
import io
import random
import string

def generate_captcha_text(length=5):
    return "".join(random.choices(string.ascii_uppercase + \
                          string.digits, k = length))


def generate_captcha_image(text):
    img = Image.new('RGB', (150, 60), color=(255, 255,255))
    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    d.text((10, 10), text, font=font, fill=(0,0,0))
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return buf


app = Flask(__name__)
app.secret_key = 'rrrrr'

html_form = '''
<form method="post">
{% if message %}
<p style="color:red"> {{ message}} </p>
{% endif %}
Username: <input type="text" name="username"><br>
Password: <input type="password" name="password"><br>
{% if show_captcha %}
<img src="{{url_for('captcha_image')}}" alt="CAPTCHA"><br><br>
Captcha: <input type="text" name="captcha"><br>
{% endif %}

<input type="submit" value="Login">
</form>
'''


@app.route("/captcha.png")
def captcha_image():
    global text
    img = generate_captcha_image(text)
    return send_file(img, mimetype='image/png')



correct_username = "user1"
correct_password = "pass1"
attempts = 0
text = ""
show_captcha = False
@app.route("/", methods=["GET", "POST"])
def login():
    global attempts
    global show_captcha
    global text

    message = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # فقط یک بار افزایش می‌دهیم
        attempts += 1
        if attempts > 2:
            show_captcha = True
            message = "CAPTCHA created! لطفا ثابت کنید انسان هستید."
            text = generate_captcha_text()
            user_text = request.form.get("captcha", "")
            if user_text != text:
                message = "Wrong Captcha"

        elif username == correct_username and password == correct_password:
            message = "Login success!"
            attempts = 0
        else:
            message = "Invalid username or password."

    print("attempts", attempts)
    return render_template_string(html_form, message=message,\
                                   show_captcha=show_captcha)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)