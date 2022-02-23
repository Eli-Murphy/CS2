import requests


def createUser():
    url = "https://www.realizefi.com/api/users"

    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer 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"
    }

    response = requests.request("POST", url, headers=headers)

    print(response.text)

def listUser():
    url = "https://www.realizefi.com/api/users"

    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer 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"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

def dcInst():
    userId = input("User ID: ")
    instId = input("Inst ID: ")

    url = "https://www.realizefi.com/api/users/" + userId + "/institution_links/" + instId

    headers = {"Authorization": "Bearer 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"}

    response = requests.request("DELETE", url, headers=headers)

    print(response.text)

def userGet():
    userId = input("User ID: ")

    url = "https://www.realizefi.com/api/users/"+ userId

    headers = {
    "Accept": "application/json",
    "Authorization": "Bearer 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"
}

    response = requests.request("GET", url, headers=headers)

    print(response.text)

def delUser():
    userId = input("User ID: ")

    url = "https://www.realizefi.com/api/users/" + userId

    headers = {"Authorization": "Bearer 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"}

    response = requests.request("DELETE", url, headers=headers)

    print(response.text)

def authPortal():
    userId = input("User ID: ")

    url = "https://www.realizefi.com/api/users/"+userId+"/auth_portals"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"
    }

    response = requests.request("POST", url, headers=headers)

    print(response.text)

