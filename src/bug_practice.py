def bug1_key_error():
    s = {"name": "Alice"}
    return s["score"]

def bug2_type_error():
    return 10 + "20"

def bug3_index_error():
    return [][0]

if __name__ == "__main__":
    bug1_key_error()