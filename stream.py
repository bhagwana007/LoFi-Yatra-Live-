import os
import time
import subprocess

# --- CONFIGURATION ---
STREAM_KEY = "dtr3-w144-392p-8x4x-75cf"  # 🔁 यहां अपनी YouTube Stream Key डालें
VIDEO_FILE = "song.mp3"  # 🔁 यहां आपका गाना mp3 फाइल का नाम
THUMBNAIL = "thumbnail.jpg"  # 🔁 यहां आपकी image thumbnail का नाम
RTMP_URL = f"rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"
# ----------------------

def start_stream():
    command = [
        'ffmpeg',
        '-re',
        '-loop', '1',
        '-i', THUMBNAIL,
        '-i', VIDEO_FILE,
        '-c:v', 'libx264',
        '-tune', 'stillimage',
        '-c:a', 'aac',
        '-b:a', '192k',
        '-pix_fmt', 'yuv420p',
        '-shortest',
        '-f', 'flv',
        RTMP_URL
    ]
    
    print("📡 Starting stream...")
    process = subprocess.Popen(command)
    process.wait()
    print("⚠️ Stream ended. Restarting in 5 seconds...")
    time.sleep(5)

if __name__ == "__main__":
    while True:
        start_stream()
