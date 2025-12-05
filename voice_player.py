import pygame as wav
import random
import time
import os

wav_path = r"C:\Users\ethyn\OneDrive\Desktop\Trump\mp3_folders_trump"
all_things = os.listdir(wav_path)

random_wavs = [f for f in all_things if os.path.isfile(os.path.join(wav_path, f))]

wav.mixer.init()

current_wav = None

while True:
    try:
        current_wav = random.choice(random_wavs)
        full_random_path = os.path.join(wav_path, current_wav)
        wav.mixer.music.load(full_random_path)
        wav.mixer.music.play()
        while wav.mixer.music.get_busy():
            wav.time.wait(100)
        print(f'Played {current_wav}. ')
        timer = random.randint(4, 30)
        print(f'Waiting for {timer} seconds. ')
        time.sleep(timer)
    except Exception as e:
        print(f'The loader ran into error {e}. ')
    except KeyboardInterrupt:
        print('Program stopped by user. Exiting. ')


