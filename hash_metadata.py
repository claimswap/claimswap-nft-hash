import hashlib
concat = ""
for i in range(0, 10000):
    with open("generated/{}.json".format(i), "r") as f:
        line = f.readline()
        print(line)
        concat += line
    with open("hashes/{}".format(i), "w") as f:
        f.write(hashlib.sha256(line.encode()).hexdigest())
with open("hashes/concat", "w") as f:
    f.write(hashlib.sha256(concat.encode()).hexdigest())
