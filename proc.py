#Функции. Обьявление и обращение к функции. Документирование
def my_func():
    '''
    This is my comment
    :return:
    '''
    print("Hi!")

i=0
while i<10:
    my_func()

    i=i+1

print(my_func.__doc__)
