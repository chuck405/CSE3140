import time, subprocess

start = time.time()

for i in open("PwnedPWfile", "r"):
    for j in open("gang", "r"):
        subprocess.run(["python3", "Login.pyc", j.strip(), i.strip()[i.strip().index(",")+1::]])
        print("Name: " + j.strip() + ", Password: " + i.strip()[i.strip().index(",")+1::])
        print("Time Elapsed: ", time.time()-start)
