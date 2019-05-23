import os
import shutil


def main():
    extensions_to_category = {}
    os.chdir('FilesToSort')
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]
        if extension not in extensions_to_category:
            category = input("What category would you like to sort {} files into?".format(extension))
            extensions_to_category[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass
        shutil.move(filename, extensions_to_category[extension])


main()
