def caesar_cipher(text, rotation):
    result = ""
    for char in text:
        if char.isalpha():
            # Shift character within A-Z
            shifted = chr(((ord(char.upper()) - 65 + rotation) % 26) + 65)
            result += shifted
        else:
            result += char
    return result

def run_length_encode(text):
    encoded = ""
    i = 0
    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
            i += 1
        encoded += text[i]
        if count > 1:
            encoded += str(count)
        i += 1
    return encoded

def special_cipher(text, rotation):
    shifted = caesar_cipher(text, rotation)
    return run_length_encode(shifted)

# Example
if __name__ == "__main__":
    sample = "AABCCC"
    rotation = 3
    print("Original:", sample)
    print("Encrypted:", special_cipher(sample, rotation))  # Should print: D2EF3
