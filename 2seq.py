# Запрашиваем у пользователя ввод чисел через запятую, точку с запятой или слэш
user_input = input("Введите числа через запятую, точку с запятой или слэш: ")

# Заменяем все возможные разделители на запятую
user_input = user_input.replace(';', ',').replace('/', ',')

# Разделяем строку на элементы по запятой и удаляем пробелы
numbers_str = user_input.split(',')
numbers_str = [num.strip() for num in numbers_str]

# Проверяем, что все элементы являются числами и преобразуем их в список чисел
try:
    numbers = [float(num) for num in numbers_str]  # Используем float для поддержки чисел с плавающей запятой
except ValueError:
    print("Неверный формат ввода. Все элементы должны быть числами.")
    exit()

# Создаем новый список с уникальными элементами
unique_numbers = [num for num in numbers if numbers.count(num) == 1]

# Выводим результат
print("Результат:", unique_numbers)
