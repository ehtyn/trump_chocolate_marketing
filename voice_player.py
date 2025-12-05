import pygame as wav
import random
import time
import os

wav_path = r"C:\Users\ethyn\OneDrive\Desktop\Trump\mp3_folders_trump"
all_things = os.listdir(wav_path)

random_wavs = [f for f in all_things if os.path.isfile(os.path.join(wav_path, f))]

wav.mixer.init()


prev_wav = None

first = True # Variable aids in duplicate .wav playing

while True:
    try:
        if first:
            print('This is the first time. ') # Debug
            # Selects random song
            current_wav = random.choice(random_wavs)
            full_random_path = os.path.join(wav_path, current_wav)

            # Fails if using just filename, since files exist in the folder, not general root

            wav.mixer.music.load(full_random_path)
            wav.mixer.music.play()

            # Keeps script active

            while wav.mixer.music.get_busy():
                wav.time.wait(100)
            
            # Debug, print can be removed
            print(f'Played {current_wav}. ')
            timer = random.randint(4, 30) # Time can be changed

            print(f'Waiting for {timer} seconds. ')
            time.sleep(timer)
            prev_wav = current_wav
            first = False
        if not first: # Checks if this is the first time running the script
            print('This is the > 1 time. ') # Debug
            current_wav = random.choice(random_wavs)

            while current_wav == prev_wav:
                print('Rolled the same wav. Rerolling. ') # Debug
                current_wav = random.choice(random_wavs)

            full_random_path = os.path.join(wav_path, current_wav)

            wav.mixer.music.load(full_random_path)
            wav.mixer.music.play()

            # Keeps script active

            while wav.mixer.music.get_busy():
                wav.time.wait(100)
            
            # Debug, print can be removed
            print(f'Played {current_wav}. ')
            timer = random.randint(4, 30) # Time can be changed

            print(f'Waiting for {timer} seconds. ')
            time.sleep(timer)
            prev_wav = current_wav




    except Exception as e:
        print(f'The loader ran into error {e}. ')
        
    except KeyboardInterrupt:
        print('Program stopped by user. Exiting. ')


