import time
import pyautogui
import threading
import tkinter as tk
from tkinter import messagebox

def start_spam():
    global spamming, spam_text
    spamming = True
    spam_text = entry_text.get()
    count = int(entry_count.get())
    delay = float(entry_delay.get())
    
    def spam():
        for _ in range(count):
            if not spamming:
                break
            pyautogui.typewrite(spam_text)
            pyautogui.press("enter")
            time.sleep(delay)
        messagebox.showinfo("Spam Complete", "Spamming finished!")
    
    threading.Thread(target=spam, daemon=True).start()

def stop_spam():
    global spamming
    spamming = False

def update_text():
    global spam_text
    spam_text = entry_text.get()

# Create GUI
root = tk.Tk()
root.title("Text Spammer")

spamming = False
spam_text = ""

tk.Label(root, text="Text to Spam:").pack()
entry_text = tk.Entry(root)
entry_text.pack()

update_text_button = tk.Button(root, text="Update Text", command=update_text)
update_text_button.pack()

tk.Label(root, text="Number of Times:").pack()
entry_count = tk.Entry(root)
entry_count.pack()

tk.Label(root, text="Delay Between Messages (seconds):").pack()
entry_delay = tk.Entry(root)
entry_delay.insert(0, "0.5")  # Default delay
entry_delay.pack()

start_button = tk.Button(root, text="Start Spamming", command=start_spam)
start_button.pack()

stop_button = tk.Button(root, text="Stop Spamming", command=stop_spam)
stop_button.pack()

root.mainloop()
