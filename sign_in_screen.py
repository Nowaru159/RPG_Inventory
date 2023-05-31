import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
#from PIL import ImageTk, Image
import sqlite3
import subprocess


# ---------------------defs-------------------

def handle_register():
    name = ent_name.get()
    cpf = ent_cpf.get()
    sex = ent_sex.get()
    client_class = ent_client_class.get()
    tel = ent_tel.get()
    birth = ent_birth.get()
    mail = ent_mail.get()
    username = ent_username.get()
    password = ent_password.get()
    cep = ent_cep.get()
    adress = ent_adress.get()

    if name == "" or cpf == "" or sex == "" or client_class == "" or tel == "" or birth == "" or mail == "" \
            or username == "" or password == "" or cep == "" or adress == "":
        lbl_warning.config(text="Campo(s) em branco, por favor preencha-os (눈_눈)")

    elif name and cpf and sex and client_class and tel and birth and username and password and cep \
            and adress and "@" not in mail:
        lbl_warning.config(text='Cadastre um e-mail válido, por favor (`△´＃)')

    elif name and cpf and sex and client_class and tel and birth and username and len(
            password) < 6 and cep and adress and "@" in mail:
        lbl_warning.config(text='Senha muito curta, por favor, ponha no mínimo 6 caracteres (￣ ￣|||)')

    elif name and cpf and sex and client_class and tel and birth and mail and username and password and cep and adress:
        conn = sqlite3.connect('bdd/bdd_user.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO user (name, cpf, sex, client_class, tel, birth, mail, username, password, cep, adress) "
            ' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            , (name, cpf, sex, client_class,
               tel, birth, mail, username,
               password, cep, adress))
        conn.commit()
        conn.close()

        lbl_warning.config(text='Usuário cadastrado com sucesso!	♡＼(￣▽￣)／♡')

    else:
        lbl_warning.config(text="Algo de errado não está certo e não sei o que é ...(￢_￢;)")


def handle_back():
    base_window.destroy()
    subprocess.call(["python","start_screen.py"])



# --------------------------------Visual-----------------------------------
# fundo
base_window = tk.Tk()
base_window.configure(
    bg="#d18fee"
)

# fonte
fnt_negrito = tkFont.Font(family="Helvetica", size=12, weight="bold")

# deixar em grid
for a in range(16):
    for b in range(5):
        frame = tk.Frame(
            master=base_window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=a, column=b, padx=20, pady=10)

"""# ------------------------Imagem---------------------------------
picture = Image.open("texture/owl_bear.png")
tk_image = ImageTk.PhotoImage(picture)
lbl_image = tk.Label(
    image=tk_image,
    bg="#d18fee",
)
lbl_image.grid(row=1, column=1, )"""

# ----------label----------------

lbl_warning = tk.Label(
    text='',
    fg="black",
    bg="#d18fee",
    font=fnt_negrito
)

lbl_title = tk.Label(
    text="Cadastro de Usuário",
    fg="#183a09",
    bg="#d18fee",
    font=fnt_negrito
)

lbl_name = tk.Label(
    text="Nome:",
    fg="#183a09",
    bg="#d18fee",
    font=fnt_negrito
)

lbl_cpf = tk.Label(
    text="CPF:",
    fg="#183a09",
    bg="#d18fee",
    font=fnt_negrito
)

lbl_sex = tk.Label(
    text="Sexo:",
    fg="#183a09",
    bg="#d18fee",
    font=fnt_negrito
)

lbl_client_class = tk.Label(
    text="Classe:",
    fg="#183a09",
    bg="#d18fee",
    font=fnt_negrito
)

lbl_tel = tk.Label(
    text="Telefone:",
    fg="#183a09",
    bg="#d18fee",
    font=fnt_negrito
)

lbl_birth = tk.Label(
    text="Data de Nascimento:",
    fg="#183a09",
    bg="#d18fee",
    font=fnt_negrito
)

lbl_mail = tk.Label(
    text="E-mail:",
    fg="#183a09",
    bg="#d18fee",
    font=fnt_negrito
)

lbl_username = tk.Label(
    text="Username:",
    fg="#183a09",
    bg="#d18fee",
    font=fnt_negrito
)

lbl_password = tk.Label(
    text="Senha:",
    fg="#183a09",
    bg="#d18fee",
    font=fnt_negrito
)

lbl_cep = tk.Label(
    text="CEP:",
    fg="#183a09",
    bg="#d18fee",
    font=fnt_negrito
)

lbl_adress = tk.Label(
    text="Endereço:",
    fg="#183a09",
    bg="#d18fee",
    font=fnt_negrito
)
# ------------------Register spaces and configs--------------

ent_name = tk.Entry(width=30)
ent_cpf = tk.Entry(width=30)
ent_sex = ttk.Combobox(base_window, width=27,values=["Miojo","F","M"])
ent_sex.current(0)
ent_client_class = ttk.Combobox(base_window, width=27, values=["Guerreiro", "Mago", "Ladino", "Clérigo"])
ent_client_class.current(0)
ent_tel = tk.Entry(width=30)
ent_birth = tk.Entry(width=30)
ent_mail = tk.Entry(width=30)
ent_username = tk.Entry(width=30)
ent_password = tk.Entry(width=30)
ent_cep = tk.Entry(width=30)
ent_adress = tk.Entry(width=30)

# ----------------location----------------
lbl_title.grid(row=0, column=0,columnspan=16)
lbl_warning.grid(row=2, column=1, padx=2)
lbl_name.grid(row=3, column=0, padx=2)
lbl_cpf.grid(row=4, column=0, padx=2)
lbl_sex.grid(row=5, column=0, padx=2)
lbl_client_class.grid(row=6, column=0, padx=2)
lbl_tel.grid(row=7, column=0, padx=2)
lbl_birth.grid(row=8, column=0, padx=2)
lbl_mail.grid(row=9, column=0, padx=2)
lbl_username.grid(row=10, column=0, padx=2)
lbl_password.grid(row=11, column=0, padx=2)
lbl_cep.grid(row=12, column=0, padx=2)
lbl_adress.grid(row=13, column=0, padx=2)

ent_name.grid(row=3, column=1, padx=2)
ent_cpf.grid(row=4, column=1, padx=2)
ent_sex.grid(row=5, column=1, padx=2)
ent_client_class.grid(row=6, column=1, padx=2)
ent_tel.grid(row=7, column=1, padx=2)
ent_birth.grid(row=8, column=1, padx=2)
ent_mail.grid(row=9, column=1, padx=2)
ent_username.grid(row=10, column=1, padx=2)
ent_password.grid(row=11, column=1, padx=2)
ent_cep.grid(row=12, column=1, padx=2)
ent_adress.grid(row=13, column=1, padx=2)

# -------------------Buttons---------------------------
# Sign in
btn_signin = tk.Button(
    text="Cadastrar",
    font=fnt_negrito,
    fg="#183a09",
    bg="#d18fee",
    command=handle_register
)
btn_signin.grid(row=14, column=1, pady=10)

btn_back = tk.Button(
    text="Voltar",
    font=fnt_negrito,
    fg="#183a09",
    bg="#d18fee",
    command=handle_back
)
btn_back.grid(row=15, column=1, padx=20, pady=10)

base_window.mainloop()
