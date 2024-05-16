import json
import glob
from pathlib import Path
from pydub import AudioSegment

# Define the directory to search
directory = "/home/skorn/podcasts"
clip_dir = "/home/skorn/podcasts_cut"


def save_clip(audio_file, start_time, stop_time, output_directory, filename):
    audio = AudioSegment.from_file(audio_file)
    # Cut the audio
    cut_audio = audio[start_time:stop_time]
    # Save the cut audio to the output directory
    clip_full_filepath = output_directory + "/" + filename
    print("Saving clip to: ", clip_full_filepath)
    cut_audio.export(clip_full_filepath, format="mp3")

# Recursively search directory for .json files
for file in glob.glob(directory + "/**/*.json", recursive=True):
    index = 0
    print(file)
    with open(file, "r") as f:
        data = json.load(f)
    for t in data["transcription"]:
        speach_text = t["text"].lower()
        if "space" in speach_text:
            print("Found 'space' in transcription.")
            offsets = t["offsets"]
            print(file)
            print(offsets)
            audio_file = Path(file).with_suffix('.mp3')
            save_clip(audio_file, offsets["from"], offsets["to"], clip_dir, f"{audio_file.name}-{index}.mp3")
            index += 1


    # Load audio file
    audio = AudioSegment.from_file(file)

    # Define start and stop time in milliseconds
    start_time = 10000
    stop_time = 20000

    # Cut the audio
    cut_audio = audio[start_time:stop_time]

    # Define the output directory
    output_directory = "/home/skorn/podcasts_cut"

    # Save the cut audio to the output directory
    cut_audio.export(output_directory + "/" + file.split('/')[-1], format="mp3")
