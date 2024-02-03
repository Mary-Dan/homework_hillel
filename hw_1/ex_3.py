# 1
def cal_average(num):
    """ Функція для обчислення середнього значення списку чисел """
    # Повертаємо 0, якщо список порожній
    if not num:
        return 0
    total = sum(num)
    # Обчислення середнього значення
    average = total / len(num)
    return average

num = [1, 2, 3, 4, 5]
average = cal_average(num)
print(f"Середнє значення: {average}")

# 2
def com_element(list1, list2):
    """ Функція для знаходження спільних елементів двох списків та виводу їх """
    find_element = [element for element in list1 if element in list2]
    print(f"Спільні елементи: {find_element}")
    return find_element

# Приклад використання функції
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
find_element = com_element(list1, list2)
