import pyautogui, time
words = set(open('message.txt').read().split())
print('within 5 seconds open Whatsapp web or any messaging ap and click the curser on the text field where messages were to be typed.')
print("The spamming will start in three seconds...")
time.sleep(5)
print("Spamming started.")
while True:
    for word in words:
        pyautogui.typewrite(word + " ")
        pyautogui.press('enter')
