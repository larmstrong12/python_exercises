import string
import random

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
            ran_string_length = len(i)
            print i
            count += 1

if __name__ == '__main__': main()
print "\n*******************************"






