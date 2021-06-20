with open("users.json", "r") as json_data:
    users = json.load(json_data)
print(len(users["users"]))
