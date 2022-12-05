spisok = input("Введите последовательность чисел через пробел: ")
spisok_list = [int(a) for a in spisok.split()]

try:
    num = int(input("Введите целое число: "))
    if num % 1 == 0:
        spisok_list.append(num)
        print("Список до сортировки: ", spisok_list)
        spisok_list.sort()
        print("Список после сортировки в порядке возрастания: ", spisok_list)
except ValueError:
    print("Не корректные данные.")
    print("Программа завершена!")

def binary_search(spisok_list, num, left, right):
        middle = (right + left) // 2
        if spisok_list[middle] == num:
            return middle
        elif num < spisok_list[middle]:
            return binary_search(spisok_list, num, left, middle - 1)
        else:
            return binary_search(spisok_list, num, middle + 1, right)

print("Индекс введенного числа в списке: ", binary_search(spisok_list, num, 0, len(spisok_list) - 1))