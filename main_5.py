class SymbolRange:
    def __init__(self, symbol, low, high):
        self.symbol = symbol
        self.low = low
        self.high = high

def compute_cumulative_probabilities(probabilities):
    cumulative_probabilities = [0] * len(probabilities)
    cumulative_probabilities[0] = probabilities[0]
    for i in range(1, len(probabilities)):
        cumulative_probabilities[i] = cumulative_probabilities[i - 1] + probabilities[i]
    return cumulative_probabilities

def arithmetic_encoding(text, probabilities):
    cumulative_probabilities = compute_cumulative_probabilities(probabilities)
    low = 0
    high = 1
    for char in text:
        index = ord(char) - ord('a')
        range_width = high - low
        high = low + range_width * cumulative_probabilities[index]
        low = low + range_width * cumulative_probabilities[index - 1] if index > 0 else 0
    return low

def to_binary_string(number, precision):
    binary_string = ""
    for _ in range(precision):
        number *= 2
        if number >= 1:
            binary_string += "1"
            number -= 1
        else:
            binary_string += "0"
    return binary_string

# Вероятности для каждого символа
probabilities = [0.10, 0.10, 0.05, 0.55, 0.10, 0.10]

# Строка для кодирования
text = "aecdfb"

# Выполняем арифметическое кодирование
encoded_value = arithmetic_encoding(text, probabilities)

# Переводим число в двоичную строку с точностью до 32 бит
binary_string = to_binary_string(encoded_value, 32)

print("Encoded value:", binary_string)
