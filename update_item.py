import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
#from PIL import ImageTk, Image
import sqlite3
import subprocess
import sys



# ---------------------defs-------------------
def handle_update():
    if len(sys.argv) > 1:
        item_id = int(sys.argv[1])
        print(item_id)

    new_name = ent_name.get()
    new_quantity = ent_quantity.get()
    new_item_weight = ent_item_weight.get()
    new_rarity = ent_rarity.get()
    new_item_type = ent_item_type.get()
    new_item_class = ent_item_class.get()

    if new_name == "" or new_quantity == "" or new_item_weight == "" or new_rarity == "" or new_item_type == "" or new_item_class == "":
        lbl_warning.config(text="Campo(s) em branco, por favor preencha-os \n( ͠° ͟ʖ ͡°)")

    elif not new_quantity.isdigit() or not new_item_weight.isdigit():
        lbl_warning.config(text="A quantidade e/ou o peso devem ser em dígitos numéricos!\n(」°ロ°)」")

    elif new_name and new_quantity and new_item_weight and new_rarity and new_item_type and new_item_class:
        conn = sqlite3.connect('bdd/bdd_item.db')
        cursor = conn.cursor()

        cursor.execute("UPDATE item SET name=?, quantity=?, weight=?, rarity=?, type=?, item_class=? WHERE id=?",
                       (new_name, new_quantity, new_item_weight, new_rarity, new_item_type, new_item_class, item_id))

        conn.commit()
        conn.close()
        lbl_warning.config(text="Item modificado com sucesso!\n (♡°▽°♡)")

def handle_back():
    base_window.destroy()
    subprocess.call(["python","inventory_screen.py"])


# --------------------------------Visual-----------------------------------
# fundo
base_window = tk.Tk()
base_window.configure(
    bg="#d18fee"
)

# fonte
fnt_negrito = tkFont.Font(family="Helvetica", size=12, weight="bold")

# deixar em grid
for a in range(13):
    for b in range(5):
        frame = tk.Frame(
            master=base_window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=a, column=b, padx=20, pady=10)

"""# ------------------------Imagem---------------------------------
picture = Image.open(texture/safe_sign.png)
tk_image = ImageTk.PhotoImage(picture)
lbl_image = tk.Label(
    image=tk_image,
    bg="#d18fee",
)
lbl_image.grid(row=1, column=5 )"""

# ----------label----------------

lbl_warning = tk.Label(
    text='',
    fg="black",
    bg="#d18fee",
    font=fnt_negrito
)

lbl_title = tk.Label(
    text="Modificar os dados do item",
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

lbl_quantity = tk.Label(
    text="Quantidade:",
    fg="#183a09",
    bg="#d18fee",
    font=fnt_negrito
)

lbl_item_weight = tk.Label(
    text="Peso:",
    fg="#183a09",
    bg="#d18fee",
    font=fnt_negrito
)

lbl_rarity = tk.Label(
    text="Raridade:",
    fg="#183a09",
    bg="#d18fee",
    font=fnt_negrito
)

lbl_item_type = tk.Label(
    text="Tipo:",
    fg="#183a09",
    bg="#d18fee",
    font=fnt_negrito
)

lbl_item_class = tk.Label(
    text="Item de classe:",
    fg="#183a09",
    bg="#d18fee",
    font=fnt_negrito
)

# ------------------Register spaces and configs--------------

ent_name = tk.Entry(width=30)
ent_quantity = tk.Entry(width=30)
ent_item_weight = tk.Entry(width=30)
ent_rarity = ttk.Combobox(base_window, width=27,values=["Comum", "Incomum",
                                                        "Raro", "Muito Raro",
                                                        "Lendário","Artefato"])


ent_item_type = ttk.Combobox(base_window, width=27,values=["Armadura","Poção",
                                                           "Anel","Pergaminho",
                                                           "Armas","Itens maravilhosos"])


ent_item_class = ttk.Combobox(base_window, width=27, values=["Não","Guerreiro", "Mago",
                                                             "Ladino", "Clérigo"])


ent_rarity.current(0)
ent_item_type.current(0)
ent_item_class.current(0)

# -------------------Buttons---------------------------

btn_save = tk.Button(
    text="Salvar",
    font=fnt_negrito,
    fg="#183a09",
    bg="#d18fee",
    command=handle_update
)

btn_back = tk.Button(
    text="Voltar",
    font=fnt_negrito,
    fg="#183a09",
    bg="#d18fee",
    command=handle_back

)


# ----------------location----------------
lbl_title.grid(row=0, column=1, padx=2, pady=0)
lbl_warning.grid(row=2, column=1, padx=2, pady=0)
lbl_name.grid(row=3, column=0, padx=2, pady=0)
lbl_quantity.grid(row=4, column=0, padx=2, pady=0)
lbl_item_weight.grid(row=5, column=0, padx=2, pady=0)
lbl_rarity.grid(row=6, column=0, padx=2, pady=0)
lbl_item_type.grid(row=7, column=0, padx=2, pady=0)
lbl_item_class.grid(row=8, column=0, padx=2, pady=0)

ent_name.grid(row=3, column=1, padx=2, pady=0)
ent_quantity.grid(row=4, column=1, padx=2, pady=0)
ent_item_weight.grid(row=5, column=1, padx=2, pady=0)
ent_rarity.grid(row=6, column=1, padx=2, pady=0)
ent_item_type.grid(row=7, column=1, padx=2, pady=0)
ent_item_class.grid(row=8, column=1, padx=2, pady=0)

btn_save.grid(row=11, column=0,columnspan=3, padx=20, pady=10)
btn_back.grid(row=11, column=1,columnspan=3, padx=20, pady=10)


base_window.mainloop()

