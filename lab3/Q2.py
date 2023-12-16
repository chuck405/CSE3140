import os, hashlib

file_list = os.listdir('/home/cse/Lab3/Q2files/')
for i in file_list:
    with open(os.path.join('/home/cse/Lab3/Q2files/', i), "rb") as file:
        contents = file.read()
        sha256 = hashlib.sha256()
        sha256.update(contents)
        if sha256.hexdigest() == "9057f7679cc2d6c15a1e6cf9c67b80cbdbeb997d2b9a3e5e84579b2f82ff8631":
            print(i)


