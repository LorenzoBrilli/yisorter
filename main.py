"""
    yisorter
    sort utility from files coming from yi camera

    author: Lorenzo Brilli
"""

from os import listdir, getcwd, remove, mkdir, rename
from os.path import isfile, join

#get files in directory
files = [f for f in listdir(getcwd()) if isfile(join(getcwd(), f))]

#get all interested file in different lists
photos = [f for f in files if (('.jpg' in f.lower()) or ('.dng' in f.lower()))]
videos = [f for f in files if ('.mp4' in f.lower())]
thms = [f for f in files if ('.thm' in f.lower())]
secs = [f for f in files if ('.sec' in f.lower())]

#sort modalities
p_photos = [f for f in photos if (f.lower()[:4]=='ydxj')]
p_bursts = [f for f in photos if (f.lower()[:1]=='c')]
p_timelapses = [f for f in photos if (f.lower()[:1]=='y' and f.lower()[1:2]!='d')]
p_photofromvideos = [f for f in photos if (f.lower()[:1]=='t')]
v_videos = [f for f in videos if ((f.lower()[:4]=='ydxj') or (f.lower()[:2]=='yn'))]
v_timelapses = [f for f in videos if ((f.lower()[:4]=='ydtl') or (f.lower()[:2]=='yt'))]
v_loop = [f for f in videos if (f.lower()[:1]=='l')]
v_videoandphotos = [f for f in videos if (f.lower()[:2]=='yp')]
v_slowmotion = [f for f in videos if ((f.lower()[:2]=='ys'))]

#create photo and video directories
if (len(photos)>0):
    try:
        mkdir('photos')
    except:
        pass
if (len(videos)>0):
    try:
        mkdir('videos')
    except:
        pass

#sort files
for f in p_photos:
    rename(f,('photos/photo_'+f[4:]).lower())
for f in p_bursts:
    rename(f,('photos/burst_'+f[1:4]+'_'+f[4:]).lower())
for f in p_timelapses:
    rename(f,('photos/timelapse_'+f[1:4]+'_'+f[4:]).lower())
for f in p_photofromvideos:
    rename(f,('photos/photofromvideo_'+f[1:4]+'_'+f[4:]).lower())
for f in v_videos:
    dest = f
    if (f[2:4].lower() == 'xj'):
        dest = f[:2] + '00' + f[4:]
    rename(f,('videos/video_'+dest[4:8]+'_'+dest[2:4]+dest[8:]).lower())
for f in v_timelapses:
    dest = f
    if (f[2:4].lower() == 'tl'):
        dest = f[:2] + '00' + f[4:]
    rename(f,('videos/timelapse_'+dest[4:8]+'_'+dest[2:4]+dest[8:]).lower())
for f in v_loop:
    rename(f,('videos/loop_'+f[4:8]+'_'+f[1:4]+f[8:]).lower())
for f in v_videoandphotos:
    dest = f
    if (f[2:4].lower() == 'xj'):
        dest = f[:2] + '00' + f[4:]
    rename(f,('videos/videowphotos_'+dest[4:8]+'_'+dest[2:4]+dest[8:]).lower())
for f in v_slowmotion:
    dest = f
    if (f[2:4].lower() == 'xj'):
        dest = f[:2] + '00' + f[4:]
    rename(f,('videos/slowmotion_'+dest[4:8]+'_'+dest[2:4]+dest[8:]).lower())


#remove all thms and secs
for f in thms:
    remove(f)
for f in secs:
    remove(f)
