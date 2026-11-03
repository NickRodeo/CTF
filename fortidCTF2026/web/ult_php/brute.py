import hashlib

with open("/usr/share/wordlists/rockyou.txt", "r", errors="ignore") as f:
    for line in f:
        teks = "ULTIMATIVE-PHP-2026:" + line.strip()
        a = hashlib.md5(teks.encode("utf-8")).hexdigest()
        b = hashlib.sha256(teks.encode("utf-8")).hexdigest()
        if a[0] == "0" and a[1] == "e" and b[0] == "0" and b[1] == "e":
            valid_a = all(c in "0123456789" for c in a[2:9])
            valid_b = all(c in "0123456789" for c in b[2:9])
            print("Trying: ", teks)
            
            if valid_a and valid_b:
                print(f"[+] DITEMUKAN!")
                print(f"Teks : {teks}")
                print(f"MD5  : {a}")
                print(f"SHA256: {b}")
                break


#Recovered : 9302110163913021
