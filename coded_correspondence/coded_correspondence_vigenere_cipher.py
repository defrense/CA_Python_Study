alphabet='abcdefghijklmnopqrstuvwxyz'

def decode_message(message, keyword):
    message_decode =''
    for i in range(len(message)):

        letter_lo = alphabet.find(message[i])
        if letter_lo >= 0:
            letter_keyword_lo = alphabet.find(keyword[i % len(keyword)])
            offset = (letter_lo - letter_keyword_lo) % 26
            decode_letter = alphabet[offset]
            message_decode += decode_letter
        else:
            message_decode += message[i]
    return message_decode


def coded_message(message, keyword):
    message_code = ''
    for i in range(len(message)):
        letter_lo = alphabet.find(message[i])
        if letter_lo >= 0:
            letter_keyword_lo = alphabet.find(keyword[i % len(keyword)])
            offset = (letter_lo + letter_keyword_lo) % 26
            coded_letter = alphabet[offset]
            message_code += coded_letter
        else:
            message_code += message[i]
    return message_code


def decypher_message():
    cipher_message = input('Please paste the cipher message here: ')
    keyword = input('Please give me the keyword: ')
    decipher_message = decode_message(cipher_message, keyword)
    print('The decoded message is as below: ')
    print(decipher_message)


def encypto_message():
    original_message = input('Please enter your message here: ')
    keyword = input('Please give me the keyword: ')
    encrypted_message = coded_message(original_message, keyword)
    print('The encypted message is as below: ')
    print(encrypted_message)

print('Welcome using the Vigenere Cipher coder/decoder !')
Choice = ''
choice = input ('Please choose one of below functions: \nA: Decode a message.\nB: Code a message\n:').upper()

if choice == 'A':
    decypher_message()
elif choice == 'B':
    encypto_message()
else:
    print ('Invalid choice!')
