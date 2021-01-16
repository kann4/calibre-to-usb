#"calibre_usb" is created on same level as working folder
from distutils.dir_util import copy_tree
import os
import sys
from send2trash import send2trash

to_be_del = []
if len(sys.argv) == 2:
    wd = sys.argv[1]
else:
    wd = input("to continue, press enter (or specify directory):")
if os.path.exists(wd) or wd == "":
    if not wd == "":
        os.chdir(wd)
    else:
        wd = "."
    for entry in os.listdir(wd):
        if not os.path.isfile(os.path.join(".", entry)) and entry != ".git":
            fromDirectory = "./" + entry
            toDirectory = "../calibre_usb"
            # copy_tree(fromDirectory, toDirectory)
            print('from:' + fromDirectory + '; to: ' + toDirectory)
            to_be_del.append(entry)
    print('-----------------------------------')
    for i in range(len(to_be_del)):
        print(to_be_del[i])
    print("sure to delete above items?")
    confirm = input()
    if confirm == "":
        print('to delete')
        for i in range(len(to_be_del)):
            # send2trash("./"+to_be_del[i])   #need"./"?
            print("./"+to_be_del[i])
    else:
        print("items kept.")
else:
    print("invalid path")


#allow multiple attempt if typo


