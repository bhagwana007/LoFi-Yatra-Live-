import os

stream_key = "dtr3-w144-392p-8x4x-75cf"  # <- Apna YouTube stream key daalo

os.system(f"ffmpeg -re -stream_loop -1 -i song.mp3 -loop 1 -i thumbnail.jpg -c:v libx264 -preset veryfast -maxrate 3000k -bufsize 6000k -pix_fmt yuv420p -vf scale=1280:720 -c:a aac -b:a 160k -shortest -f flv rtmp://a.rtmp.youtube.com/live2/{stream_key}")
