import re  # Импорт модуля регулярных выражений
from collections import Counter  # Импорт функции Counter из модуля collections
import heapq  # Импорт модуля heapq для работы с приоритетными очередями

# Открываем файл и читаем его содержимое
with open("sherlock_holmes.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Преобразуем текст в нижний регистр
text = text.lower()

# Получаем уникальные символы
unique_chars = sorted(set(text))  # Уникальные символы в отсортированном порядке

# Выводим уникальные символы
print("Уникальные символы:", unique_chars)

# Считаем частоту каждой буквы
letter_freq = Counter(text)  # Словарь частот каждой буквы

# Создаем список пар букв и считаем их частоту
letter_pairs = [text[i:i+2] for i in range(len(text)-1)]  # Список пар букв
pair_freq = Counter(letter_pairs)  # Словарь частот пар букв

''''# Выводим результаты
print("Частота букв:")
print(letter_freq)
print("\nЧастота пар букв:")
print(pair_freq)'''

# Создаем класс узла для построения дерева Хаффмана
class Node:
    def __init__(self, char, freq):
        self.char = char  # Символ
        self.freq = freq  # Частота
        self.left = None  # Левый потомок
        self.right = None  # Правый потомок

    def __lt__(self, other):
        return self.freq < other.freq  # Сравнение узлов по частоте

# Функция для построения дерева Хаффмана
def build_huffman_tree(freq_dict):
    priority_queue = [Node(char, freq) for char, freq in freq_dict.items()]  # Создание приоритетной очереди из узлов
    heapq.heapify(priority_queue)  # Преобразование списка в мин-кучу

    while len(priority_queue) > 1:  # Пока в очереди больше одного элемента
        left = heapq.heappop(priority_queue)  # Извлекаем узел с наименьшей частотой
        right = heapq.heappop(priority_queue)  # Извлекаем следующий узел с наименьшей частотой

        merged = Node(None, left.freq + right.freq)  # Создаем новый узел, объединяя два наименьших узла
        merged.left = left  # Присваиваем левому потомку нового узла левый узел
        merged.right = right  # Присваиваем правому потомку нового узла правый узел

        heapq.heappush(priority_queue, merged)  # Добавляем новый узел в очередь

    return priority_queue[0]  # Возвращаем корень дерева Хаффмана

# Функция для построения кодов Хаффмана
def build_huffman_codes(root, current_code="", huffman_codes={}):
    if root is None:
        return

    if root.char is not None:
        huffman_codes[root.char] = current_code  # Добавляем код символа в словарь кодов

    build_huffman_codes(root.left, current_code + "0", huffman_codes)  # Рекурсивно вызываем для левого поддерева
    build_huffman_codes(root.right, current_code + "1", huffman_codes)  # Рекурсивно вызываем для правого поддерева

    return huffman_codes  # Возвращаем словарь кодов Хаффмана

# Построение дерева Хаффмана
huffman_tree = build_huffman_tree(letter_freq)

# Построение кодов Хаффмана
huffman_codes = build_huffman_codes(huffman_tree)

# Кодирование текста
encoded_text_huffman = "".join(huffman_codes[char] for char in text)  # Кодируем текст с помощью кодов Хаффмана

# Размер текста в битах
text_size_bits = len(text) * 5  # Предполагаем, что каждый символ кодируется 5 битами

# Размер закодированного текста в битах
encoded_size_huffman_bits = len(encoded_text_huffman)

# Вывод результатов
print("\nКоды Хаффмана:")
for char, code in huffman_codes.items():
    print(f"{char}: {code}")

print("\nКоличество бит закодированного текста с использованием кодов Хаффмана:", encoded_size_huffman_bits)
print("Количество бит исходного текста (равномерные коды):", text_size_bits)

# Функция для кодирования текста с использованием алгоритма LZW
def lzw_encode(text):
    dictionary_size = 256  # Начальный размер словаря
    dictionary = {chr(i): i for i in range(dictionary_size)}  # Инициализация словаря
    result = []  # Результат кодирования
    sequence = ""  # Текущая последовательность

    for char in text:  # Для каждого символа в тексте
        new_sequence = sequence + char  # Создаем новую последовательность
        if new_sequence in dictionary:  # Если последовательность уже есть в словаре
            sequence = new_sequence  # Обновляем текущую последовательность
        else:
            result.append(dictionary[sequence])  # Добавляем код текущей последовательности в результат
            dictionary[new_sequence] = dictionary_size  # Добавляем новую последовательность в словарь
            dictionary_size += 1  # Увеличиваем размер словаря
            sequence = char  # Обновляем текущую последовательность

    if sequence:  # Если последовательность не пустая
        result.append(dictionary[sequence])  # Добавляем код последней последовательности в результат

    return result  # Возвращаем закодированный текст

# Кодирование текста
encoded_text_lzw = lzw_encode(text)

# Размер закодированного текста в битах
encoded_size_lzw_bits = len(encoded_text_lzw) * 5  # Предполагаем, что каждый код символа кодируется 5 битами

# Вывод результатов
print("\nКоличество бит закодированного текста с использованием кодов LZW:", encoded_size_lzw_bits)
