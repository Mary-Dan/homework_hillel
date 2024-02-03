# 1
def number_squared(input_int):
    """ Функція, яка приймає число і повертає його квадрат """
    # Обчислюємо квадрат числа
    result = input_int ** 2
    print(f"Квадрат числа {input_int} дорівнює {result}")

number = int(input("Введіть число:"))
number_squared(number)

# 2
def sum_num(int1, int2):
    """ Функція, яка приймає два числа і повертає їхню суму """
    # обчислюємо суму чисел
    return int1 + int2

int1 = int(input("Введіть число: "))
int2 = int(input("Введіть число: "))

result = sum_num(int1, int2)
print(result)

# 3
def divide_num(int1, int2):
    """ Функція яка приймає 2 числа типу int, виконує операцію ділення """
    # обчислюємо чілу частину і залишок числа
    num_1 = int1 // int2
    num_2 = int1 % int2
    return num_1, num_2

num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

result_num_1, result_num_2 = divide_num(num1, num2)

print(f"Частка: {result_num_1}")
print(f"Залишок: {result_num_2}")