from customtkinter import *

set_widget_scaling(1.3)
win = CTk()
win.geometry("750x600")
win.title("Disappearing Text App")
win.config(padx=20, pady=20)

start_frame = CTkFrame(win)
main_frame = CTkFrame(win)
end_frame = CTkFrame(win)

start_frame.pack(fill=BOTH, expand=True)
title_label = CTkLabel(start_frame, text="The Disappearing Text App", font=("", 34, "bold"))
title_label.pack(pady=70)

time_limit_frame = CTkFrame(start_frame)
time_limit_frame.pack()

time_limit_label_a = CTkLabel(time_limit_frame, text="Set time limit : ", font=("", 15, "normal"))
time_limit_label_a.pack(side=LEFT, padx=(100, 10), pady=10)
time_limit = CTkEntry(time_limit_frame, width=40)
time_limit.pack(side=LEFT)
time_limit.focus()
time_limit_label_b = CTkLabel(time_limit_frame, text="minutes", font=("", 15, "normal"))
time_limit_label_b.pack(side=LEFT, padx=(10, 120))

start_btn = CTkButton(start_frame, text="Start")
start_btn.pack(pady=(90, 0))

win.mainloop()
