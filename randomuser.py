import requests

reponse = requests.get("https://randomuser.me/api/", params={"results": 100, "gender": "male"})

data = reponse.json()



for user in data["results"]:
    gender = user["gender"]
    name = user["name"]["title"] + " " + user["name"]["first"] + " " + user["name"]["last"]
    email = user["email"]

    print(f"Name: {name} Gender: {gender} Email: {email}")
