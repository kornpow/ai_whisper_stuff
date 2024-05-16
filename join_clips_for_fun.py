from pydub import AudioSegment
import os

# Define the directory to search
directory = "/home/skorn/podcasts_cut"

# Create an empty list to store the audio segments
audio_segments = []

# Loop through each file in the directory
for filename in os.listdir(directory):
    # Check if the file is an mp3
    if filename.endswith(".mp3"):
        # Load the mp3 file
        audio = AudioSegment.from_file(os.path.join(directory, filename))
        # Append the audio segment to the list
        audio_segments.append(audio)

# Combine all audio segments into a single audio segment
combined_audio = sum(audio_segments, AudioSegment.empty())

# Define the output file path
output_file_path = "/home/skorn/output.mp3"

# Export the combined audio to the output file
combined_audio.export(output_file_path, format="mp3")
