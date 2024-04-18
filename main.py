def string_to_binary(string):
    binary = ''.join(format(ord(char), '08b') for char in string)
    return binary

def add_parity_bits(data):
    n = len(data)
    m = 0
    while 2**m < n + m + 1:
        m += 1
    coded_data = list(data) + ['0'] * m
    for i in range(m):
        position = 2**i - 1
        parity = 0
        for j in range(position, n + m, 2 * (position + 1)):
            parity ^= int(coded_data[j])
        coded_data[position] = str(parity)
    return ''.join(coded_data)

def add_errors(data, error_positions):
    data_list = list(data)
    for pos in error_positions:
        if pos < len(data_list):
            data_list[pos] = '0' if data_list[pos] == '1' else '1'
    return ''.join(data_list)

def extract_data(coded_data):
    m = 0
    while 2**m < len(coded_data) + 1:
        m += 1
    data = list(coded_data)
    error_positions = []
    for i in range(m):
        position = 2**i - 1
        parity = 0
        for j in range(position, len(coded_data), 2 * (position + 1)):
            parity ^= int(coded_data[j])
        if parity != 0:
            error_positions.append(position)
    if error_positions:
        print("Errors detected at positions:", error_positions)
    else:
        print("No errors detected.")
    return ''.join([data[i] for i in range(len(data)) if i not in error_positions])


input_string = "Pentium"
binary_data = string_to_binary(input_string)
print("Original binary data:", binary_data)

# Разбиваем на два блока по 32 бита
block_size = 32
block1 = binary_data[:block_size]
block2 = binary_data[block_size:block_size*2]
print("Block 1:", block1)
print("Block 2:", block2)

# Добавляем контрольные биты
coded_block1 = add_parity_bits(block1)
coded_block2 = add_parity_bits(block2)
print("Coded block 1:", coded_block1)
print("Coded block 2:", coded_block2)

# Имитируем ошибки
error_positions_block1 = [5]
error_positions_block2 = [21]
corrupted_block1 = add_errors(coded_block1, error_positions_block1)
corrupted_block2 = add_errors(coded_block2, error_positions_block2)
print("Corrupted block 1:", corrupted_block1)
print("Corrupted block 2:", corrupted_block2)

# Восстановление исходной информации
recovered_block1 = extract_data(corrupted_block1)
recovered_block2 = extract_data(corrupted_block2)
print("Recovered block 1:", recovered_block1)
print("Recovered block 2:", recovered_block2)

# Объединяем блоки и переводим обратно в строку
recovered_data = recovered_block1 + recovered_block2
print("Recovered binary data:", recovered_data)
