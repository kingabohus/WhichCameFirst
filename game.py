import tkinter as tk
# from tkinter.ttk import *
from tkinter.font import Font
from PIL import Image, ImageTk
from Invention import *


inventions = set()
with open("dataset.txt", 'r') as file:
    for line in file:
        data = line.split('\t')
        inventions.add(Invention(id = data[0], name = data[1], link = data[2], date_text = data[3], value_min = data[4], value_max = data[5], flavor_text = data[6]))

x = 0
exit = False
def on_click(side):
    global x
    x = side
def on_exit():
    global exit
    exit = True
    
def game_round():
    invention1 = inventions.pop()
    invention2 = inventions.pop()

    correct = compare(invention1, invention2)
    # code for choice click

    window = tk.Tk()

    window.title("Inventions Game")
    window.geometry('700x350+100+100')



    title_font = Font(family="Garamond", size=15)
    text_font = Font(family="Helvetica", size=10)

    try:
        image1 = Image.open("images/image_{}.jpg".format(invention1.id))
    except:
        image1 = Image.open("images/grey.jpg")
    photo1 = ImageTk.PhotoImage(image1)

    try:
        image2 = Image.open("images/image_{}.jpg".format(invention2.id))
    except:
        image2 = Image.open("images/grey.jpg")
    photo2 = ImageTk.PhotoImage(image2)
    # left side
    button1 = tk.Button(window, image=photo1, command=lambda: [window.destroy(), on_click(1)])
    button1.place(relx=0.25, rely=0.5, anchor=tk.CENTER)
    button1.config(height=350, width=350)
    inv1_label = tk.Button(window, text = invention1.name, font = title_font, command=lambda: [window.destroy(), on_click(1)])
    inv1_label.place(relx = 0.25, rely = 0.5, anchor=tk.CENTER)


    # right side
    button2 = tk.Button(window, image=photo2, command=lambda: [window.destroy(), on_click(2)])
    button2.place(relx=0.75, rely=0.5, anchor=tk.CENTER)
    button2.config(height=350, width=350)
    inv2_label = tk.Button(window, text = invention2.name, font = title_font, command=lambda: [window.destroy(), on_click(2)])
    inv2_label.place(relx = 0.75, rely = 0.5, anchor=tk.CENTER)

    # top text
    q_label = tk.Label(window, text = "Which came first?", font = text_font)
    q_label.place(relx = 0.5, rely = 0.05, anchor=tk.CENTER)
    score_label = tk.Label(window, text="score = {}".format(score), font = text_font)
    score_label.place(relx=0.9, rely=0.05, anchor=tk.CENTER)

    window.mainloop()


    # After choice
    window = tk.Tk()
    # window.config(bg='black')
    window.title("Inventions Game")
    window.geometry('700x350+100+100')

    title_font = Font(family="Garamond", size=15)
    text_font = Font(family="Helvetica", size=10)

    inv1_label = tk.Label(window, text=invention1.name, font=title_font)
    inv1_label.place(relx=0.25, rely=0.2, anchor=tk.CENTER)
    inv1_date = tk.Label(window, text=invention1.date_text, font=title_font)
    inv1_date.place(relx=0.25, rely=0.3, anchor=tk.CENTER)
    inv1_flavor = tk.Label(window, text=invention1.flavor_text, font=text_font, wraplength=300)
    inv1_flavor.place(relx=0.25, rely=0.6, anchor=tk.CENTER)

    inv2_label = tk.Label(window, text=invention2.name, font=title_font)
    inv2_label.place(relx=0.75, rely=0.2, anchor=tk.CENTER)
    inv2_date = tk.Label(window, text=invention2.date_text, font=title_font)
    inv2_date.place(relx=0.75, rely=0.3, anchor=tk.CENTER)
    inv2_flavor = tk.Label(window, text=invention2.flavor_text, font=text_font, wraplength=300)
    inv2_flavor.place(relx=0.75, rely=0.6, anchor=tk.CENTER)

    print(x)
    if correct == 0:
        result_text = "Around the same time"
        result_color = 'black'
        round_score = 0
    elif x == correct:
        result_text = "Correct!"
        result_color = 'green'
        round_score = 1
    elif x != correct:
        result_text = "Incorrect!"
        result_color = 'red'
        round_score = -1
    else:
        Exception("something is fishy")

    q_label = tk.Label(window, text=result_text, font=title_font, fg=result_color)
    q_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
    score_label = tk.Label(window, text="score = {}".format(score+round_score), font=text_font)
    score_label.place(relx=0.9, rely=0.05, anchor=tk.CENTER)

    next_button = tk.Button(window, text = "Next round", command = window.destroy, font = text_font)
    next_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    exit_button = tk.Button(window, text="Quit", command= lambda: [window.destroy(), on_exit()], font=text_font)
    exit_button.place(relx=0.9, rely=0.9, anchor=tk.CENTER)

    window.mainloop()

    return round_score


# main
window = tk.Tk()
# window.config(bg='black')
window.title("Inventions Game")
window.geometry('700x350+100+100')

title_font = Font(family="Garamond", size=15)
text_font = Font(family="Helvetica", size=10)

welcome_text = tk.Label(window, text = "Which came first? A game about historic inventions.", font = title_font)

welcome_text.pack(side=tk.TOP, pady = 50)
play_button = tk.Button(window, text = "Play", command = window.destroy, font = text_font)
play_button.pack(side=tk.BOTTOM, pady = 50)

window.mainloop()

score = 0
while (len(inventions) >= 2) & (exit == False):
    score_change = game_round()
    score = score + score_change
print('Good game!')
