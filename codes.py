# At first, install these modules [pytube, pyttsx3]

from pytube import *# for dowloading
from pyttsx3 import *# for the voice

# Make a func to download the video
def Download(link: str):
    # formality
    speak("Thanks for using me! Your video is being downloaded.")
    
    # get the object of the video
    youtubeVideo=YouTube(link)
    # make sure to get the highest resolution
    youtubeVideo=youtubeVideo.streams.get_highest_resolution()
    # download the video
    youtubeVideo.download()

    # finish
    print("Download completed successfully !")
    speak("Download completed successfully !")
    print("PLease check the folder where this Python file is located to get the downloaded file.")
    speak("PLease check the folder where this Python file is located to get the downloaded file.")

# Take the link of the video from the user.
link=input("Enter your YouTube video link : ")

# Trigger the func we made earlier to download it...
Download(link)
