# 1
def union_sets(set1, set2):
    """ Функція для об'єднання двох множин """
    # за допомогою методу union об'єднуємо множини
    result_set = set1.union(set2)
    return result_set

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = union_sets(set1, set2)
print("Об'єднана множина:", result)

#2
def is_subset(set1, set2):
    """ Функція для перевірки, чи є перша множина підмножиною другої множини """
    # за допомогою методу issubset перевіряємо чи є перша множина підмножиною другої множини
    return set1.issubset(set2)

set1 = {1, 2}
set2 = {1, 2, 3, 4}
result = is_subset(set1, set2)
print("Чи є set1 підмножиною set2:", result)
