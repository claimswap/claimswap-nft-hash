import hashlib
success = 0
failure = 0
concat = ""
for i in range(0, 10000):
    with open("generated/{}.json".format(i), "r") as jsonf:
        with open("hashes/{}".format(i), "r") as hashf:
            line = jsonf.readline()
            concat += line
            first = hashf.readline()
            second = str(hashlib.sha256(line.encode()).hexdigest())
            if first != second:
                print("Validation Failure: Slime #{}: {} vs {}".format(i, first, second))
                failure += 1
            else:
                print("Success: Slime #{}".format(i))
                success += 1
print("{} success, {} failure".format(success, failure))

with open("hashes/concat", "r") as f:
    if f.readline() != hashlib.sha256(concat.encode()).hexdigest():
        print("Validate concatenated hash: failure")
    else:
        print("Validate concatenated hash: success")
