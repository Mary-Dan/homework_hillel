# 1
def dictionary_keys(dictionary):
    """ Функція для виведення всіх ключів словника """
    keys = dictionary.keys()
    print("Ключі словника:")
    # виведення за допомогою циклу ключів
    for key in keys:
        print(key)

my_dict = {"name": "Mary", "age": 26, "country": "Ukraine"}
dictionary_keys(my_dict)

# 2
def merge_dictionaries(dict1, dict2):
    """ Функція для об'єднання двох словників у новий словник """
    # Розпаковуємо словник
    merge_dict = {**dict1, **dict2}
    return merge_dict

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
result_dict = merge_dictionaries(dict1, dict2)
print("Об'єднаний словник:", result_dict)
