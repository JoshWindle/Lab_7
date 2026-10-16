alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encrypted_messages = []
encryption_keys = []
current_key_index = 0


def vigenere_sq():
    square = []

    for i in range(26):
        row = []

        for j in range(26):
            index = (i + j) % 26
            row.append(alphabet[index])

        square.append(row)

    print("|   |", end="")
    for letter in alphabet:
        print(f" {letter} |", end="")
    print()
    print("|---|" + "---|" * 26)

    for i in range(26):
        print(f"| {alphabet[i]} |", end="")

        for letter in square[i]:
            print(f" {letter} |", end="")

        print()




def letter_to_index(letter, alphabet):
    return alphabet.index(letter)


def index_to_letter(index, alphabet):
    return alphabet[index]
def vigenere_index(key_letter, plaintext_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    plaintext_index = letter_to_index(plaintext_letter, alphabet)

    cipher_index = (key_index + plaintext_index) % 26

    return index_to_letter(cipher_index, alphabet)


def encrypt_vigenere(key, plaintext, alphabet):
    ciphertext = []
    key_position = 0

    for letter in plaintext:
        if letter in alphabet:
            key_letter = key[key_position % len(key)]

            cipher_letter = vigenere_index(key_letter, letter, alphabet)
            ciphertext.append(cipher_letter)

            key_position += 1
        else:
            ciphertext.append(cipher_letter)

    return "".join(ciphertext)


def undo_vigenere_index(key_letter, cypher_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    cypher_index = letter_to_index(cypher_letter, alphabet)

    plaintext_index = (cypher_index - key_index) % 26

    return index_to_letter(plaintext_index, alphabet)


def decrypt_vignere(key, cipher_text, alphabet):
    plaintext = []
    key_position = 0

    for letter in cipher_text:
        if letter in alphabet:
            key_letter = key[key_position % len(key)]

            plaintext_letter = undo_vigenere_index(key_letter, letter, alphabet)
            plaintext.append(plaintext_letter)

            key_position += 1
        else:
            plaintext.append(letter)

    return "".join(plaintext)

def setup_keys():
    global current_key_index

    encryption_keys.clear()
    current_key_index = 0

    print("Enter your encryption keywords.")
    print("Press Enter without typing anything when finished.")

    while True:
        key = input("Enter a keyword: ").upper()

        if key == "":
            break

        if any(letter not in alphabet for letter in key):
            print("Please use letters only.")
        else:
            encryption_keys.append(key)

    print("Keywords saved:", len(encryption_keys))


def encrypt_message():
    global current_key_index

    if not encryption_keys:
        print("Please set up your keywords first.")
        return

    key = encryption_keys[current_key_index]
    plaintext = input("Enter a message: ").upper()

    encrypted = encrypt_vigenere(key, plaintext, alphabet)
    encrypted_messages.append((key, encrypted))

    print("Keyword used:", key)
    print("Encrypted message:", encrypted)
    print("Message saved!")

    current_key_index = (current_key_index + 1) % len(encryption_keys)

def decrypt_messages():
    if not encrypted_messages:
        print("No encrypted messages to decrypt.")
        return

    for key, encrypted in encrypted_messages:
        decrypted = decrypt_vignere(key, encrypted, alphabet)
        print("Decrypted message:", decrypted)


def dump_encrypted():
    if not encrypted_messages:
        print("No encrypted messages saved.")
        return

    print("Saved encrypted messages:")
    print(encrypted_messages)


def main():
    menu = [
        "1. Encrypt",
        "2. Decrypt",
        "3. Dump Encrypted Text",
        "4. Set Up Encryption Keys",
        "5. Quit"
    ]

    while True:
        print("\nVigenere Cipher Menu")

        for option in menu:
            print(option)

        choice = input("Choose an option: ")

        if choice == "1":
            encrypt_message()

        elif choice == "2":
            decrypt_messages()

        elif choice == "3":
            dump_encrypted()


        elif choice == "4":

            setup_keys()


        elif choice == "5":

            print("Goodbye!")

            break

        else:
            print("Invalid choice. Please try again.")

main()