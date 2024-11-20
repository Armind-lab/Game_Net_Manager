import GameNetDatabase
from customtkinter import *
from CTkMessagebox import CTkMessagebox
from time import time

def reg():
    global playing
    n = sname.get().strip()
    s = console.get()
    p = player.get()
    sr = time()
    u = GameNetDatabase.user_info()

    if n.isspace() or len(n) < 3:
        CTkMessagebox(title="error", message="name must be at least 3 characters")
    else:
        if s.isspace() or s == "Console":
            CTkMessagebox(title="Error", message="Console can't be empty")
        else:
            if p.isspace() or p == "Player":
                CTkMessagebox(title="Error", message="Player can't be empty")
            else:
                for i in u:
                    if i[0] == n:
                        CTkMessagebox(title="Error", message="User already registered")
                        break
                else:
                    GameNetDatabase.add_to_database(n , s , p , sr)
                    sname.delete(0, END)
                    resul = GameNetDatabase.user_info()
                    playing = [i[0] for i in resul]
                    playing.remove("نام")
                    fname.configure(values=playing)
                    show()

def show():
    for label in users.winfo_children():
        label.destroy()
    h = 30
    res = GameNetDatabase.user_info()
    for i in res:
        CTkLabel(master=users , text=i[0] , font=("Arial", 32)).place(x=550, y=h, anchor=E)
        CTkLabel(master=users , text=i[1], font=("Arial", 32)).place(x=320, y=h, anchor=E)
        CTkLabel(master=users , text=i[2], font=("Arial", 32)).place(x=90, y=h, anchor=E)
        h += 50

def settings():
    global settings_page
    global ps4_1_price_entry , ps4_2_price_entry , ps4_3_price_entry ,ps4_4_price_entry , ps5_1_price_entry ,ps5_2_price_entry ,ps5_3_price_entry ,ps5_4_price_entry
    try:
        settings_page.destroy()
    except:
        pass
    settings_page = CTk()
    settings_page.title("Settings")
    settings_page.resizable(False, False)
    settings_page.geometry("400x360")

    res = GameNetDatabase.price_info()

    ps4_tag = CTkLabel(master=settings_page, text="PS4", font=("Arial", 32))
    ps5_tag = CTkLabel(master=settings_page, text="PS5", font=("Arial", 32))

    one_player_tag = CTkLabel(master=settings_page, text="1", font=("Arial", 32))
    two_player_tag = CTkLabel(master=settings_page, text="2", font=("Arial", 32))
    three_player_tag = CTkLabel(master=settings_page, text="3", font=("Arial", 32))
    four_player_tag = CTkLabel(master=settings_page, text="4", font=("Arial", 32))

    ps4_1_price_entry = CTkEntry(master=settings_page, font=("Arial", 32), placeholder_text=res[0])
    ps4_2_price_entry = CTkEntry(master=settings_page, font=("Arial", 32), placeholder_text=res[1])
    ps4_3_price_entry = CTkEntry(master=settings_page, font=("Arial", 32), placeholder_text=res[2])
    ps4_4_price_entry = CTkEntry(master=settings_page, font=("Arial", 32), placeholder_text=res[3])
    ps5_1_price_entry = CTkEntry(master=settings_page, font=("Arial", 32), placeholder_text=res[4])
    ps5_2_price_entry = CTkEntry(master=settings_page, font=("Arial", 32), placeholder_text=res[5])
    ps5_3_price_entry = CTkEntry(master=settings_page, font=("Arial", 32), placeholder_text=res[6])
    ps5_4_price_entry = CTkEntry(master=settings_page, font=("Arial", 32), placeholder_text=res[7])

    save_btn = CTkButton(master=settings_page, text="Save", font=("Arial", 32), command=save_settings)

    ps4_tag.place(x=100, y=13)
    ps5_tag.place(x=270, y=13)

    one_player_tag.place(x=20, y=63)
    two_player_tag.place(x=20, y=123)
    three_player_tag.place(x=20, y=183)
    four_player_tag.place(x=20, y=243)

    ps4_1_price_entry.place(x=60, y=60)
    ps4_2_price_entry.place(x=60, y=120)
    ps4_3_price_entry.place(x=60, y=180)
    ps4_4_price_entry.place(x=60, y=240)
    ps5_1_price_entry.place(x=230, y=60)
    ps5_2_price_entry.place(x=230, y=120)
    ps5_3_price_entry.place(x=230, y=180)
    ps5_4_price_entry.place(x=230, y=240)

    save_btn.place(x=140, y=300)

    settings_page.mainloop()

def save_settings():
    res = GameNetDatabase.price_info()

    p41 = ps4_1_price_entry.get()
    p42 = ps4_2_price_entry.get()
    p43 = ps4_3_price_entry.get()
    p44 = ps4_4_price_entry.get()
    p51 = ps5_1_price_entry.get()
    p52 = ps5_2_price_entry.get()
    p53 = ps5_3_price_entry.get()
    p54 = ps5_4_price_entry.get()

    if len(p41.strip()) == 0:
        p41 = res[0]
    if len(p42.strip()) == 0:
        p42 = res[1]
    if len(p43.strip()) == 0:
        p43 = res[2]
    if len(p44.strip()) == 0:
        p44 = res[3]
    if len(p51.strip()) == 0:
        p51 = res[4]
    if len(p52.strip()) == 0:
        p52 = res[5]
    if len(p53.strip()) == 0:
        p53 = res[6]
    if len(p54.strip()) == 0:
        p54 = res[7]

    GameNetDatabase.add_price(p41, p42, p43, p44, p51, p52, p53, p54)
    settings_page.destroy()

def finish():
    n = fname.get()
    res = GameNetDatabase.user_info()
    price = GameNetDatabase.price_info()
    for i in res:
        if i[0] == n:
            if i[1] == "PS4":
                if i[2] == "1":
                    x = price[0]
                elif i[2] == "2":
                    x = price[1]
                elif i[2] == "3":
                    x = price[2]
                elif i[2] == "4":
                    x = price[3]
            elif i[1] == "PS5":
                if i[2] == "1":
                    x = price[4]
                elif i[2] == "2":
                    x = price[5]
                elif i[2] == "3":
                    x = price[6]
                elif i[2] == "4":
                    x = price[7]
            GameNetDatabase.delete_user(n)
            fname.set("")
            resul = GameNetDatabase.user_info()
            playing = [i[0] for i in resul]
            playing.remove("نام")
            fname.configure(values=playing)
            sp = time()
            pt = sp - i[3]
            out = int(pt // 3600)
            remain = round((pt - (out * 3600)) / 60)
            if pt < 60 :
                txt = round(pt)
                t = "Seconds"
            else:
                txt = round(pt / 60)
                t = "Minutes"
            if pt < 3550:
                msg = f"You've been playing for {txt} {t}\nyou're bill is {round(pt / 3600 * x)} Toman"
            else:
                msg = f"You've been playing for {out} hours and {remain} minutes\nyou're bill is {(round(pt / 3600 * x / 1000)) * 1000} Toman"
            CTkMessagebox(title="Done", message=msg)
            show()
            break
    else:
        CTkMessagebox(title="Error", message="User didn't found")

root = CTk()
root.geometry("600x600")

resul = GameNetDatabase.user_info()

playing = [i[0] for i in resul]
playing.remove("نام")

config = CTkFrame(master=root, width=580, height=115)

sname = CTkEntry(master=config, font=("Arial", 28), width=140, placeholder_text="Name")

fname = CTkComboBox(master=config, values=playing, font=("Arial", 28), dropdown_font=("Arial", 18), width=135, state="readonly")
fname.set("Stop")

console = CTkComboBox(master=config, values=["PS4", "PS5"], width=140, font=("Arial", 28), state="readonly")
console.set("Console")

player = CTkComboBox(master=config, values=["1", "2", "3", "4"], width=135, font=("Arial", 28), state="readonly")
player.set("Player")

add = CTkButton(master=config, text="add", font=("Arial", 44), width=130, height=94, command=reg)

done = CTkButton(master=config, text="done", font=("Arial", 44), width=130, height=94, command=finish)

users = CTkFrame(master=root, width=580, height=458)

settings_btn = CTkButton(master=root, text="Settings", font=("Arial", 32), command=settings)

config.place(x=10, y=10)
sname.place(x=292, y=10)
fname.place(x=148, y=10)
console.place(x=292, y=60)
player.place(x=148, y=60)
add.place(x=440, y=10)
done.place(x=10, y=10)
users.place(x=300, y=362, anchor=CENTER)
settings_btn.place(x=300, y=560, anchor=CENTER)

show()

root.mainloop()