import tkinter as tk
from tkinter import messagebox, scrolledtext

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

#title label
title_label = tk.Label(root, text="Word Counter", font=("Helvetica", 24))
title_label.pack()

text_area = scrolledtext.ScrolledText(root, width=30, height=10, font=("Times New Roman", 18))
text_area.pack()

count_button = tk.Button(root, text="Count Words", command=count_words)
count_button.pack()


#words counted text
count_label = tk.Label(root,text="")
count_label.pack()

root.mainloop()

