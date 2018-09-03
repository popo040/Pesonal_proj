

def func_1():

    data1 = open("input_file.txt", "r")
    text = data1.readline().strip('\n')
    print("The text file contains: " + text)
    key = int(data1.readline())
    data1.close()
    data2 = open("output_file.txt", "w")

    def encrypt(text, key):
        result = ""
        for i in range(len(text)):
            char = text[i]
            if char == ' ':
                result += ' '
            elif char == '.':
                result += '.'
            elif char.isupper():
                result += chr((ord(char) + key - 65) % 26 + 65)
            else:
                result += chr((ord(char) + key - 97) % 26 + 97)
        return result
    data2.write(encrypt(text, key))
    print("The output of encryption is: " + encrypt(text, key))


def func_2():

    data1 = open("input_file.txt", "r")
    data1 = open("input_file.txt", "r")
    text = data1.readline().strip('\n')
    key = int(data1.readline())
    data1.close()
    data2 = open("output_file.txt", "r")
    encrypted_text = data2.readline()
    print("The encrypted text is: " + encrypted_text)
    data2.close()

    def decrypt(encrypted_text, key):
        result = ""
        for i in range(len(encrypted_text)):
            char = encrypted_text[i]
            if char == ' ':
                result += ' '
            elif char == '.':
                result += '.'
            elif char.isupper():
                result += chr((ord(char) - key - 65) % 26 + 65)
            else:
                result += chr((ord(char) - key - 97) % 26 + 97)
        return result

    print("The output of decryption is: " + decrypt(encrypted_text, key))


def func_3():

    data = open("output_file.txt", "r")
    encrypted_text = data.readline()

    def Cryptanalysis(encrypted_text, key):
        result = ""
        for i in range(len(encrypted_text)):
            char = encrypted_text[i]
            if char == ' ':
                result += ' '
            elif char == '.':
                result += '.'
            elif char.isupper():
                result += chr((ord(char) - key - 65) % 26 + 65)
            else:
                result += chr((ord(char) - key - 97) % 26 + 97)
        return result

    for i in range(0, 26):
        key = i
        print(Cryptanalysis(encrypted_text, key))


def indirect(i):
    switcher = {
        1: func_1,
        2: func_2,
        3: func_3
        }
    func = switcher.get(i, lambda: "Invalid")
    return func()

ch = int(input("What would you like to do?\n1:Encrypt\n2:Dycryppt\n3:Cryptanalysis\n"))
indirect(ch)
while True:
    co = input("Do you want to continue?\nY:Yes\nN:No\n")
    if co == 'Y':
        ch = int(input("What would you like to do?\n1:Encrypt\n2:Dycryppt\n3:Cryptanalysis\n"))
        indirect(ch)
    elif co == 'N':
        break
    else:
        print("Invalid option")