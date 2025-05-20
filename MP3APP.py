import pygame
import time
import random
import os
pygame.mixer.init()
print("Hello!! Welcome to this MP3 Player App or whatever you may call")
time.sleep(0.2)
print("This App works by command, and not by GUI... as i am new and dont know anything about tkinter")
time.sleep(0.2)
print("Lets get Started...")
print('COMMANDS')
print('1. "play" for playing audio' )
print('2. "pause" for Pausing audio')
print('3. "shuffle" for shuffling audio and playing random audio')
print('4. "resume" for playing audio' )
print('5. "exit" for exiting audio' )
# command=input("Enter your command: ")
musics= "C:\\Users\Saurabh\OneDrive\Desktop\PythonTests\MP3Player\musics"
songs=[]
for i in os.listdir(musics):
    if i.endswith(".mp3"):
        songs.append(i)
# used chatGPT here
def play_audio(file_name):
    full_path = os.path.join(musics, file_name)
    pygame.mixer.music.load(full_path)
    pygame.mixer.music.play()
    print(f"Now playing: {file_name}")
# till here
while True:
    command=input("Enter your command: ").lower()
    if command== "play":
        if songs:
            play_audio(songs[0])  
        else:
            print("no medias found")

    elif command=="pause":
        pygame.mixer.music.pause()
        print("Audio paused")
    elif command=="shuffle":
        if songs:
            random_song=random.choice(songs)
            play_audio(random_song)
        else:
            print("no MP3 found")

    elif command=="resume":
        pygame.mixer.music.unpause()
        print("COntinued")

    elif command=="exit":
        print("I quit!!! ")
        break
    else:
        print("Enter Valid COmmand")