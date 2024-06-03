import pygame
from pydub import AudioSegment
from io import BytesIO
from copy import deepcopy


# def play_audio_from_bytesio(audio_bytes):
#     pygame.mixer.init()
#     audio_bytes_playable = deepcopy(audio_bytes)
#     sound = pygame.mixer.Sound(audio_bytes_playable)
#     sound.play()


class AudioFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.audio_segment = AudioSegment.from_mp3(file_path)
    def get_file_path(self):
        return self.file_path
    def get_audio_segment(self):
        return self.audio_segment
    def slice_audio(self, start_time_ms, end_time_ms):
        sliced_audio = self.audio_segment[start_time_ms:end_time_ms]
        output_bytes_io = BytesIO()
        sliced_audio.export(output_bytes_io, format="mp3")
        # sliced_audio.export("test.mp3", format="mp3")
        return output_bytes_io
    @classmethod
    def play_audio_from_bytesio(cls, audio_bytes):
        pygame.mixer.init()
        print("playing a sound!")
        audio_bytes_playable = deepcopy(audio_bytes)
        sound = pygame.mixer.Sound(audio_bytes_playable)
        sound.play()
        pygame.time.wait(int(sound.get_length() * 1000))



    
class AudioFileClip:
    def __init__(self, audio_file: AudioFile, start_time_ms: int, end_time_ms: int):
        if end_time_ms < start_time_ms:
            raise ValueError("end_time_ms cannot be less than start_time_ms")
        self.audio_file = audio_file
        self.start_time_ms = start_time_ms
        self.end_time_ms = end_time_ms
    def get_audio_segment(self):
        return self.audio_file.audio_segment
    def get_original_file(self):
        return self.audio_file.file_path
    def get_start_time_ms(self):
        return self.start_time_ms
    def get_end_time_ms(self):
        return self.end_time_ms
    def play(self):
        self.audio_file.play_audio_from_bytesio(self.audio_file.slice_audio(self.start_time_ms, self.end_time_ms))



# Example usage
# audio_file = AudioFile("/Users/samkorn/Documents/repos/ai_whisper_stuff/audio_data/SLP/2023/2023.12.31 Are Covenants Necessary for Bitcoin with Brandon Black (SLP537).mp3")
# audio_file = AudioFile("/Users/samkorn/Documents/repos/ai_whisper_stuff/audio_data/SLP/2023/2023.12.15 The Great Drivechain Debate with Paul Sztorc and Peter Todd (SLP533).mp3")
# sliced_audio_segment = SlicedAudioSegment(audio_file, 55240, 56010)

import pickle

# Save the sliced_audio_segment as a pickle
# with open("sliced_audio_segment.pkl", "wb") as f:
#     pickle.dump(sliced_audio_segment, f)


# # Load the sliced_audio_segment from the pickle
# with open("sliced_audio_segment.pkl", "rb") as f:
#     loaded_sliced_audio_segment = pickle.load(f)

# # Example usage of the loaded object
# print(f"Loaded SlicedAudioSegment from {loaded_sliced_audio_segment.get_original_file()}")
# print(f"Start time: {loaded_sliced_audio_segment.get_start_time_ms()} ms")
# print(f"End time: {loaded_sliced_audio_segment.get_end_time_ms()} ms")


if __name__ == "__main__":
    import code
    code.interact(local={**globals(), **locals()})