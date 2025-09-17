import requests
from tqdm import tqdm
import time
import json
from PIL import Image
import pytesseract
from io import BytesIO


url = "http://127.0.0.1:5000/"


def solve_captcha():
    # r = requests.get(url + "captcha.png")
    # img = Image.open(BytesIO(r.content))
    img = Image.open("./captcha.png")
    text = pytesseract.image_to_string(img)
    return text

print(solve_captcha())


# def test_login(username, password_list):

#     results = []
#     for password in tqdm(password_list):
#         data = {
#             "username": username,
#             "password": password
#         }
#         response  = requests.post(url, data=data)
#         print("----------", "CAPTCHA" in response.text)
#         if "CAPTCHA" in response.text:
#             print(f"captcha created ")
#             time.sleep(4)
#             continue
#         if "login success" in response.text:
#             print(f"correct password is :{password}")
#             results.append({"username": username, "password":password, "success":True})
#             break
#         time.sleep(0.1)
#         # else:
#         #     print(f"{password} is incorrect")
#         #     return False
#     with open("results.json", "w") as f:
#         json.dump(results, f, indent=4, ensure_ascii=False)
    
# password_list = ["1234", "password", "blalalal","sssss", "pass1"]
# test_login("user1", password_list)
