import assemblyai as aai

aai.settings.api_key = "b1fa440650424dd494a560c99dfc8a21" 

transcript = aai.Transcriber().transcribe("./Test_videos/LAMP_Stack.mov")

subtitles = transcript.export_subtitles_srt(chars_per_caption=85)

f = open("subtitles.srt", "w")

f.write(subtitles)

f.close()

