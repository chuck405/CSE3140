import time, subprocess

start = time.time()

for i in open("MostCommonPWs", "r"):
    subprocess.run(["python3", "Login.pyc", "Adam", i.strip()])
    print("Password: " + i.strip())
    print("Time Elapsed: ", time.time()-start)