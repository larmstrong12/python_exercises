SEPERATE = "******************************"


def main_menu():
    print SEPERATE + "\nEXERCISE 4 - MENU\n" + SEPERATE
    print "1. Write input to file\n2. Write input to screen\n3. Quit\n" + SEPERATE


def main():
    main_menu()
    choice = None
    while choice is None:
        user_input = raw_input("Enter your choice [1-3]: ")
        if user_input in ["1", "2", "3"]:
            choice = user_input
        else:
            print "You entered an invalid choice."

    if choice in ["1", "2"]:
        user_input = raw_input("Enter a phrase: ")
        if choice == "1":
            with open("output.txt", "a") as f:
                f.write("\n" + user_input)
            if not f.closed:
                print "Done.\nFile will close on exit."
            else:
                print "Done."

        else:
            user_input = user_input.replace('\n')
            print "You entered:" + user_input
    else:
        print "Exiting"


main()