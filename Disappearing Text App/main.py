from customtkinter import *

set_widget_scaling(1.4)
win = CTk()
win.geometry("800x600")
win.title("Disappearing Text App")
win.config(padx=20, pady=20)

start_frame = CTkFrame(win)
main_frame = CTkFrame(win)
end_frame = CTkFrame(win)

start_frame.pack(fill=BOTH, expand=True)
title_label = CTkLabel(start_frame, text="The Disappearing Text App", font=("", 34, "bold"))
title_label.pack(pady=80)

time_limit_label_a = CTkLabel(start_frame, text="Set time limit", font=("", 15, "normal"))
time_limit_label_a.pack()

time_limit = CTkEntry(start_frame)
time_limit.pack()
time_limit.focus()

time_limit_label_b = CTkLabel(start_frame, text="minutes", font=("", 15, "normal"))
time_limit_label_b.pack()

start_btn = CTkButton(start_frame, text="Start")
start_btn.pack(pady=70)

win.mainloop()
