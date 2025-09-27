from tkinter import *
import elo_backend as bck

main_app = Tk()
main_app.geometry("800x900")
main_app.title("ELO calculator GUI")

title = Label(main_app, text="ELO GUI", height=2, width=30, font=("Helvetica", 30, "bold"))
title.pack()

# Enter Player A's Original ELO
player_A_text = Label(main_app, text="Player A ELO: ", font=("Helvetica", 16))
player_A_text.place(x=100, y=200)
player_A_entry = Entry(main_app)
player_A_entry.place(x=250, y=198)

# Enter Player B's Original ELO
player_B_text = Label(main_app, text="Player B ELO: ", font=("Helvetica", 16))
player_B_text.place(x=100, y=250)
player_B_entry = Entry(main_app)
player_B_entry.place(x=250, y=248)

number_of_sets = IntVar(value=0)

set_entries = []  # global or declared outside the function

def update_set_entries():
    global set_entries
    set_entries = []  # reset when updating

    # Clear any existing widgets inside the frame
    for widget in set_scores.winfo_children():
        widget.destroy()

    # New Entry boxes based on number_of_sets
    for i in range(1, number_of_sets.get() + 1):
        lbl = Label(set_scores, text=f"Set {i}:", font=("Arial", 16))
        lbl.grid(row=i - 1, column=0, padx=10, pady=10)

        entry = Entry(set_scores, font=("Arial", 12), width=5)
        entry.grid(row=i - 1, column=1, padx=10)
        
        set_entries.append(entry)  # save reference

# Choose Set box
set_decide = LabelFrame(main_app, text="SETS PLAYED", font=("Arial", 16, "bold"))
set_decide.place(x=515, y=170, width=170, height=200)

Radiobutton(set_decide, text="One", variable=number_of_sets, value=1, font=("Arial", 16), command=update_set_entries).place(x=20, y=20)
Radiobutton(set_decide, text="Two", variable=number_of_sets, value=2, font=("Arial", 16), command=update_set_entries).place(x=20, y=60)
Radiobutton(set_decide, text="Three", variable=number_of_sets, value=3, font=("Arial", 16), command=update_set_entries).place(x=20, y=100)

# Score for each set
set_scores = LabelFrame(main_app, text="SET SCORES", font=("Arial", 16, "bold"))
set_scores.place(x=515, y=400, width=170, height=200)

# Results contained in a box

result_box = LabelFrame(main_app, text="RESULTS", font=("Arial", 16, "bold"))
result_box.place(x=100, y=500, width=300, height = 200)

# Player A New ELO

new_elo_a = Label(result_box, text="Player A: ", font=("Arial", 14, "bold"))
new_elo_a.place(x = 40, y = 10)

# Player B New ELO

new_elo_b = Label(result_box, text="Player B: ", font=("Arial", 14, "bold"))
new_elo_b.place(x = 40, y = 40)

# Change in ELO

change_in_elo_text = Label(result_box, text="ELO change: ", font=("Arial", 14, "bold"))
change_in_elo_text.place(x = 40, y = 70)

# Error raising

error_text = Label(result_box, font=("Arial", 14, "bold"))
error_text.place(x=20, y=100)

# Calculate button

def calculate():
    set_scores_list = []
    for entry in set_entries:
        val = entry.get()
        set_scores_list.append(val)

    if len(set_scores_list) == 1:
        set_scores_list.append("0:0")
        set_scores_list.append("0:0")
    if len(set_scores_list) == 2:
        set_scores_list.append("0:0")
    
    print(set_scores_list)

    rA = int(player_A_entry.get())
    rB = int(player_B_entry.get())
    sets_played = number_of_sets.get()

    new_a, new_b, elo_change, error = bck.update_player_elo(rA, rB, sets_played, set_scores_list[0], set_scores_list[1], set_scores_list[2])

    # Update GUI
    if error == 0:
        new_elo_a.config(text=f"Player A: {new_a}")
        new_elo_b.config(text=f"Player B: {new_b}")
        change_in_elo_text.config(text=f"ELO change: {elo_change}")
    else:
        error_text.config(text=f"Error: Can't have 3 winning\n sets for one player", fg="red")


calculate_button = Button(main_app, text = "CALCULATE", font=("Helvetica", 20, "bold"), bd=3, command=calculate).place(x=150, y=350, width = 200, height = 60)

main_app.mainloop()
