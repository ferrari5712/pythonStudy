import json

print("hello")


def write_json(filename, data):
    with open(filename, "w") as f:
        f.write(json.dumps(data))

    f.close()


def read_json(filename):
    pass


write_json("test.json", "hello")
