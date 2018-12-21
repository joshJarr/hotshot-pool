import os
import time
import requests

while(True):
    user = raw_input("type in enter")
    if user == "enter":
        print "you pressed enter"
        os.system("sudo ffmpeg -i /mnt/ramdisk/tmp.avi -preset ultrafast -crf 27 /mnt/ramdisk/output.mp4")
    else:
        print "you haven't pressed enter"
        os.system("sudo ffmpeg -i /mnt/ramdisk/tmp.avi -preset ultrafast -crf 27 /mnt/ramdisk/output.mp4 -y")
        time.sleep(30)
        my_file = {
            'file' : ('/mnt/ramdisk/output.mp4', open('/mnt/ramdisk/output.mp4', 'rb'), 'mp4')
        }

        payload={
            "filename":"output.mp4", 
            "token":"<token goes here>", 
            "channels":['#hotshot-test'], 
        }

        r = requests.post("https://slack.com/api/files.upload", params=payload, files=my_file)

