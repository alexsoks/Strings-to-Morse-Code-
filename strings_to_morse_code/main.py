#This python project will convert Strings into morse code

#dictionary with characters & corresponding morsen code
morse_dict = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': ' ',
}


#function that processes the text, referring to the dictionary to convert to morse code
def converter(t):
    #list that will be appended with each character conversion
    morse_list = []

    for char in t:
        morse_equiv = morse_dict[char.lower()]
        morse_list.append(morse_equiv)

    result = "".join(morse_list)

    return result

cycle = True

while cycle == True:
    #prompt to type text
    text = input("Please enter text to be converted to morse code \n")
    print(converter(text))

    options = True
    while options == True:
        ans = input("Would you like to convert more text?\nenter y or n\n")
        if ans in ["yes", "Yes", "y"]:
            options = False
        elif ans in ["no", "No", "n"]:
            cycle = False
            options = False
            print("bye!")

        else:
            cycle = True
            print("sorry that is not an option. Try again!")

