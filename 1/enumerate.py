def my_enumerate(iterable, start=1):
    """
    Власна реалізація функції enumerate().

    Параметри:
    - iterable: будь-який ітерабельний об'єкт (список, рядок, кортеж тощо).
    - start: початкове значення індексу (за замовчуванням 1).

    Повертає:
    - Ітератор кортежів (index, element).
    """
    index = start
    for element in iterable:
        yield index, element
        index += 1


# Приклад 1: Список фруктів
fruits_list = ['apple', 'banana', 'cherry']
for index, fruit in my_enumerate(fruits_list):
    print(f"{index}: {fruit}")
print()  # Порожній рядок для відокремлення результатів

# Приклад 2: Список тварин з початковим індексом
animals_list = ['cat', 'dog', 'parrot']
for index, animal in my_enumerate(animals_list, start=1):
    print(f"{index}: {animal}")
print()

# Приклад 3: Рядок
text = "Hello"
for index, char in my_enumerate(text):
    print(f"Character '{char}' is at index {index}")
print()
