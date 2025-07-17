# password = input("enter your pass: ")
# if len(password) >= 8:
#     print("strong")
# else:
#     print("weak")


# import re
# score = 0
# password = input("enter your pass: ")
# if len(password) >= 8:
#     score += 1
# if re.search(r"[A-Z]", password):
#     score += 1
# if re.search(r"[0-9]", password):
#     score += 1
# if re.search(r"[!@#$%^&*]", password):
#     score += 1
# print(score)


# import random
# import string
# import pyperclip
# def generate_password():
#     chars = string.ascii_letters + string.digits + string.punctuation
#     password = "".join(random.choice(chars) for _ in range(12))
#     pyperclip.copy(password)
#     return password
# print(generate_password())



# from fpdf import FPDF

# report = FPDF()
# report.add_page()
# report.set_font("Arial", size=14)
# password = input("enter the pass: ")
# report.cell(200, 10, txt="report", ln=True)
# report.cell(200, 10, txt=password, ln=True)
# report.output("report.pdf")