import os
import random
from PIL import Image
import pyautogui #pip install pyautogui
import time
from bing_image_downloader import downloader #pip install bing_image_downloader

def puppyScraper(): #Downloads the images of puppies
    done = False
    while not done: 
        amount = input("How many images?:  ")
        try:
            downloader.download("puppies", limit=int(amount), adult_filter_off=True, force_replace=True)
            done = True
        except:
            print("That isn't a number! Try again...")
            done = False

def show_puppies(): #Shows the images at random
    folder=r"dataset\bing\puppies"
    try:
        a=random.choice(os.listdir(folder))
    except:
        print("No puppies found! Downloading puppies...")
        puppyScraper()
    finally:
        print(a)
        file = folder+'\\'+a
        Image.open(file).show()

def close_win():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('f4')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('f4') 

if __name__ == "__main__":
    while True:
        choice = input("Want to download more puppies? (Y/N)  ")
        if choice.lower() == "y":
            puppyScraper()
        elif choice.lower() == "n":
            print("Showing random puppies...")
            while True:
                show_puppies()
                time.sleep(3)
                close_win()
        else:
            print("That isn't an option... Try again!")
