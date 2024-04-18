def hamming_distance(str1, str2):
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))

# Двоичные коды для символов
codes = {
    "и": "000",
    "к": "001",
    "л": "010",
    "м": "011",
    "н": "100",
    "о": "101",
    "п": "110",
    "р": "111"
}

# Добавляем ошибку в один из кодов
error_code = "111"  # Это код для "р", изменим его, чтобы создать ошибку
error_code = "110"  # Измененный код будет "п"
error_code_index = 6  # Индекс измененного бита
error_position = "п"
original_code = codes[error_position]

print("Original:", original_code)
print("Error introduced:", error_code)

# Находим код с наименьшим расстоянием
min_distance = float('inf')
closest_symbol = None
for symbol, code in codes.items():
    distance = hamming_distance(code, error_code)
    if distance < min_distance:
        min_distance = distance
        closest_symbol = symbol

print("Closest symbol found:", closest_symbol)

'''

def hamming_distance(str1, str2):
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))

# Двоичные коды для символов с расстоянием менее 2
codes = {
    "и": "00",
    "к": "01",
    "л": "10",
    "м": "01",  # Один бит отличается от "к"
    "н": "11",
    "о": "10",  # Один бит отличается от "л"
    "п": "11",  # Один бит отличается от "н"
    "р": "00"   # Один бит отличается от "и"
}

# Добавляем ошибку в один из кодов
error_code = "01"  # Это код для "к", изменим его, чтобы создать ошибку
error_code = "11"  # Измененный код будет "н"
error_position = "н"
original_code = codes[error_position]

print("Original:", original_code)
print("Error introduced:", error_code)

# Находим код с наименьшим расстоянием
min_distance = float('inf')
closest_symbol = None
for symbol, code in codes.items():
    distance = hamming_distance(code, error_code)
    if distance < min_distance:
        min_distance = distance
        closest_symbol = symbol

print("Closest symbol found:", closest_symbol)
'''