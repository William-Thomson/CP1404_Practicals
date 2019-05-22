import os
import shutil


def main():
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('FilesToSort')
    print("New directory is: {}".format((os.getcwd())))


main()
