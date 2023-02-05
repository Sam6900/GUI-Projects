from customtkinter import *

writing_time = 0
written_text = ""
not_writing_time = 0
progress_bar_timer = None
set_widget_scaling(1.3)


def load_main():
    main_screen.pack(fill=BOTH, expand=True)
    start_screen.pack_forget()


def on_focus_in(event):
    global writing_time
    if event.widget.get("1.0", "end-1c") == "Click to start typing your story...":
        event.widget.delete("1.0", END)
        my_text.configure(text_color="white")
        time_mins = time_limit.get()
        if time_mins.isdigit():
            time_mins = int(time_mins)
        else:
            time_mins = 3
        writing_time = time_mins * 60
        update_time_bar()


def handle_writing():
    global written_text, not_writing_time
    text = my_text.get("1.0", END).strip()
    if text == written_text:
        not_writing_time += 0.5
    else:
        written_text = text
        not_writing_time = 0
    if 3 <= not_writing_time < 5:
        time_bar.configure(progress_color="#DC3535")
    elif 5 <= not_writing_time < 7:
        time_bar.configure(progress_color="#CD0404")
    elif not_writing_time == 7:
        load_timeup()
    else:
        time_bar.configure(progress_color="#36719F")


def update_time_bar():
    global progress_bar_timer
    handle_writing()
    progress = time_bar.get()
    if progress == 1:
        load_finish()
    time_bar.set(progress + 1/(writing_time * 2))
    if progress != 1 and not_writing_time < 7:
        progress_bar_timer = win.after(500, update_time_bar)


def load_timeup():
    win.after_cancel(progress_bar_timer)
    timeup_screen.pack(fill=BOTH, expand=True)
    main_screen.pack_forget()


def load_finish():
    win.after_cancel(progress_bar_timer)
    finish_text.configure(state="normal")
    finish_text.insert("1.0", my_text.get("1.0", END))
    finish_text.configure(state="disabled")
    finish_screen.pack(fill=BOTH, expand=True)
    main_screen.pack_forget()


def reload_main():
    global written_text, not_writing_time
    time_bar.set(0)
    written_text = ""
    not_writing_time = 0
    my_text.delete("1.0", END)
    my_text.insert("1.0", "Click to start typing your story...")
    my_text.configure(text_color="#FECB89")
    time_bar.focus_set()
    main_screen.pack(expand=True, fill=BOTH)
    timeup_screen.pack_forget()
    finish_screen.pack_forget()


win = CTk()
win.geometry("750x600")
win.title("Disappearing Text App")
win.config(padx=20, pady=20)

start_screen = CTkFrame(win)
main_screen = CTkFrame(win)
timeup_screen = CTkFrame(win)
finish_screen = CTkFrame(win)


# Start Screen
start_screen.pack(fill=BOTH, expand=True)
title_label = CTkLabel(start_screen, text="The Disappearing Text App", font=("", 34, "bold"))
title_label.pack(pady=70)

time_limit_frame = CTkFrame(start_screen)
time_limit_frame.pack()

time_limit_label_a = CTkLabel(time_limit_frame, text="Set time limit for your story: ", font=("", 15, "normal"))
time_limit_label_a.pack(side=LEFT, padx=(20, 10), pady=10)
time_limit = CTkEntry(time_limit_frame, width=40, justify='center')
time_limit.insert(0, "3")
time_limit.pack(side=LEFT)
time_limit_label_b = CTkLabel(time_limit_frame, text="minutes", font=("", 15, "normal"))
time_limit_label_b.pack(side=LEFT, padx=(10, 20))

start_btn = CTkButton(start_screen, text="Start", command=load_main)
start_btn.pack(pady=(90, 0))


# Main Screen
time_bar = CTkProgressBar(main_screen, width=490, height=5, progress_color="#36719F", corner_radius=0)
time_bar.set(0)
time_bar.pack(pady=(20, 0))

my_text = CTkTextbox(main_screen, width=500, height=380, spacing2=8, font=("", 14), text_color="#FECB89", wrap=WORD)
my_text.insert(END, "Click to start typing your story...")
my_text.bind("<FocusIn>", on_focus_in)
my_text.pack()


# Time Up Screen
timeup_label = CTkLabel(timeup_screen, text="Whoops! your story disappeared", font=("", 20, "normal"))
timeup_label.pack(pady=(150, 30))

return_btn = CTkButton(timeup_screen, text="← Write Again", font=("", 15, "bold"), command=reload_main)
return_btn.pack()


# Finish Screen
finish_label = CTkLabel(finish_screen, text="Here's your story", font=("", 20, "normal"))
finish_label.pack(pady=(20, 20))

finish_text = CTkTextbox(finish_screen, width=500, height=260, spacing2=8, font=("", 13), text_color="#FECB89", wrap=WORD)
finish_text.pack()

return_btn = CTkButton(finish_screen, text="← Write Again", font=("", 15, "bold"), command=reload_main)
return_btn.pack(pady=30)


win.mainloop()
