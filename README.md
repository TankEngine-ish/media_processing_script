# Media Processing Script


## Part 1 - Generating captions for your video


This simple Python script's main purpose is to generate captions for your video file
using Assembly AI's model to understand and transcribe speech. It's actually insanely impressive
how accurate it is in extracting the words from a voice with heavy accent like mine.

This is the first .srt file I generated for one of my portfolio videos.

![Alt text](<Images/Screenshot from 2024-01-29 17-05-18.png>)

## Part 2 - Extracting the audio from your video file

It's worth noting that the larger your video file the longer it would take for the 
caption generator to create them.

That's why I've added a video to audio extraction part of my script with the FFMPEG library to help you quicken the whole process. You can comment it out if not needed.
