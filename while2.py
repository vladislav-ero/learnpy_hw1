"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

def ask_user_dict(command):
    command_dict = {
        "Как дела?" : "Хорошо!",
        "Что делаешь?" : "Программирую",
        "Как погода?" : "Сойдет"
    }
    
    if command in command_dict:
        print(command_dict[command])
        

def ask_user():
    command = ""
    while not command == "EXIT":
        command = input("Задайте вопрос: ")
        ask_user_dict(command)
    print("Application is closing")
    
    
if __name__ == "__main__":
    ask_user()
