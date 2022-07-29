def take_pass():
    """
    takes password from file
    """
    with open(r"C:\\password.txt", 'r') as p:
        password = p.readline()
    return password


if __name__ == "__main__":
    take_pass()
