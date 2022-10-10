import tkinter
import time
import random

listy = [
    "Such a race would not be fair",
    "I'll race you to the bottom and we can talk about it.",
    "His heart continued to race as he glanced over at Edith.",
    "Dad said we were going to watch some horses race tomorrow.",
    "It, too, was done up in a race car theme with toys lining the side of the tub."
]


window = tkinter.Tk()
window.geometry('500x500')
window.title("Welcome to the TypeRacer app")
phrase = ''
lbl = tkinter.Label(window, text = "TypeRacer!", font = ("Arial Bold",20))
window.columnconfigure(0, weight=1)
window.columnconfigure(2, weight=1)
lbl.grid(column = 1, row = 0)

def begin():
    tic = time.perf_counter()
    start_button.grid_forget()
    start_button.update_idletasks()
    typing = listy[random.randint(0,len(listy) -1)]
    phrase = typing
    text_to_type = tkinter.Label(window, text=f"{typing}", font=("Arial", 10))
    text_to_type.grid(column=1, row=1)
    start_button.grid_forget()
    start_button.update_idletasks()
    input_window = tkinter.Entry(width=50)
    input_window.grid(column=1, row=2)

    def done():
        toc = time.perf_counter()
        input_from_user = input_window.get()
        if input_from_user == phrase:
            fin_lbl = tkinter.Label(window, text = f'Race was completed in {toc - tic:0.4f} seconds', font = ("Arial",10))
            fin_lbl.grid(column=1, row=3, padx=20, pady=60)
            end_button.grid_forget()
        else:
            print('You did not input the phrase correctly. Try Again!')
        return

    end_button = tkinter.Button(window, text="Finish!", font=("Arial Bold", 20), command=done)
    end_button.grid(column=1, row=5, padx=20, pady=60)
    return


start_button = tkinter.Button(window, text = "Press me to begin the race!", font = ("Arial Bold",20), command = begin)
window.rowconfigure(0, weight=1)
window.rowconfigure(2, weight=1)
start_button.grid(column = 1, row = 1)



window.mainloop()
