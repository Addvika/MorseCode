"""Morse Code Encryptor"""
"Dictionary for Morse Values"
morse={ 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
"variable to store each letter/value"
letter=""
"variable to store words"
word=""
"variable to display final message"
toDisplay=""
message=input("Enter message:")
if message=="":
    print("No message found.")
    exit()
if message.isspace():
    print("No")
    exit()
message=message.upper()
"iterating through each letter of message"
for i in range(len(message)):
    "checking if space"
    if message[i]!=" ":
        letter=""
        "adding encrypted letter if not space"
        letter+=morse[message[i]]
        "adding space after each letter"
        letter+=" "
        word+=letter
    else:
        "adding letters to word"
        letter=""
        toDisplay+=word
        word=""
        toDisplay+=" "
    if i==len(message)-1:
        toDisplay+=word
    print(i,letter,"letter")
print(toDisplay)
