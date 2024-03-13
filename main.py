print('''
 
 /$$      /$$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$$        /$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$$$
| $$$    /$$$ /$$__  $$| $$__  $$ /$$__  $$| $$_____/       /$$__  $$ /$$__  $$| $$__  $$| $$_____/
| $$$$  /$$$$| $$  \ $$| $$  \ $$| $$  \__/| $$            | $$  \__/| $$  \ $$| $$  \ $$| $$      
| $$ $$/$$ $$| $$  | $$| $$$$$$$/|  $$$$$$ | $$$$$         | $$      | $$  | $$| $$  | $$| $$$$$   
| $$  $$$| $$| $$  | $$| $$__  $$ \____  $$| $$__/         | $$      | $$  | $$| $$  | $$| $$__/   
| $$\  $ | $$| $$  | $$| $$  \ $$ /$$  \ $$| $$            | $$    $$| $$  | $$| $$  | $$| $$      
| $$ \/  | $$|  $$$$$$/| $$  | $$|  $$$$$$/| $$$$$$$$      |  $$$$$$/|  $$$$$$/| $$$$$$$/| $$$$$$$$
|__/     |__/ \______/ |__/  |__/ \______/ |________/       \______/  \______/ |_______/ |________/ ''' )



alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']


while True:
    response = input("Text Input \n" ).upper()
    if response == '1111':
        print('exiting morse code app')
        break

    words = response.split()


    for word in words:
        if not all(char in alphabets for char in word): # It iterates over each character in word, and for each character, it checks if it is present in the alphabets list.
            print("Please use only alphabets .")
            continue

        morse_code_word = ' '.join(code[alphabets.index(letter)] for letter in word)
        print(morse_code_word)



