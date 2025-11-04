alphabet2numbers = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
    'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15,
    'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23,
    'y': 24, 'z': 25,
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
    'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15,    
    'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
    'Y': 24, 'Z': 25
}
numbers2alphabet = {v: k for k, v in alphabet2numbers.items()}
def cezar_encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char in alphabet2numbers:
            original_position = alphabet2numbers[char]
            new_position = (original_position + shift) % 26
            encrypted_char = numbers2alphabet[new_position]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetic characters are unchanged
    return encrypted_text
def cezar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char in alphabet2numbers:
            encrypted_position = alphabet2numbers[char]
            original_position = (encrypted_position - shift) % 26
            decrypted_char = numbers2alphabet[original_position]
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  # Non-alphabetic characters are unchanged
    return decrypted_text
if __name__ == "__main__":
    sample_text = "HelloWorld"
    shift_value = 3
    encrypted = cezar_encrypt(sample_text, shift_value)
    print(f"Encrypted: {encrypted}")
    decrypted = cezar_decrypt(encrypted, shift_value)
    print(f"Decrypted: {decrypted}")