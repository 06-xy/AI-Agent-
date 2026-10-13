def level_c():
    result = int("abc")

def level_b():
    level_c()

def level_a():
    level_b()

if __name__ == "__main__":
    level_a()