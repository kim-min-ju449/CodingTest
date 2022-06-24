import json

user = {
    "id":"summer",
    "password":"123456",
    "age":"30",

}
with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file, indent=4)