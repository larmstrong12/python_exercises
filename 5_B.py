import string
import random
from collections import Counter

print "******************************"

print "********* EXERCISE 5 *********"

print "******************************"

print "\n**** BEGIN RANDOM STRING *****\n"

def main():
    with open("bible.txt", 'r') as f:
        count = 0
        for i in f:
            c = Counter(i)
            print i + ' '.join('{} ==> {}'.format(key, val) for key, val in c.items())
            print
            count += 1


if __name__ == '__main__': main()
print "*******************************"

