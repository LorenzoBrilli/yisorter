from os import listdir, getcwd, remove
from os.path import isfile, join

#get files in directory
files = [f for f in listdir(getcwd()) if isfile(join(getcwd(), f))]

#get all interested file in different lists
photos = [f for f in files if ('.jpg' in f.lower())]
videos = [f for f in files if ('.mp4' in f.lower())]
thms = [f for f in files if ('.thm' in f.lower())]
secs = [f for f in files if ('.secs' in f.lower())]


print(thms)

#remove all thms and secs
for f in thms:
    remove(f)
for f in secs:
    remove(f)

print(photos)
print(videos)
print(thms)
print(secs)
