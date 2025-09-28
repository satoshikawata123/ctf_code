def caesar_decrypt_shift3(ciphertext: str) -> str:
    result = []
    for ch in ciphertext:
        if 'A' <= ch <= 'Z':
            new_ord = (ord(ch) - ord('A') - 3) % 26 + ord('A')
            result.append(chr(new_ord))
        elif 'a' <= ch <= 'z':
            new_ord = (ord(ch) - ord('a') - 3) % 26 + ord('a')
            result.append(chr(new_ord))
        else:
            result.append(ch)
    return ''.join(result)

if __name__ == "__main__":
    encrypted = input()
    print(caesar_decrypt_shift3(encrypted))
