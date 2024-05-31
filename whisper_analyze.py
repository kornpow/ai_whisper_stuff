import sh
import os

# Define the directory to search
wav_dir = "/media/podcasts/data/podcasts/"


def whisper_analyze(wav_file, output_file):
    # Do the whisper analysis
    print("Whisper Analyzing file: ", wav_file)
    print("Will generate output file: ", output_file)
    sh.main(
        "-m", "/home/skorn/Documents/repos/whisper.cpp/models/ggml-medium.en.bin",
        "-p", 2,
        "-t", 8,
        "-ml", 1,
        "--output-json",
        "--output-file", output_file,
        # "-d", "20000", # test conversion
        wav_file
    )
    print("done")

for root, dirs, files in os.walk(wav_dir):
    for file in files:
        print("Reading file: ", os.path.join(root, file))
        # Check if the file is an MP3
        if file.endswith(".wav"):
            # Do the whisper analysis
            wav_file = os.path.join(root, file)
            output_file = os.path.splitext(wav_file)[0]
            if not os.path.exists(f"{output_file}.json"):
                whisper_analyze(wav_file, output_file)
            else:
                print("Transcription already exists: ", output_file)
            




# a = sh.main(
#     "-m", "/home/skorn/Documents/repos/whisper.cpp/models/ggml-medium.en.bin",
#     "-p", 2,
#     "-t", 8,
#     "-ml", 1,
#     # "--output-txt",
#     "--output-json",
#     # "--output-json-full",
#     "--output-file", "/media/podcasts/data/podcasts/TFTC/2024/2024.05.04 #503 The Bitcoin Stack with Dhruv Bansal,Ryan Gentry & Allen Farrington",
#     # "-d", "20000", # test conversion
#     "/media/podcasts/data/podcasts/TFTC/2024/2024.05.04 #503 The Bitcoin Stack with Dhruv Bansal,Ryan Gentry & Allen Farrington.wav"
# )