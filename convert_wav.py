import os
from pydub import AudioSegment

# Define the directory to search
directory = "/media/podcasts/data/podcasts/"

# Define the sample rate
# WhisperCpp requires a sample rate of 16 kHz
sample_rate = 16_000

# Recursively search through the directory
for root, dirs, files in os.walk(directory):
    for file in files:
        print("Reading file: ", os.path.join(root, file))
        # Check if the file is an MP3
        if file.endswith(".mp3"):
            # Define the output file name
            output_file = os.path.splitext(os.path.join(root, file))[0] + ".wav"
            # Check if the WAV file already exists
            if not os.path.exists(output_file):
                # Load the MP3 file
                audio = AudioSegment.from_mp3(os.path.join(root, file))
                print("Writing file: ", output_file)
                # Export as WAV
                audio.export(output_file, format="wav", parameters=["-ar", str(sample_rate)])
            else:
                print("File already exists: ", output_file)
