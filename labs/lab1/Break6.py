import time, subprocess, hashlib

start = time.time()

hashed_dict = {}
for i in open("SaltedPWs", "r"):
    name = i.strip()[0:i.strip().index(",")]
    i = i.strip()[i.strip().index(",")+1:]
    salt = i.strip()[0:i.strip().index(",")]
    i = i.strip()[i.strip().index(",")+1:]
    salt_pw = i.strip()
    if name not in hashed_dict: hashed_dict[name] = set()
    hashed_dict[name].add((salt, salt_pw))

for j in open("PwnedPWs100k", "r"):
    for i in open("gang", "r"):
        if i.strip() in hashed_dict:
            for k in range(0,10):
                for l in hashed_dict[i.strip()]:
                    sha256 = hashlib.sha256()
                    curr = l[0] + j.strip() + str(k)
                    sha256.update(bytes(curr, "utf-8"))
                    if sha256.hexdigest() == l[1]:
                        subprocess.run(["python3", "Login.pyc", i.strip(), str(j.strip() + str(k))])
                        print("Name: " + i.strip() + ", Password: " + str(j.strip() + str(k)))
                        print("Time Elapsed: ", time.time()-start)
