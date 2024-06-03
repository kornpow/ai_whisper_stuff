import json
import glob
import sqlite3
from pathlib import Path
from pydub import AudioSegment

# Define the directory to search
wav_dir = "/media/podcasts/data/podcasts/"
clip_dir = "/media/podcasts/data/podcasts_cut"
db_file = f"{clip_dir}/metadata.db"



# def save_clip(audio_file, start_time, stop_time, output_directory, filename):
#     audio = AudioSegment.from_file(audio_file)
#     # Cut the audio
#     cut_audio = audio[start_time:stop_time]
#     # Save the cut audio to the output directory
#     clip_full_filepath = output_directory + "/" + filename
#     print("Saving clip to: ", clip_full_filepath)
#     cut_audio.export(clip_full_filepath, format="mp3")

def db_init():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create table for metadata if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clips (
        id INTEGER PRIMARY KEY,
        original_file TEXT,
        clip_file TEXT,
        clip_audio BLOB
        start_time INTEGER,
        stop_time INTEGER,
        text TEXT
    )
    ''')
    return cursor
# Connect to SQLite database (it will be created if it doesn't exist)


# Function to check if a clip has already been processed
def clip_exists(original_file, start_time, stop_time):
    cursor.execute('''
    SELECT 1 FROM clips WHERE original_file = ? AND start_time = ? AND stop_time = ?
    ''', (original_file, start_time, stop_time))
    return cursor.fetchone() is not None

def open_transcription_file(tf):
    with open(tf, "r") as f:
        data = json.load(f)
    try:
        return flatten_transcription(data["transcription"])
    except KeyError:
        raise ValueError("Transcription file is corrupted")
    

def flatten_transcription(transcription):
    return [(t["text"].lower().strip(),t["offsets"]["from"],t["offsets"]["to"]) for t in transcription]


def find_target_phrase(transcript, word1="the", word2="space"):
    found_space = []
    for i in range(0,len(transcript)):
        if transcript[i][0].find("space") != -1:
            found_space.append(i)


    target_clips = []
    # find instances of the word "the" before the word "space"
    for space_found in found_space:
        if transcript[space_found - 1][0].find("the") != -1:
            print(space_found)
            target_clips.append(space_found)

    return target_clips

# # Recursively search directory for .json files
# for file in glob.glob(wav_dir + "/**/*.json", recursive=True):
#     index = 0
#     print(file)
#     with open(file, "r") as f:
#         data = json.load(f)
#     for t in data["transcription"]:
#         speach_text = t["text"].lower()
#         if "space" in speach_text:
#             print("Found 'space' in transcription.")
#             offsets = t["offsets"]
#             print(file)
#             print(offsets)
#             audio_file = Path(file).with_suffix('.mp3')
#             save_clip(audio_file, offsets["from"], offsets["to"], clip_dir, f"{audio_file.name}-{index}.mp3")
#             index += 1



def example():
    b = open_transcription_file("/Users/samkorn/Documents/repos/ai_whisper_stuff/audio_data/SLP/2023/2023.12.31 Are Covenants Necessary for Bitcoin with Brandon Black (SLP537).json")
    b = open_transcription_file("/Users/samkorn/Documents/repos/ai_whisper_stuff/audio_data/SLP/2023/2023.12.15 The Great Drivechain Debate with Paul Sztorc and Peter Todd (SLP533).json")


    flat_transcript = flatten_transcription(transcript)

        # find instances of the word "space"
    found_space = []
    for i in range(0,len(flat_transcript)):
        if flat_transcript[i][0].lower().find("space") != -1:
            found_space.append(i)


    target_clips = []
    # find instances of the word "the" before the word "space"
    for space_found in found_space:
        if "the" in flat_transcript[space_found - 1][0]:
            print(space_found)
            target_clips.append(space_found)




if __name__ == "__main__":
    import code
    code.interact(local={**globals(), **locals()})
    cursor = db_init()
