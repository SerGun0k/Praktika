import heapq
from collections import defaultdict

class Node:
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(frequencies):
    pq = [Node(symbol, freq) for symbol, freq in frequencies.items()]
    heapq.heapify(pq)
    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        parent = Node(frequency=left.frequency + right.frequency)
        parent.left = left
        parent.right = right
        heapq.heappush(pq, parent)
    return pq[0]

def build_huffman_codes(root, prefix="", codes={}):
    if root is not None:
        if root.symbol is not None:
            codes[root.symbol] = prefix
        build_huffman_codes(root.left, prefix + "0", codes)
        build_huffman_codes(root.right, prefix + "1", codes)
    return codes

def huffman_encoding(text, codes):
    encoded_text = ''.join(codes[char] for char in text)
    return encoded_text

def huffman_decoding(encoded_text, root):
    decoded_text = ""
    current_node = root
    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.symbol is not None:
            decoded_text += current_node.symbol
            current_node = root
    return decoded_text

# Подсчитываем частоты символов
frequencies = {'A': 3, 'B': 10, 'C': 12, 'D': 14, 'E': 16, 'F': 19, 'G': 26}

# Строим дерево Хаффмана
huffman_tree_root = build_huffman_tree(frequencies)

# Получаем коды символов
huffman_codes = build_huffman_codes(huffman_tree_root)

# Выводим коды символов
print("Huffman codes:")
for symbol, code in huffman_codes.items():
    print(f"{symbol}: {code}")

# Пример кодирования и декодирования
text_to_encode = "BEEFG"
encoded_text = huffman_encoding(text_to_encode, huffman_codes)
print("\nEncoded text:", encoded_text)
decoded_text = huffman_decoding(encoded_text, huffman_tree_root)
print("Decoded text:", decoded_text)
