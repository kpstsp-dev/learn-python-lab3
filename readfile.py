def readfile():
    # Определяем имя файла
    file_name = "questions.txt"

    # Первый способ: Использование контекстного менеджера (`with` statement)
    print("Метод 1: Использование контекстного менеджера (with statement)")

    questions=[]

    # Открываем файл с помощью контекстного менеджера
    with open(file_name, "r", encoding="utf-8", errors="ignore") as file:
        # Считываем все строки в список
        questions = file.readlines()
        # Убираем символы переноса строки и выводим каждый вопрос
        for question in questions:
            print(question.strip())  # Удаляем лишние символы переноса строки

    return questions
