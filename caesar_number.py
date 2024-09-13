import string


# @TODO: Create a function that print % of each character in sentence


def print_percentage(sentence: str):
    sentence = list(sentence)
    letters = []
    punctuation = []
    whitespace = []

    for character in sentence:
        if character in string.ascii_letters:
            if character in letters:
                continue
            else:
                letters.append(character)
            print(character, string.ascii_letters.count(character) / len(sentence) * 100, "%")
        elif character in string.punctuation:
            if character in punctuation:
                continue
            else:
                punctuation.append(character)
            print(character, string.punctuation.count(character) / len(sentence) * 100, "%")
        elif character == " ":
            whitespace.append(character)
            print(character, string.whitespace.count(character) / len(sentence) * 100, "%")
    print("Done")


def decrypt_sentence(sentence: str, key: int):
    sentence_decrypted = []
    sentence.lower()
    sentence = list(sentence)
    for character in sentence:
        if character in string.ascii_letters:
            character = string.ascii_letters[(string.ascii_letters.index(character) + key + 1) % 26]
            sentence_decrypted.append(character)
        elif character in string.punctuation:
            sentence_decrypted.append(character)
        elif character == " ":
            sentence_decrypted.append(character)
    sentence_decrypted = ''.join(str(e) for e in sentence_decrypted)
    print(sentence_decrypted)


def encrypt_sentence(sentence: str, key: int):
    sentence_encrypted = []
    sentence.lower()
    sentence = list(sentence)
    for character in sentence:
        if character in string.ascii_letters:
            character = string.ascii_letters[(string.ascii_letters.index(character) - key - 1) % 26]
            sentence_encrypted.append(character)
        elif character in string.punctuation:
            sentence_encrypted.append(character)
        elif character == " ":
            sentence_encrypted.append(character)
    sentence_encrypted = ''.join(str(e) for e in sentence_encrypted)
    print(sentence_encrypted)
