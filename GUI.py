from tkinter import *

main_app = Tk()
main_app.geometry("800x900")
main_app.title("ELO calculator GUI")

title = Label(main_app, text="ELO GUI", height=2, width=30,
              font=("Helvetica", 30, "bold"))
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

# Callback to update set entries dynamically
def update_set_entries():
    # Clear any existing widgets inside the frame
    for widget in set_scores.winfo_children():
        widget.destroy()

    # New Entry boxes based on number_of_sets
    for i in range(1, number_of_sets.get() + 1):
        Label(set_scores, text=f"Set {i}:", font=("Arial", 16)).place(x=20, y=40*(i-1)+20)
        Entry(set_scores).place(x=80, y=40*(i-1)+21, width=45)

# Choose Set box
set_decide = LabelFrame(main_app, text="SETS PLAYED", font=("Arial", 16, "bold"))
set_decide.place(x=515, y=170, width=170, height=200)

Radiobutton(set_decide, text="One", variable=number_of_sets, value=1, font=("Arial", 16), command=update_set_entries).place(x=20, y=20)
Radiobutton(set_decide, text="Two", variable=number_of_sets, value=2, font=("Arial", 16), command=update_set_entries).place(x=20, y=60)
Radiobutton(set_decide, text="Three", variable=number_of_sets, value=3, font=("Arial", 16), command=update_set_entries).place(x=20, y=100)

# Score for each set
set_scores = LabelFrame(main_app, text="SET SCORES", font=("Arial", 16, "bold"))
set_scores.place(x=515, y=400, width=170, height=200)

# Calculate button

calculate_button = Button(main_app, text = "CALCULATE", font=("Helvetica", 20, "bold"), bd=3).place(x=150, y=350, width = 200, height = 60)

main_app.mainloop()
