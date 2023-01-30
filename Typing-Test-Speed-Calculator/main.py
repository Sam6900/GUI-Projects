from customtkinter import *


def load_main():
    main_screen.pack(fill=BOTH, expand=True)
    start_screen.pack_forget()


def count_down(count):
    if count < 10:
        time_label.configure(text=f"0{count}")
    else:
        time_label.configure(text=count)
    if count > 0:
        win.after(1000, count_down, count - 1)


def on_focus_in(event):
    if event.widget.get("1.0", "end-1c") == "Click to Start timer":
        event.widget.delete("1.0", END)
        my_text.configure(text_color="white")
        count_down(time_limit)


set_widget_scaling(1.3)
win = CTk()
win.geometry("800x680")
win.title("Rapid Typo App")
win.config(padx=20, pady=20)
set_default_color_theme("green")

start_screen = CTkFrame(win)
main_screen = CTkFrame(win)
score_screen = CTkFrame(win)


# Start Screen
start_screen.pack(fill=BOTH, expand=True)
start_label_a = CTkLabel(start_screen, text="Welcome to Rapid Typo", font=("", 34, "bold"))
start_label_a.pack(pady=80)
start_label_b = CTkLabel(start_screen, text="Let's test your typing speed", font=("", 20, "normal"))
start_label_b.pack()

start_btn = CTkButton(start_screen, text="Start typing", command=load_main, font=("", 16, "bold"), height=32)
start_btn.pack(pady=100)


# Main Screen
type_text = CTkTextbox(main_screen, width=420, height=200, activate_scrollbars=False, wrap=WORD, font=("Arial", 14), spacing2=8, text_color="#FBE6D4")
text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's "\
       "standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to " \
       "make a type specimen book. It has survived not only five centuries, but also the leap into electronic " \
       "typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset " \
       "sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus " \
       "PageMaker including versions of Lorem Ipsum."
type_text.insert("0.0", text)
type_text.configure(state="disabled")
type_text.pack(pady=20)

time_limit = 30
time_label = CTkLabel(main_screen, text=str(time_limit), font=("Courier", 35, "bold"), text_color="#FFA931")
time_label.pack()

my_text = CTkTextbox(main_screen, width=420, height=180, spacing2=8, font=("", 13), text_color="#FECB89", wrap=WORD)
my_text.insert(END, "Click to Start timer")
my_text.bind("<FocusIn>", on_focus_in)
my_text.pack(pady=10)
