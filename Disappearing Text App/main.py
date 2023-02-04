from customtkinter import *


def load_main():
    main_screen.pack(fill=BOTH, expand=True)
    start_screen.pack_forget()


def on_focus_in(event):
    if event.widget.get("1.0", "end-1c") == "Start typing...":
        event.widget.delete("1.0", END)
        my_text.configure(text_color="white")


set_widget_scaling(1.3)
win = CTk()
win.geometry("750x600")
win.title("Disappearing Text App")
win.config(padx=20, pady=20)

start_screen = CTkFrame(win)
main_screen = CTkFrame(win)
end_screen = CTkFrame(win)


# Start Screen
start_screen.pack(fill=BOTH, expand=True)
title_label = CTkLabel(start_screen, text="The Disappearing Text App", font=("", 34, "bold"))
title_label.pack(pady=70)

time_limit_frame = CTkFrame(start_screen)
time_limit_frame.pack()

time_limit_label_a = CTkLabel(time_limit_frame, text="Set time limit : ", font=("", 15, "normal"))
time_limit_label_a.pack(side=LEFT, padx=(100, 10), pady=10)
time_limit = CTkEntry(time_limit_frame, width=40, justify='center')
time_limit.insert(0, "3")
time_limit.pack(side=LEFT)
time_limit_label_b = CTkLabel(time_limit_frame, text="minutes", font=("", 15, "normal"))
time_limit_label_b.pack(side=LEFT, padx=(10, 120))

start_btn = CTkButton(start_screen, text="Start", command=load_main)
start_btn.pack(pady=(90, 0))


# Main Screen
time_bar = CTkProgressBar(main_screen, width=490, height=5, progress_color="blue", corner_radius=0)
time_bar.pack(pady=(20, 0))

my_text = CTkTextbox(main_screen, width=500, height=380, spacing2=8, font=("", 14), text_color="#FECB89", wrap=WORD)
my_text.insert(END, "Start typing...")
my_text.bind("<FocusIn>", on_focus_in)
my_text.pack()

win.mainloop()
