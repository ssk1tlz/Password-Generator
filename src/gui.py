import tkinter as tk
from tkinter import messagebox
from main import generate_password, send_password_via_email  # Импортируем функцию отправки email

def generate():
    length = int(length_entry.get())
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()
    
    password = generate_password(length, use_uppercase, use_digits, use_special)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Скопировано", "Пароль скопирован в буфер обмена.")

def send_email():
    email = email_entry.get()
    password = password_entry.get()
    if email and password:
        send_password_via_email(email, password)
        messagebox.showinfo("Успех", "Пароль отправлен на вашу почту.")
    else:
        messagebox.showwarning("Ошибка", "Убедитесь, что введен адрес электронной почты и сгенерирован пароль.")

# Основное окно
root = tk.Tk()
root.title("Генератор паролей")

# Настройки длины пароля
tk.Label(root, text="Длина пароля:").grid(row=0, column=0, padx=5, pady=5)
length_entry = tk.Entry(root)
length_entry.insert(0, "12")
length_entry.grid(row=0, column=1, padx=5, pady=5)

# Чекбоксы для настроек символов
uppercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Заглавные буквы", variable=uppercase_var).grid(row=1, column=0, columnspan=2, padx=5, pady=5)
tk.Checkbutton(root, text="Цифры", variable=digits_var).grid(row=2, column=0, columnspan=2, padx=5, pady=5)
tk.Checkbutton(root, text="Специальные символы", variable=special_var).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Кнопка для генерации пароля
generate_button = tk.Button(root, text="Сгенерировать", command=generate)
generate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Поле для отображения пароля
password_entry = tk.Entry(root, width=30)
password_entry.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Кнопка для копирования пароля в буфер обмена
copy_button = tk.Button(root, text="Копировать", command=copy_to_clipboard)
copy_button.grid(row=6, column=0, columnspan=2, pady=5)

# Поле для ввода электронной почты
tk.Label(root, text="Email:").grid(row=7, column=0, padx=5, pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=7, column=1, padx=5, pady=5)

# Кнопка для отправки пароля на почту
email_button = tk.Button(root, text="Отправить на почту", command=send_email)
email_button.grid(row=8, column=0, columnspan=2, pady=5)

root.mainloop()
