# a morse coder / decoder

from winsound import Beep
from time import sleep

morse_dict = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
         'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
         'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
         'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
         'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
         '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----',
         ',':'--..--', ':':'---...', ';':'-.-.-.', '/':'-..-.', '@':'.--.-.',
         '!':'-.-.--', '?':'..--..', '=':'-...-', '_':'..--.-', '+':'.-.-.',
         '$':'...-..-', '"':'.-..-.', '(':'-.--.', ')':'-.--.-', '&':'.-...',}

morse_tcid = dict() # this will create an empty dictionary 

def get_message():
    return input("insert your code so we could cipher or decipher it: \n ").upper()  #this will get you the input message.
#    return message

def processus(message): # now, this is the true processus to coding or decoding
    
    transmsg = ""
    transmsgtomorse = ''
    
    if '.' and '-' in message:
        
        for key, value in morse_dict.items(): #    this will select the morse_dict items which happen to be a bench of tuples (key, value)
            morse_tcid[value] = key           #    this will add a set of pairs(key value) to the emty dictionary but we inversed them.
            
        for i in message.split(' '):
            if i in morse_tcid:
                transmsg = transmsg + morse_tcid[i]
            elif i == '':
                transmsg += ' '
        print(transmsg)
        
        return transmsg.lower()
        
    else:
        for i in message:
            if i in morse_dict:
                transmsgtomorse += morse_dict[i] + ' '
            elif i == ' ':
                transmsgtomorse += ' '
        print(transmsgtomorse)
        
        return transmsgtomorse
        
def morse_sound(transmsgtomorse):
    
    for i in transmsgtomorse:
        
        if i == ".":
            Beep(1500, 200)
        elif i == "-":
            Beep(2000, 500)
        else:
            sleep(2/5)

morse_sound(processus(get_message()))