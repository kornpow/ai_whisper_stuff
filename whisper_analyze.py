import sh
import os
import subprocess

# Define the directory to search
directory = "/home/skorn/podcasts"

for root, dirs, files in os.walk(directory):
    for file in files:
        print("Reading file: ", os.path.join(root, file))
        # Check if the file is an MP3
        if file.endswith(".wav"):
            # Do the whisper analysis
            print("Whisper Analyzing file: ", os.path.join(root, file))
            # Define the output file name
            output_file = os.path.splitext(os.path.join(root, file))[0]
            sh.main(
                os.path.join(root, file), 
                "-p", 2,
                "-t", 8,
                # "--output-txt",
                "--output-json",
                # "--output-json-full",
                "--output-file", output_file,
                # "-d", "20000", # test conversion
            )

