import assemblyai as aai
import subprocess

aai.settings.api_key = "b1fa440650424dd494a560c99dfc8a21" 

## Extract audio from video file


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

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Video converted to audio successfully")
    except subprocess.CalledProcessError as e:
        print("Converting video to audio failed")



convert_video_to_audio("./Test_videos/LAMP_Stack.mov", "./Test_videos/LAMP_Stack.mp3")




## Transcribe the audio file
 
transcript = aai.Transcriber().transcribe("./Test_videos/LAMP_Stack.mp3")

subtitles = transcript.export_subtitles_srt(chars_per_caption=85)

f = open("subtitles.srt", "w")

f.write(subtitles)

f.close()

print("Your Captions are ready!")

