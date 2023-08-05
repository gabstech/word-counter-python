import tkinter as tk
from tkinter import scrolledtext

def count_words():
    text = text_area.get("1.0", 'end-1c')
    words = text.split()
    word_count = len(words)
    count_label.config(text=f"Word count: {word_count}")

root = tk.Tk()
root.title("Word Counter")

# Get screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate width and height for root window
root_width = int(screen_width * 0.7)
root_height = int(screen_height * 0.7)

# Set root window size and position it at center
x_position = int((screen_width / 2) - (root_width / 2))
y_position = int((screen_height / 2) - (root_height / 2))

root.geometry(f'{root_width}x{root_height}+{x_position}+{y_position}')

# Create a frame
frame = tk.Frame(root)
frame.pack(expand=True, fill=tk.BOTH)

# Title and exit frame
title_exit_frame = tk.Frame(frame)
title_exit_frame.grid(row=0, column=0, sticky='ew')

# Title label
title_label = tk.Label(title_exit_frame, text="Word Counter", font=("Helvetica", 24))
title_label.pack(side=tk.LEFT, expand=True)

# Exit button and functionality
exit_button = tk.Button(title_exit_frame, text='X', command=root.quit)
exit_button.pack(side=tk.RIGHT)

# Text area
text_area = scrolledtext.ScrolledText(frame, font=("Times New Roman", 18))
text_area.grid(row=1, column=0, sticky='nsew')

# Button frame
button_frame = tk.Frame(frame)
button_frame.grid(row=2, column=0, sticky='ew')

# Count words button
count_button = tk.Button(button_frame, text="Count Words", command=count_words)
count_button.pack(side=tk.LEFT)

# Save Log
save_log_button = tk.Button(button_frame, text="Save Log")
save_log_button.pack(side=tk.RIGHT)

# Words counted label
count_label = tk.Label(frame, text="", font=("Helvetica", 14), padx=10, pady=10)
count_label.grid(row=3, column=0, sticky='ew')

# Configure the rows and columns of the grid to expand.
frame.grid_rowconfigure(1, weight=1)  # Make the text_area row expandable.
frame.grid_columnconfigure(0, weight=1)  # Make the column expandable.

root.mainloop()

