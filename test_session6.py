import requests
url = "http://127.0.0.1:5000/"
def test_login(username, password):
    data = {
        "username": username,
        "password": password
    }
    response  = requests.post(url, data=data)
    if "login success" in response.text:
        print(f"correct password is :{password}")
        return True
    else:
        print(f"{password} is incorrect")
        return False
    

test_login("user1", "salaam")
