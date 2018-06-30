alphabet='abcdefghijklmnopqrstuvwxyz'

def decode_letter(letter, offset):
    cipher = alphabet.find(letter)
    correct_location = (cipher + offset) % len(alphabet)
    return alphabet[correct_location]

def code_letter(letter, offset):
    location = alphabet.find(letter)
    cipher = location - offset
    return alphabet[cipher]

def decode_message(message, offset):
    message_list = message.split()
    messageN = []
    for word in message_list:
        wordN = ''
        for letter in word:
            if alphabet.find(letter) >= 0:
                letterN = decode_letter(letter, offset)
                wordN = wordN + letterN
            else:
                wordN = wordN + letter
        messageN.append(wordN)
    message_result = ' '.join(messageN)
    return message_result

def coded_message(message, offset):
    message_list = message.split()
    messageN = []
    for word in message_list:
        wordN = ''
        for letter in word:
            if alphabet.find(letter) >= 0:
                letterN = code_letter(letter, offset)
                wordN = wordN + letterN
            else:
                wordN = wordN + letter
        messageN.append(wordN)
    message_result = ' '.join(messageN)
    return message_result

#cipher_message = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'
def decypher_message():
    cipher_message = input('Please paste the cipher message here: ')
    offset = int(input('Please give me the offset: '))
    decipher_message = decode_message(cipher_message, offset)
    print('The decoded message is as below: ')
    print(decipher_message)

def encypto_message():
    original_message = input('Please enter your message here: ')
    offset = int(input('Please give me the offset: '))
    encrypted_message = coded_message(original_message, offset)
    print('The encypted message is as below: ')
    print(encrypted_message)

print('Welcome using the Caesar coder/decoder !')
Choice = ''
choice = input ('Please choose one of below functions: \nA: Decode a message.\nB: Code a message\n:').upper()

if choice == 'A':
    decypher_message()
elif choice == 'B':
    encypto_message()
else:
    print ('Invalid choice!')
