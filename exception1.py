"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
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
        try:      
            command = input("Задайте вопрос: ")
            ask_user_dict(command)          
        except KeyboardInterrupt:
            print("\nBye!")
            break

    
if __name__ == "__main__":
    ask_user()
