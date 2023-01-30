from customtkinter import *


def load_main():
    main_screen.pack(fill=BOTH, expand=True)
    start_screen.pack_forget()
    

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
