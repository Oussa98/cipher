# Vigenère cipher

def get_message():
    return input("your message \n ") #this will get you the input message.


def get_key(mode):
    if mode == "d":
        return input("insert your decrypting key ,please").lower(), mode
        print("decrypting in process, please wait")

    elif mode == "e":
        return input("insert your encrypting key ,please").lower(), mode
        print("encrypting in process, please wait")
    


def get_mode():
    mode = input("insert the mode").lower()  #this will get you the input message.
    while mode not in 'd decrypte decipher decode e encrypte c cipher code'.split():
        mode = input("you can insert :\n d decrypte decipher decode e encrypte c cipher code").lower()  #this will get you the input message.
        
    if mode in 'd decrypte decipher decode'.split():
        mode = 'd'
        
    elif mode in 'e encrypte c cipher code'.split():
        mode = 'e'

    return mode


def translating(message, key):
    the_key = key[0]
    translatednum = []
    translated = ''
    mode = key[1]
    c = 0
    if mode == 'e':
        for count, char in enumerate(message):
            print(count, char)
            if char.isalpha() and char.isupper():
                translatednum.append(((( ord(char) + ord(the_key[(count - c) % len(the_key)].upper())) - 64 - 65) % 26) + 64)
            elif char.isalpha() and char.islower():
                translatednum.append( (((ord(char) + ord(the_key[(count - c) % len(the_key)].lower())) - 96 - 97) % 26) + 96)
            else:
                translatednum.append(ord(char))
                c += 1
        print(translatednum)
        for order in translatednum:
            translated += chr(order)
        print(translated)


    if mode == 'd':
        for count, char in enumerate(message):
            if char.isalpha() and char.isupper():
                translatednum.append((ord(char) - ord(the_key[(count - c) % len(the_key)].upper()) + 26) % 26 + 65)
            elif char.isalpha() and char.islower():
                translatednum.append((ord(char) - ord(the_key[(count - c) % len(the_key)].lower()) + 26) % 26 + 97)
            else:
                translatednum.append(ord(char))
                c += 1
        print(translatednum)
        for order in translatednum:
            translated += chr(order)
        print(translated)
translating(get_message(), get_key(get_mode()))