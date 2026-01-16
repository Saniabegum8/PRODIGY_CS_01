def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result


def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - 97 - shift) % 26 + 97)
            else:
                result += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            result += char
    return result


# Main Program
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

print("1. Encrypt")
print("2. Decrypt")

choice = input("Choose an option (1 or 2): ")

if choice == "1":
    print("Encrypted Text:", encrypt(message, shift))
elif choice == "2":
    print("Decrypted Text:", decrypt(message, shift))
else:
    print("Invalid choice")
