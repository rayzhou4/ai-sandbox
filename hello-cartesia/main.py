import requests
import subprocess
from dotenv import load_dotenv
import os

load_dotenv()

# headers + data
headers = {
  "Cartesia-Version": "2024-06-10",
  "X-API-Key": os.getenv("API_KEY"),
  "Content-Type": "application/json"
}
data = {
    "transcript": "Hello Cartesia, this is Ray's Project!",
    "model_id": "sonic-english", 
    "voice": {
      "mode": "id",
      "id": "a0e99841-438c-4a64-b679-ae501e7d6091",
      "__experimental_controls": {
        "speed": "normal", # control voice speed
        "emotion": [ # control emotions
          "positivity:high",
          "curiosity"
        ]
      }
    },
    "output_format": {
        "container": "raw",
        "encoding": "pcm_f32le",
        "sample_rate": 44100
    }
}

url = "https://api.cartesia.ai/tts/bytes"
response = requests.post(url, headers=headers, json=data, stream=True)

# Check if the request was successful
if response.status_code == 200:
    # Use ffmpeg to convert the streamed audio to a .wav file
    ffmpeg_process = subprocess.Popen(
        ['ffmpeg', '-f', 'f32le', '-i', 'pipe:', 'sonic.wav'],
        stdin=subprocess.PIPE
    )
    
    # Write the streamed response content to ffmpeg
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            ffmpeg_process.stdin.write(chunk)
    
    # Close the ffmpeg stdin to finish the process
    ffmpeg_process.stdin.close()
    ffmpeg_process.wait()

    print("Audio saved as sonic.wav")
else:
    print(f"Request failed with status code {response.status_code}")