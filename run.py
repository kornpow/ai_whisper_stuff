
from play_audio import AudioFile, AudioFileClip
from search_for_space import open_transcription_file, find_target_phrase

def example_process(file_root="audio_data/SLP/2023", file_name="2023.11.19 Don’t Lose Your Coins with NVK (SLP526)"):
    target_file = f"{file_root}/{file_name}"
    print(f"Processing {target_file}...")
    audio_file = AudioFile(f"{target_file}.mp3")
    transcript = open_transcription_file(f"{target_file}.json")
    targets = find_target_phrase(transcript)
    # good_clips = []
    count = 1
    for clip in targets:
        import csv
        import os

        clip_start_ms = transcript[clip][2]- 1000
        clip_end_ms = transcript[clip][2]
        space_clip = AudioFileClip(audio_file, clip_start_ms, clip_end_ms)

        # Ensure the clips subdirectory exists
        clips_dir = os.path.join(file_root, "clips")
        os.makedirs(clips_dir, exist_ok=True)

        # Save the space_clip to a file in the clips subdirectory
        clip_filename = f"{file_name.replace(' ', '_')}_clip_{count}.mp3"

        clip_filepath = os.path.join(clips_dir, clip_filename)
        with open(clip_filepath, 'wb') as f:
            f.write(space_clip.audio_file.slice_audio(clip_start_ms, clip_end_ms).getvalue())

        # Create or append to the CSV file in the clips directory
        csv_filename = os.path.join(clips_dir, "clips_metadata.csv")
        file_exists = os.path.isfile(csv_filename)
        with open(csv_filename, mode='a', newline='') as csv_file:
            fieldnames = ['id', 'filename', 'start_time_ms', 'end_time_ms']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow({'id': count, 'filename': clip_filename, 'start_time_ms': clip_start_ms, 'end_time_ms': clip_end_ms})

        print(f"Saved clip to {clip_filepath}")
        count += 1
        # good_clips.append(space_clip)

    # return good_clips
    # code.interact(local={**globals(), **locals()})


from pathlib import Path
import psutil
process = psutil.Process()

# files = [
#     "2023.08.15 SLP501 RGB Walkthrough with Maxim Orlovsky",
#     "2023.07.10 SLP490 Dusty - What is Splicing and why will it improve LN",
#     "2023.05.29 SLP482 Burak - Ark A new L2 protocol for Bitcoin"
# ]

base_path = Path("/Users/samkorn/Documents/repos/ai_whisper_stuff/audio_data/SLP/2023")
files = [file.stem for file in base_path.rglob("*.mp3")]



clips = []
for f in files:
    try:
        try:
            new_clips = example_process("audio_data/SLP/2023/", f)
        except FileNotFoundError:
            pass 
        # clips.extend(new_clips)
        # if process.memory_info().rss / 1024 / 1024 > 2000:
        #     print("Memory limit reached.")
        #     break
    except KeyboardInterrupt:
        break

if __name__ == "__main__":
    import code
    # example_process()
    code.interact(local={**globals(), **locals()})