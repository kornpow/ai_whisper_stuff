# AI Whisper Stuff

This repository contains several scripts that perform various operations on podcast files. Here's a brief overview of each script:

- **download.py**: This script is responsible for downloading podcasts from various RSS feeds. It leverages the `getpodcast` library to fetch and download the podcasts. The script is configured to only download new podcasts from a specified date.

- **convert_wav.py**: Once the podcasts are downloaded, this script converts the mp3 podcast files into wav format. It recursively searches through a specified directory for mp3 files and, if found, converts them to wav format with a sample rate of 16 kHz.

- **whisper_analyze.py**: This script processes the audio files to find what is being said and when it is said. It uses the `WhisperCpp` library for this purpose. The script recursively searches through a specified directory for wav files and, if found, analyzes them. The results are saved in a json file.

- **search_for_space.py**: This script searches through downloaded podcast transcriptions for the word "space". If found, it extracts the corresponding audio clip from the podcast and saves it as a separate mp3 file.

- **join_clips_for_fun.py**: This script combines all the extracted audio clips into a single mp3 file. It reads all the mp3 files in a specified directory, combines them, and exports the combined audio to a new mp3 file.
