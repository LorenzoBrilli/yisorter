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

#create photo and video directories
if (len(photos)>0):
    mkdir('photos')
if (len(videos)>0):
    mkdir('videos')

#sort modalities
p_photos = [f for f in photos if (f.lower()[:4]=='ydxj')]
p_bursts = [f for f in photos if (f.lower()[:1]=='c')]
p_timelapses = [f for f in photos if (f.lower()[:1]=='y' and f.lower()[1:2]!='d')]
p_photofromvideos = [f for f in photos if (f.lower()[:1]=='t')]
v_videos = [f for f in videos if ((f.lower()[:4]=='ydxj') or (f.lower()[:2]=='yn') or (f.lower()[:2]=='yp'))]
v_timelapses = [f for f in videos if ((f.lower()[:4]=='ydtl') or (f.lower()[:2]=='yt'))]
v_slowmotion = [f for f in videos if ((f.lower()[:2]=='ys'))]


#remove all thms and secs
for f in thms:
    remove(f)
for f in secs:
    remove(f)
