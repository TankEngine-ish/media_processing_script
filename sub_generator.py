import assemblyai as aai
import subprocess

aai.settings.api_key = "<your API key from Assembly AI>" 

## Extract audio from video file section

def convert_video_to_audio(input_video, output_audio):
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_video,
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", "192k",
        "-ar", "44100",
        "-y",
        output_audio
    ]
    
    # the above options are for the output audio's quality such as bitrate,
    # sample rate, codec, etc. You can change them as needed.
    
    
    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Video converted to audio successfully")
    except subprocess.CalledProcessError as e:
        print("Converting video to audio failed")


convert_video_to_audio("<path to your video>", "<path to your audio file>")



## Transcribe the audio file section
 
transcript = aai.Transcriber().transcribe("<path to your audio file>")

subtitles = transcript.export_subtitles_srt(chars_per_caption=85)

# between 80 and 100 characters per caption is recommended

f = open("subtitles.srt", "w")

f.write(subtitles)

f.close()

print("Your Captions are ready!")

