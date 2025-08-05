import os
import time

STREAM_KEY = "dtr3-w144-392p-8x4x-75cf"  # Replace with your key
THUMBNAIL = "thumbnail.jpg"

MP3_FILES = ["song.mp3"]

while True:
    for file in MP3_FILES:
        os.system(f'ffmpeg -re -loop 1 -i {THUMBNAIL} -i {file} -c:v libx264 -preset veryfast -tune stillimage -c:a aac -b:a 128k -shortest -f flv rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}')
        time.sleep(2)
