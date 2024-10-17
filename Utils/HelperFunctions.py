def CharNaBit(char):
    # Step 1: Get the ASCII value of the character
    ascii_value = ord(char)

    # Step 2: Convert the ASCII value to a binary string
    # The [2:] slices off the '0b' prefix from the binary string
    binary_string = bin(ascii_value)[2:]

    # Step 3: Pad the binary string with leading zeros to make it 8 bits long
    padded_binary_string = binary_string.zfill(8)

    # Step 4: Convert the padded binary string to a list of bits
    bits_array = [int(bit) for bit in padded_binary_string]

    return bits_array

def SlowoNaTablice(slowo):
    slowotemp = []
    for litera in slowo:
        slowotemp.append(CharNaBit(litera))
    return slowotemp



def split_array_of_8_to_4(bits_array):
    # Check if the input array has exactly 8 bits
    if len(bits_array) != 8:
        raise ValueError("Input array must have exactly 8 bits.")

    # Split the array into two arrays of 4 bits each
    first_half = bits_array[:4]  # First 4 bits
    second_half = bits_array[4:]  # Last 4 bits

    return first_half, second_half

# Łączy dwie tablice 4-bitowe w jedną tablicę 8-bitową
def join_4_bit_arrays(array1, array2):
    return array1 + array2  # Łączymy tablice w jedną

# Zamienia tablicę bitów na znak
def bits_to_char(bits):
    byte_str = ''.join(str(bit) for bit in bits)  # Konwertuje tablicę bitów na string
    return chr(int(byte_str, 2))  # Konwertuje string binarny na znak

"""
Jeżeli mamy tak jak niżej słowo hej (przykładowe, te tablice nie oznaczają hej)
[0,1,1,1,0,0,0,1],[0,0,0,0,1,1,1,1],[0,0,1,1,0,0,1,1]
to funkcja rozbija je na mniejsze arraye czyli
[0,1,1,1],[0,0,0,1],[0,0,0,0],[1,1,1,1],[0,0,1,1],[0,0,1,1]
"""
def RozbijSlowoNa4BitoweArraye(slowo):
    listabit = []
    for l in slowo:
        tablica = CharNaBit(l)
        firsthalf,secondhalf = split_array_of_8_to_4(tablica)
        listabit.append(firsthalf)
        listabit.append(secondhalf)
    return listabit

# Funkcja do łączenia 4-bitowych tablic z powrotem w słowo
"""
zamienia array typu
[0,1,1,1],[0,0,0,1],[0,0,0,0],[1,1,1,1],[0,0,1,1],[0,0,1,1]
{                 } {                  }{                 }
         H                     E                 J
w słowo (przykładowe te tablice w ascii nie oznaczają słowa hej
"""
def Zlacz4BitoweArrayeNaSlowo(array):
    if len(array) % 2 != 0:
        raise ValueError("Tablica musi mieć parzystą liczbę elementów")

    slowo = ""
    for i in range(0, len(array), 2):
        array1 = array[i]
        array2 = array[i + 1]
        polaczona_tablica = join_4_bit_arrays(array1, array2)
        znak = bits_to_char(polaczona_tablica)
        slowo += znak
    return slowo

"""
ZŁaczy 8 bitowe array w slowo np
[0,1,1,1,0,0,0,1],[0,0,0,0,1,1,1,1],[0,0,1,1,0,0,1,1] zamienia na hej
DANE ZMYSLILEM TAK NAPRAWDE TE 3 TABLICE NIE OZNACZAJĄ HEJ W ASCII
"""
def Zlacz8BitoweArrayeNaSlowo(array):
    tablicachar = []

    for subarray in array:
        result = 0
        for bit in subarray:
            result = (result << 1) | bit  # Przesunięcie bitowe i dodanie bitu
        char = chr(result)  # Zamiana liczby na znak
        tablicachar.append(char)

    slowo = ''.join(tablicachar)  # Łączenie znaków w słowo
    return slowo





