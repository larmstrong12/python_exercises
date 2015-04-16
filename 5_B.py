import string
import random
from collections import Counter

print "******************************"

print "********* EXERCISE 5 *********"

print "******************************"

print "\n**** BEGIN RANDOM STRING *****\n"


def random_string_generator():
    size = random.randint(20, 80)
    return "".join(random.choice(string.ascii_lowercase + string.ascii_uppercase)
                   for _ in range(size))


def main():
    with open("exercise_five.dat", "w+") as f:
        for x in range(0, 10):
            data = random_string_generator()
            f.write(data + "\n")
        f.close()
    with open("exercise_five.dat", 'r') as f:
        count = 0
        for i in f:
            c = Counter(i)
            print i + ' '.join('{} ==> {}'.format(key, val) for key, val in c.items())
            print
            count += 1


if __name__ == '__main__': main()
print "*******************************"

