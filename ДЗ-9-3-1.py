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
    code = b1_combobox.get()
    name = cur[code]
    b1_label.config(text=name)


def exchange():
    t_code = t_combobox.get()
    b_code = b1_combobox.get()

    if t_code and b_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{b_code}')
            response.raise_for_status()
            data=response.json()
            if t_code in data['rates']:
                exchange_rate = data['rates'][t_code]
                t_name=cur[t_code]
                b_name = cur[b_code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {t_name} за один {b_name}")
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
window.geometry("360x300")

Label(text="Базовая валюта").pack(padx=10, pady=10)
b1_combobox = ttk.Combobox(values=list(cur.keys()))
b1_combobox.pack(padx=10, pady=10)
b1_combobox.bind("<<ComboboxSelected>>", update_b1_label)

b1_label = ttk.Label()
b1_label.pack(padx=10, pady=10)

Label(text="Целевая валюта").pack(padx=10, pady=10)
t_combobox = ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(padx=10, pady=10)
t_combobox.bind("<<ComboboxSelected>>", update_t_label)

t_label = ttk.Label()
t_label.pack(padx=10, pady=10)



Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()
