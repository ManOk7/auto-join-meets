import pyautogui
import time
import os
import schedule

def join(link, duration):
    print(f"Joining meeting: {link} for {duration} minutes")

    os.system(f'"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" {link}')
    time.sleep(5)  # wait for Chrome to open

    # Turn off cam & mic
    pyautogui.click(x=671, y=887)  # camera
    pyautogui.click(x=558, y=872)  # mic
    time.sleep(1)

    # Join now button
    pyautogui.click(x=1498, y=660)
    print("Joined successfully!")
    
    # meeting duration
    time.sleep(duration * 60)

    # Leave meeting 
    pyautogui.click(x=1140, y=1010) 


# input from user
n = int(input("How many meetings do you want to schedule: "))

meetings = {}

for i in range(n):
    t = input("Enter time for meeting (HH:MM, 24hr format): ")
    link = input("Enter Google Meet link for meeting: ")
    d = int(input("Enter duration (in minutes) for meeting: "))
    meetings[t] = {"link": link, "duration": d}


# Scheduling meetings
for t, info in meetings.items():
    schedule.every().day.at(t).do(join, info["link"], info["duration"])
    print(f"Meeting scheduled at {t} : {info['link']} : ({info['duration']} min)")

print("Program started")

while True:
    schedule.run_pending()
    time.sleep(60)
