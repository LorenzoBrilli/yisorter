from os import listdir, getcwd
from os.path import isfile, join

#get files in directory
files = [f for f in listdir(getcwd()) if isfile(join(getcwd(), f))]
