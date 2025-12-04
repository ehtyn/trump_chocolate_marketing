import pygame as mp3
import random
import time


random_mp3s = [
    r'C:\Users\ethyn\OneDrive\Desktop\Email_Reader\mp3_folders_trump\believe_me.mp3',
    r'C:\Users\ethyn\OneDrive\Desktop\Email_Reader\mp3_folders_trump\complainer.mp3',
    r'C:\Users\ethyn\OneDrive\Desktop\Email_Reader\mp3_folders_trump\good_cocoa.mp3',
    r'C:\Users\ethyn\OneDrive\Desktop\Email_Reader\mp3_folders_trump\I_Know.mp3',
    r'C:\Users\ethyn\OneDrive\Desktop\Email_Reader\mp3_folders_trump\its_true.mp3',
    r'C:\Users\ethyn\OneDrive\Desktop\Email_Reader\mp3_folders_trump\marshmallows.mp3',
    r'C:\Users\ethyn\OneDrive\Desktop\Email_Reader\mp3_folders_trump\one_sip.mp3',
    r'C:\Users\ethyn\OneDrive\Desktop\Email_Reader\mp3_folders_trump\other_cocoa.mp3',
    r'C:\Users\ethyn\OneDrive\Desktop\Email_Reader\mp3_folders_trump\other_people.mp3',
    r'C:\Users\ethyn\OneDrive\Desktop\Email_Reader\mp3_folders_trump\People_always_say.mp3',
    r'C:\Users\ethyn\OneDrive\Desktop\Email_Reader\mp3_folders_trump\the_best.mp3',
    r'C:\Users\ethyn\OneDrive\Desktop\Email_Reader\mp3_folders_trump\we_do_right.mp3'
]

mp3.mixer.init()

current_mp3 = None

while True:
    try:
        current_mp3 = random.choice(random_mp3s)
        mp3.mixer.music.load(current_mp3)
        mp3.mixer.music.play()
        while mp3.mixer.music.get_busy():
            mp3.time.wait(100)
        print(f'Played {current_mp3}. ')
        timer = random.randint(4, 30)
        print(f'Waiting for {timer} seconds. ')
        time.sleep(timer)
    except Exception as e:
        print(f'The loader ran into error {e}. ')
    except KeyboardInterrupt:
        print('Program stopped by user. Exiting. ')


