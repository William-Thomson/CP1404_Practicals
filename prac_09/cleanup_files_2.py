"""
CP1404/CP5632 Practical
Demos of various os module examples
"""

import os


def main():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics/Old')
    print("Current Directory: {}".format(os.getcwd()))
    filename = os.listdir('.')[4]
    print(filename)
    new_name = get_fixed_filename(filename)
    print(new_name)


def get_fixed_filename(filename):
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    for i, current_character in enumerate(new_name):
        previous_character = new_name[i - 1]
        if current_character.isupper() and previous_character.islower():
            new_name = new_name.replace("{}{}".format(previous_character, current_character),
                                        "{}_{}".format(previous_character, current_character))

        print(previous_character, current_character)
    print(filename, new_name)
    return new_name


main()
