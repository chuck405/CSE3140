import time, subprocess

start = time.time()

for i in open("MostCommonPWs", "r"):
    for j in open("gang", "r"):
        subprocess.run(["python3", "Login.pyc", j.strip(), i.strip()])
        print("Name: " + j.strip() + ", Password: " + i.strip())
        print("Time Elapsed: ", time.time()-start)
