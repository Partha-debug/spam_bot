import pyautogui, time

def show_instructions():
    print('within 5 seconds open Whatsapp web or any other messaging app and click the curser on the text field where messages were to be typed.')
    print("The spamming will start in three seconds...")
    time.sleep(5)
    print("Spamming started.")

def start_spamming():
    words = set(open('message.txt').read().split())
    while True:
        for word in words:
            pyautogui.typewrite(word + " ")
            pyautogui.press('enter')


if __name__ == "__main__":
   
    show_instructions()
    start_spamming() 

