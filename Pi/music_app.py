import subprocess
import time
import os
import signal

#uncomment on pi
#music = subprocess.Popen("mplayer 'partySong.mp3'", stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
print "Hello!"
time.sleep(5)
#os.killpg(music.pid, signal.SIGTERM) 
print "I can keep doing other stuff now!"
