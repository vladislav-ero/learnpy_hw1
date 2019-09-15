"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def CompareStrings(first_string, second_string):
    # first_string = strings[0]
    # second_string = strings[1]
    if not type(first_string) == str or not type(second_string) == str:
        return 0
    if first_string == second_string:
        return 1
    if not first_string == second_string and len(first_string) > len(second_string):
        return 2
    if not first_string == second_string and second_string == "learn":
        return 3

def main():
    
    print(CompareStrings(2, 39)) # 0
    print(CompareStrings("strk", "strk")) # 1
    print(CompareStrings("strk", "str")) # 2
    print(CompareStrings("sssss", "learn")) # 3

    
if __name__ == "__main__":
    main()
