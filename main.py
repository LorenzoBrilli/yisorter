"""
    yisorter
    sort utility from files coming from yi camera

    author: Lorenzo Brilli
"""

from os import listdir, getcwd, remove, mkdir
from os.path import isfile, join

#get files in directory
files = [f for f in listdir(getcwd()) if isfile(join(getcwd(), f))]

#get all interested file in different lists
photos = [f for f in files if (('.jpg' in f.lower()) or ('.dng' in f.lower()))]
videos = [f for f in files if ('.mp4' in f.lower())]
thms = [f for f in files if ('.thm' in f.lower())]
secs = [f for f in files if ('.secs' in f.lower())]

#sort files
p_photos = [f for f in photos if (f.lower()[:4]=='ydxj')]
p_bursts = [f for f in photos if (f.lower()[:1]=='c')]
p_timelapses = [f for f in photos if (f.lower()[:1]=='y' and f.lower()[1:2]!='d')]


#remove all thms and secs
for f in thms:
    remove(f)
for f in secs:
    remove(f)
