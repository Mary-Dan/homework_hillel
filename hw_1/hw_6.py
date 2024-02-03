# 1
def check_number(number):
    """ Функція для перевірки парності числа та виведення результату """
    # за допомогою циклу число ділимо на 2
    if number % 2 == 0:
        print("Парне")
    else:
        print("Непарне")

number = int(input("Введіть число: "))
check_number(number)

# 2
def even_numbers(numbers):
    """ Функція для знаходження парних чисел у списку та повернення нового списку """
    even_numbers = [number for number in numbers if number % 2 == 0]
    return even_numbers


numbers = [1, 2, 3, 4, 5, 6]
result = even_numbers(numbers)
print("Парні числа:", result)
