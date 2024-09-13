def decimal_to_binary(n):
    steps = []
    if n == 0:
        steps.append("0 en binaire est 0")
        return '0', steps
    binary = ''
    original_n = n
    while n > 0:
        quotient = n // 2
        remainder = n % 2
        steps.append(f"{n:3} ÷  2 = {quotient:3} avec un reste de {remainder}")
        binary = str(remainder) + binary
        n = quotient
    steps.append(f"Le nombre binaire est {binary}")
    return binary, steps[::-1]  

def decimal_to_hexadecimal(n):
    steps = []
    hex_chars = '0123456789ABCDEF'
    if n == 0:
        steps.append("0 en hexadécimal est 0")
        return '0', steps
    hexadecimal = ''
    original_n = n
    while n > 0:
        quotient = n // 16
        remainder = n % 16
        hex_digit = hex_chars[remainder]
        steps.append(f"{n:3} ÷ 16 = {quotient:3} avec un reste de {remainder:2} ({hex_digit})")
        hexadecimal = hex_digit + hexadecimal
        n = quotient
    steps.append(f"Le nombre hexadécimal est {hexadecimal}")
    return hexadecimal, steps[::-1]  

def char_to_codes(char):
    ascii_code = ord(char)
    print("\n" + "=" * 50)
    print(f"Caractère                : '{char}'")
    print(f"Code ASCII décimal       : {ascii_code}")
    print("=" * 50)
    binary, binary_steps = decimal_to_binary(ascii_code)
    print("\nConversion en binaire :")
    for step in binary_steps:
        print(step)
    print(f"\nReprésentation binaire sur 8 bits : {binary.zfill(8)}")
    hexadecimal, hex_steps = decimal_to_hexadecimal(ascii_code)
    print("\nConversion en hexadécimal :")
    for step in hex_steps:
        print(step)
    print(f"\nReprésentation hexadécimale sur 2 chiffres : {hexadecimal.zfill(2)}")

def word_to_codes(word):
    for char in word:
        char_to_codes(char)

def main():
    print("=== Convertisseur Binaire et Hexadécimal ===")
    word = input("Entrez un mot ou une lettre : ")
    if not word:
        print("Vous n'avez rien entré. Veuillez réessayer.")
        return
    word_to_codes(word)

if __name__ == "__main__":
    main()
