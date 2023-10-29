python
import tkinter as tk

# создаем главное окно
root = tk.Tk()
root.title("Слова")

# задаем фон главного окна
root.configure(bg="red")

# создаем вкладки
tab_control = tk.Notebook(root)

# вкладка "слова, которые употребляются всеми"
tab1 = tk.Frame(tab_control, bg="white")
tab_control.add(tab1, text="Слова для всех")

# добавляем текст на вкладку 1
label1 = tk.Label(tab1, text="Привет, это вкладка со словами, которые употребляются всеми", font=("Arial", 14))
label1.pack(pady=20)

# вкладка "слова употребляемые геймерами"
tab2 = tk.Frame(tab_control, bg="white")
tab_control.add(tab2, text="Слова для геймеров")

# добавляем текст на вкладку 2
label2 = tk.Label(tab2, text="Привет, это вкладка со словами, которые употребляются геймерами", font=("Arial", 14))
label2.pack(pady=20)

# добавляем вкладки на главное окно
tab_control.pack(expand=1, fill="both")

# запускаем главный цикл
root.mainloop()






