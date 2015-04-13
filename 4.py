import time
import sys


def main_menu():
    print "Menu\n1. Write input to file\n2. Write input to screen\n3. Quit"


def main():
    main_menu()
    choice = None
    while choice is None:
        user_input = raw_input("Please enter your choice: ")
        if user_input in ["1", "2", "3"]:
            choice = user_input
        else:
            print "You entered an invalid choice."
            time.sleep(3)
            main_menu()

    if choice in ["1", "2"]:
        user_input = raw_input("Enter the text you want to save: ")
        if choice == "1":
            with open("output.txt", "a") as f:
                f.write("\n" + user_input)
            if not f.closed:
                print "Done.\nFile will close on exit."
            else:
                print "Done."
            time.sleep(5)
            main()

        else:
            user_input = user_input.replace('\n')
            print user_input
            time.sleep(5)
            main()
    else:
        print "Exiting"
        time.sleep(3)
        sys.exit(0)

if __name__ == '__main__':
    main()