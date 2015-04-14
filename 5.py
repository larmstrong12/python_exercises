import string
import random
from collections import Counter



print "******************************"

print "********* EXERCISE 5 *********"

print "******************************"

print "\n**** BEGIN RANDOM STRING *****\n"


def random_string_generator():
    size = random.randint(1, 500)
    return "".join(random.choice(string.ascii_lowercase + string.ascii_uppercase)
                   for _ in range(size))

def main():
    with open("exercise_five.dat", "w+") as f:
        for x in range(0, 10):
            data = random_string_generator()
            f.write(data + "\n")
        f.close()
    with open("exercise_five.dat", 'r') as f:
        char_count = 0
        chars = ""
        for i in f.readlines():
            i = i.strip
            chars += i
            char_count += len(i)
            print i + "\n" + "*"*220 + "\nTotal Characters for the above string: " + str(len(i))

        print "\n" + "*"*220 + "\nTotal characters for all of the above strings: " + str(char_count)
        print Counter(char_count).most_common()


print "\n*******************************"

if __name__ == '__main__': main()







