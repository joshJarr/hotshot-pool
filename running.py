import sched, time
import os
from multiprocessing import Process
from time import sleep

s = sched.scheduler(time.time, time.sleep)
def recordStream(sc): 
    print "Capturing..."
    os.system("sudo streamer -q -c /dev/video0 -s 640x480 -f jpeg -t 0:10 -r 12 -j 75 -w 0 -o /mnt/ramdisk/tmp.avi")
    s.enter(12, 1, recordStream, (sc,))

s.enter(12, 1, recordStream, (s,))
s.run()
