"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # renames the files as the program walks
        for filename in filenames:
            old_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            print("Renaming {} to {}".format(old_name, new_name))
            os.rename(old_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename
    for i, current_character in enumerate(filename):
        previous_character = filename[i - 1]
        if current_character.isupper():
            if previous_character.islower():
                new_name = filename.replace("{}{}".format(previous_character, current_character),
                                            "{}_{}".format(previous_character, current_character)).replace(" ",
                                                                                                           "_").replace(
                    ".TXT", ".txt")
                print("{}{}".format(previous_character, current_character))
    return new_name


main()
