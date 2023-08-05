import tkinter as tk
from tkinter import messagebox, scrolledtext

def count_words():
    text = text_area.get("1.0", tk.END)
    words = text.split()
    word_count = len(words)
    messagebox.showinfo("Word count", f"Word count: {word_count}")

root = tk.Tk()
root.title("Word Counter")

exit_button = tk.Button(root, text='X', command=root.quit)
exit_button.pack(side=tk.RIGHT, anchor=tk.N)

text_area = scrolledtext.ScrolledText(root, width=30, height=10, font=("Times New Roman", 18))
text_area.pack()

count_button = tk.Button(root, text="Count Words", command=count_words)
count_button.pack()

root.mainloop()

