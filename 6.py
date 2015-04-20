def first_file():
    pass

def second_file():
    try:
        f = open("text.txt", "r")
        f.write("This is a test")
    except:
        print IOError("This file does not exist")

def main():
    first_file()
    second_file()
    try:
        f = open("text.txt", "w")
        f.write("This is a test")
    except:
        print IOError("This file does not exist")