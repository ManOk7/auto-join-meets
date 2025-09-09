# Google Meet Auto Join Bot 

 This Python script joins Google Meet meetings automatically.  
 It eliminates the need for you to manually click on the camera, microphone, and "Join" button by using **PyAutoGUI**.


 ---

 ## ⚡ Features:
 Schedule several meetings with various times and links.
 
 At the specified time, Google Chrome opens automatically.
 
 Before joining, turn off the **microphone** and **camera**.
 
 The **"Join now"** button is automatically clicked.

 Ends the meeting after the desired duration.
 
 Runs continuously in the background.

 ---

 ## 🛠️  Conditions
 - Python 3.10+ 
 - Chrome needs to be already logged in with your account - Google Chrome (installed in the default path)
 - Python libraries:
   - `pyautogui`
   - `schedule`
   - `time`
   - `os`

 ---

 ## Installation and working
 1. Download or clone this repository.
 ```git clone https://github.com/ManOk7/auto-join-meets```
 2. Set up dependencies:
    ```pip install -r requirements.txt```
3. Start the script
   ```python auto-join-meets.py``` 
