from distutils.dir_util import copy_tree
import os

cwd = os.getcwd()

for entry in os.listdir():
    if not os.path.isfile(os.path.join(".", entry)):
        fromDirectory = "./" + entry
        toDirectory = "../calibre_usb"

        copy_tree(fromDirectory, toDirectory)