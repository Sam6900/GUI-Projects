from customtkinter import *

set_widget_scaling(1.3)
win = CTk()
win.geometry("800x680")
win.title("Rapid Typo App")
win.config(padx=20, pady=20)
set_default_color_theme("green")

start_screen = CTkFrame(win)


# Start Screen
start_screen.pack(fill=BOTH, expand=True)
start_label_a = CTkLabel(start_screen, text="Welcome to Rapid Typo", font=("", 34, "bold"))
start_label_a.pack(pady=80)
start_label_b = CTkLabel(start_screen, text="Let's test your typing speed", font=("", 20, "normal"))
start_label_b.pack()

start_btn = CTkButton(start_screen, text="Start typing", command=load_main, font=("", 16, "bold"), height=32)
start_btn.pack(pady=100)
