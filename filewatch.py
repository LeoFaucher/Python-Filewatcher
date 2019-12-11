import sys

"""Python File Watcher
"""


def app_start_message():
    # Messages shown once launching the app
    print("\nThis a python file watcher")
    print("The project was developed by Leo Aka YRM and Jacky for a school project")
    print("To use the file watcher simply write \"filewatch\" and enter the path of your folder/file \n")


def help_message():
    # Helper messages to get some knowledge before using the app
    print("\nHere's some tips you may need to use the file watcher: \n")
    print("Use -d or --directory <name of the directory> to select a directory to monitor")
    print("Use -i or --interval <number of seconds> to set a timer before each monitoring (time in second)")
    print("Use -c or --config <name of the configuration file> to select a configuration file for your monitor")
    print("Use -l or --logging <name of the logging file> to select a logging file \n")

    # Input command to start using the file watcher
    y = input("Start using the file watcher by using of these commands \n\n")

    # Need to implement a switch case depending of what the user type to start the file watcher
    print(y)


app_start_message()

# Input command to start using the file watcher or get help
x = input("To get help just type --help: \n\n")

if x == "--help":
    help_message()

