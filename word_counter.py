import tkinter as tk
from tkinter import scrolledtext

def count_words():
    text = text_area.get("1.0", tk.END)
    words = text.split()
    word_count = len(words)
    count_label.config(text=f"Word count: {word_count}")

root = tk.Tk()
root.title("Word Counter")

#exit button and functionality
exit_button = tk.Button(root, text='X', command=root.quit)
exit_button.pack(side=tk.RIGHT, anchor=tk.N)

#creacion de un frame para poder tener todo al centro
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

#title label
title_label = tk.Label(frame, text="Word Counter", font=("Helvetica", 24))
title_label.pack()

text_area = scrolledtext.ScrolledText(frame, width=30, height=10, font=("Times New Roman", 18))
text_area.pack()

count_button = tk.Button(frame, text="Count Words", command=count_words)
count_button.pack()


#words counted text
count_label = tk.Label(frame,text="")
count_label.pack()

root.mainloop()

