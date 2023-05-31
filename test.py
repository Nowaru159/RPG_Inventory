import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import tkinter.messagebox as messagebox
import sqlite3
import subprocess


# ---------------------defs-------------------

def add_item():
    base_window.destroy()
    subprocess.call(["python", "register_item.py"])


def att_item():
    selected_item = list.get(tk.ACTIVE)
    if selected_item:
        item_id = int(selected_item.split(" ID : ")[1].split("\n")[0])
        base_window.destroy()
        subprocess.call(["python", "update_item.py", str(item_id)])

def del_item():
    selected_item = list.get(tk.ACTIVE)
    if selected_item:
        # Extract the item name from the selected string
        item_name = selected_item.split("Nome: ")[1]

        # Display a confirmation dialog
        confirm = messagebox.askyesno("Confirmação", f"Tem certeza que deseja droppar '{item_name}'?")

        if confirm:
            con = sqlite3.connect('bdd/bdd_item.db')
            cur = con.cursor()

            cur.execute("DELETE FROM item WHERE name=?", (item_name,))

            con.commit()
            con.close()

            list.delete(tk.ACTIVE)  # Remove the item from the list

            # Update the list after deletion
            list_item()


def list_item():
    con = sqlite3.connect('bdd/bdd_item.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM item")
    rows = cur.fetchall()

    list.delete(0, tk.END)

    for row in rows:
        item_info = [
            f" ID : {row[0]} ",
            f" Nome: {row[1]}",
            f" Quantidade: {row[2]}",
            f" Peso: {row[3]}",
            f" Raridade: {row[4]}",
            f" Tipo: {row[5]}",
            f" Item de classe: {row[6]}",
            "-----------------٩(× ×)۶-----------------------٩(× ×)۶------------------"
        ]
        for info in item_info:
            list.insert(tk.END, info)

    con.close()


# --------------------------------Visual-----------------------------------

# fundo
base_window = tk.Tk()
base_window.configure(bg="#d18fee")

# fonte
fnt_negrito = tkFont.Font(family="Helvetica", size=12, weight="bold")

# deixar em grid
for a in range(10):
    for b in range(15):
        frame = tk.Frame(
            master=base_window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=a, column=b, padx=20, pady=10)

lbl_title = tk.Label(
    text="Inventário",
    fg="#183a09",
    bg="#d18fee",
    font=fnt_negrito
)

lbl_title.grid(row=0, column=0, columnspan=15, padx=10, pady=10)
# columnspan -> ele pega x qnts d colunas para espaçamento

list = tk.Listbox(
    base_window,
    fg="#183a09",
    bg="#d18fee",
    width=50,
    height=20,
    font=fnt_negrito,

)

list.grid(row=1, column=0, columnspan=15, padx=10, pady=10)

# -------------------Buttons---------------------------

btn_add = tk.Button(
    text="Cadastrar",
    font=fnt_negrito,
    fg="#183a09",
    bg="#d18fee",
    command=add_item
)

btn_list = tk.Button(
    text="Listar",
    font=fnt_negrito,
    fg="#183a09",
    bg="#d18fee",
    command=list_item
)

btn_att = tk.Button(
    text="Atualizar",
    font=fnt_negrito,
    fg="#183a09",
    bg="#d18fee",
    command=att_item
)

btn_del = tk.Button(
    text="Deletar",
    font=fnt_negrito,
    fg="#183a09",
    bg="#d18fee",
    command=del_item
)

# ---------------localização------------

btn_add.grid(row=2, column=1, padx=10, pady=10)
btn_list.grid(row=2, column=2, padx=10, pady=10)
btn_att.grid(row=2, column=3, padx=10, pady=10)
btn_del.grid(row=2, column=4, padx=10, pady=10)

base_window.mainloop()
