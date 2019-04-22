#!/usr/bin/python3

"""
myfile = open("myfile.txt", "w")
myfile.write("Firstline in the file\n")
myfile.close()
"""

with open("myfile.txt", "w") as myfile:
    myfile.write("Firstline in the file\n")
