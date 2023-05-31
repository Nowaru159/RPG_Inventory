import tkinter as tk
import tkinter.font as tkFont
import sqlite3
import subprocess
# from PIL import ImageTk, Image
from tkinter import END


# 1804
# site de cor https://www.colorhexa.com/d18fee
# imagens https://www.redbubble.com/people/ArcanaGames/shop tamanho250x250
#          ref
# https://docs.python.org/3/library/tk.html
# https://www.tutorialspoint.com/
# https://pythonexamples.org/
# https://pt.stackoverflow.com/
#https://www.geeksforgeeks.org/
#https://pythonguides.com/
# ---------------------defs-------------------

def on_ent_username_click(event):
    if ent_user.get() == "Usuário":
        ent_user.delete(0, END)
        ent_user.config(fg="#183a09")


def on_ent_password_click(event):
    if ent_password.get() == "Senha":
        ent_password.delete(0, END)
        ent_password.config(show="*")
        ent_password.config(fg="#183a09")


def handle_login():
    username = ent_user.get()
    password = ent_password.get()

    conn = sqlite3.connect('bdd/bdd_user.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    conn.close()

    if result:
        base_window.destroy()
        subprocess.call(["python", "inventory_screen.py"])
    else:
        lbl_warning.config(text="Senha e/ou usuário incorretos(ಡ‸ಡ)")


def handle_new_user():
    base_window.destroy()
    subprocess.call(["python", "sign_in_screen.py"])


# fundo
base_window = tk.Tk()
base_window.configure(bg="#d18fee")

# fontes
fnt_negrito = tkFont.Font(family="Helvetica", size=12, weight="bold")

# deixar em grid
for a in range(7):
    for b in range(3):
        frame = tk.Frame(
            master=base_window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=a, column=b, padx=20, pady=20)

# titulo de boas vindas

lbl_title = tk.Label(
    text='Seja bem-vindo ao Achados da Irmandade\n '
         'Organize seu inventário conosco!\n (งÒ-Ó)ง',
    fg="#183a09",
    bg="#d18fee",
    font=fnt_negrito
)
lbl_title.grid(row=0, column=1, padx=0, pady=0)

"""# ------------------------Imagem---------------------------------
picture = Image.open("texture/blink_dog.png")
tk_image = ImageTk.PhotoImage(picture)
lbl_image = tk.Label(
    image=tk_image,
    bg="#d18fee"
)
lbl_image.grid(row=1, column=1)"""

# ---------------------------User login---------------------------------------------------

# Entry
ent_user = tk.Entry()
ent_user.insert(0, "Usuário")
ent_user.bind("<FocusIn>", on_ent_username_click)
ent_user.grid(row=3, column=1)

# ---------------------------Password login---------------------------------------------------
# Entry
ent_password = tk.Entry()
ent_password.insert(0, "Senha")
ent_password.bind("<FocusIn>", on_ent_password_click)
ent_password.grid(row=4, column=1)

# ---------------------------Warning Login---------------------------------------------------
lbl_warning = tk.Label(
    text='',
    fg="black",
    bg="#d18fee",
    font=fnt_negrito
)
lbl_warning.grid(row=2, column=1, padx=0, pady=0)
# -------------------Buttons---------------------------
# Log in
btn_login = tk.Button(
    text="Entrar",
    font=fnt_negrito,
    fg="#183a09",
    bg="#d18fee",
    command=handle_login
)
btn_login.grid(row=5, column=1)

# Cadastro
btn_signin = tk.Button(
    text="Novo Usuário",
    font=fnt_negrito,
    fg="#183a09",
    bg="#d18fee",
    command=handle_new_user
)
btn_signin.grid(row=6, column=1, pady=10)

base_window.mainloop()

