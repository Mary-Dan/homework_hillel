# 1
def length_str(input_str):
    """ Функція для визначення довжини рядка """

    # Визначаємо довжину рядка
    length = len(input_str)
    print(f"Довжина рядка: {length}")

str_1 = input("Введіть рядок: ")
length_str(str_1)


# 2
def concatenate_str(string1, string2):
    """ Функція, яка конкатенує два рядки і повертає результат """
    return string1 + string2

# Запитуємо користувача ввести два рядки
str1 = input("Введіть перший рядок: ")
str2 = input("Введіть другий рядок: ")

result = concatenate_str(str1, str2)
print(result)


