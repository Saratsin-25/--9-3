import requests
import  json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_t_label(event):
    code = t_combobox.get()
    name = cur[code]
    t_label.config(text=name)


def update_b1_label(event):
    code1 = b1_combobox.get()
    name1 = cur[code1]
    b1_label.config(text=name1)

def update_b2_label(event):
    code2 = b2_combobox.get()
    name2 = cur[code2]
    b2_label.config(text=name2)


def exchange():
    t_code = t_combobox.get()
    b1_code = b1_combobox.get()
    b2_code = b2_combobox.get()

    if t_code and b1_code and b2_code:
        try:
            response1 = requests.get(f'https://open.er-api.com/v6/latest/{b1_code}')
            response1.raise_for_status()
            data1=response1.json()
            if t_code in data1['rates']:
                exchange_rate1 = data1['rates'][t_code]
                t_name=cur[t_code]
                b1_name = cur[b1_code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate1:.2f} {t_name} за один {b1_name}")
            else:
                mb.showerror("Ошибка", f"Валюта {t_code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!", f"Введите код валюты!")

cur = {
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум",
    "USD": "Американский доллар"
    }

window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x460")

Label(text="Базовая валюта").pack(padx=10, pady=10)
b1_combobox = ttk.Combobox(values=list(cur.keys()))
b1_combobox.pack(padx=10, pady=10)
b1_combobox.bind("<<ComboboxSelected>>", update_b1_label)

b1_label = ttk.Label()
b1_label.pack(padx=10, pady=10)

Label(text="Вторая базовая валюта").pack(padx=10, pady=10)
b2_combobox = ttk.Combobox(values=list(cur.keys()))
b2_combobox.pack(padx=10, pady=10)
b2_combobox.bind("<<ComboboxSelected>>", update_b2_label)

b2_label = ttk.Label()
b2_label.pack(padx=10, pady=10)




Label(text="Целевая валюта").pack(padx=10, pady=10)
t_combobox = ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(padx=10, pady=10)
t_combobox.bind("<<ComboboxSelected>>", update_t_label)

t_label = ttk.Label()
t_label.pack(padx=10, pady=10)



Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()
