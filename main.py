import pygame
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[2H"

def get_seconds():
    while True:
        try:
            seconds = int(input("Enter the amount of seconds you want the alarm to be: "))
            if seconds <= 0:
                print("Alarm must be 1 second(s) or longer.\n")
                continue
            return seconds
        except ValueError:
            print("Please enter a valid number.\n")

def alarm(seconds):
    print(CLEAR)
    for time_elapsed in range(seconds, -1, -1):
        minutes_left = time_elapsed // 60
        seconds_left = time_elapsed % 60
        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}")
        time.sleep(1)

    # Initialize the mixer and play the alarm sound
    pygame.mixer.init()
    pygame.mixer.music.load("alarm.wav")  # Make sure the file exists
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)

def main():
    seconds = get_seconds()
    alarm(seconds)

if __name__ == "__main__":
    main()
