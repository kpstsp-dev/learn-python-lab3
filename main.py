# Определяем имя файла
file_name = "questions.txt"

# Первый способ: Использование контекстного менеджера (`with` statement)
print("Метод 1: Использование контекстного менеджера (with statement)")

# Открываем файл с помощью контекстного менеджера
with open(file_name, "r", encoding="utf-8", errors="ignore") as file:
    # Считываем все строки в список
    questions = file.readlines()
    # Убираем символы переноса строки и выводим каждый вопрос
    for question in questions:
        print(question.strip())  # Удаляем лишние символы переноса строки

print("\n" + "=" * 50 + "\n")  # Разделитель для удобства чтения вывода

# Второй способ: Ручное управление файлом (open() и close())
print("Метод 2: Ручное управление файлом (open() и close())")

# Открываем файл вручную
file = open(file_name, "r", encoding="utf-8", errors="ignore")
while True:
    # Считываем одну строку за раз
    line = file.readline()
    if not line:  # Если достигнут конец файла, выходим из цикла
        break
    print(line.strip())  # Удаляем лишние символы переноса строки и выводим строку
# Закрываем файл вручную
file.close()
