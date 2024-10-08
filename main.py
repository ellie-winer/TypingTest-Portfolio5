import tkinter as tk
from tkinter import messagebox
from sentences import sentences_dict

time_left = 60
typed_words = []
current_sentence = []
sentence_index = 0



def start_test():
    global time_left, typed_words, sentence_index

    if time_left == 60:
        typed_words = []
        sentence_index = 0
        entry.delete(0, tk.END)
        entry.focus_set()
        label.config(text="")
        display_sentence()
        countdown()
        add_more_words()



def display_sentence():
    global sentence_index, current_sentence

    sentence_keys = list(sentences_dict.keys())

    if sentence_index < len(sentence_keys):
        current_sentence = sentences_dict[sentence_keys[sentence_index]]
        sentence_index += 1
    else:
        current_sentence = []



def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_label.config(text=f"Time left: {time_left}s")
        window.after(1000, countdown)
    else:
        finish_test()



def add_more_words():
    global current_sentence

    if time_left > 0:
        if len(current_sentence) == 0:
            display_sentence()

        if current_sentence:
            word = current_sentence.pop(0)
            label.config(text=label.cget("text").strip() + " " + word)
        window.after(500, add_more_words)



def check_input():
    global typed_words
    typed_input = entry.get().strip().split()
    displayed_words = label.cget("text").strip().split()  # Get the words displayed in the label

    correct_word_count = 0


    for i in range(min(len(typed_input), len(displayed_words))):
        if typed_input[i] == displayed_words[i]:
            correct_word_count += 1


    messagebox.showinfo("Results", f"You typed {correct_word_count} words correctly.")
    entry.delete(0, tk.END)


def finish_test():
    entry.config(state='disabled')

    final_input = entry.get().strip().split()
    final_displayed = label.cget("text").strip().split()

    correct_word_count = sum(
        1 for i in range(min(len(final_input), len(final_displayed))) if final_input[i] == final_displayed[i])
    messagebox.showinfo("Test Finished", f"Time's up! You typed {correct_word_count} words correctly.")



window = tk.Tk()
window.title("Typing Test")
window.config(padx=30, pady=30, bg='lightblue')
window.minsize(width=800, height=600)

label = tk.Label(window, text="", font=("Helvetica", 24), wraplength=600, highlightbackground='lightblue')
label.pack(pady=20)

entry = tk.Entry(window, font=("Helvetica", 20), highlightcolor='lightblue', highlightbackground='lightblue')
entry.pack(pady=10)

start_button = tk.Button(window, text="Start Test", command=start_test, highlightcolor='lightblue',
                         highlightbackground='lightblue')
start_button.pack(pady=20)

check_button = tk.Button(window, text="Check Input", command=check_input, highlightcolor='lightblue',
                         highlightbackground='lightblue')
check_button.pack(pady=10)

timer_label = tk.Label(window, text="Time left: 60s", font=("Helvetica", 16), highlightcolor='lightblue',
                       highlightbackground='lightblue')
timer_label.pack(pady=10)

window.mainloop()
