import pyautogui
import time
import os
import schedule

def join(link):
    os.system(f'"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" {link}')
    time.sleep(5)  

    pyautogui.click(x=671, y=887) #camera
    pyautogui.click(x=558, y=872) #mic

    time.sleep(1)
    pyautogui.click(x=1498, y=660) #join button


#input from user
n = int(input("How many meeting do you want to schedule:"))

meetings = {}

for i in range(n):
    t = input("Enter time for meeting (HH:MM, 24hr format): ")
    link = input("Enter Google Meet link for meeting:")
    meetings[t] = link
    

for t, link in meetings.items():
    schedule.every().day.at(t).do(join, link)
    print(f"Meeting scheduled at {t} : {link}")

print("Program started")

while True:
    schedule.run_pending()
    time.sleep(60)




