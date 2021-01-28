import requests

def searchTrain(url, train_name):
    payload = "{\r\n    \"search\": \""+train_name+"\"\r\n}"

    headers = {
        'content-type': "application/json",
        'x-rapidapi-key': "0267e9fba2msh9bb91d9e84501e9p1eb587jsnb2a86b6ae3c3",
        'x-rapidapi-host': "trains.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.text