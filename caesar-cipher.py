alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypt(message, key):
    code =  ""
    for letter in message:
        letter_index=alphabet.index(letter)
        letter_index+=key
        letter=alphabet[letter_index]
        code+=letter
        
    print(f"Your encrypted message is {code}, the receiptient must use {key} to decrypt it")

def decrypt(message, key):
    code=""
    for letter in message:
         letter_index=alphabet.index(letter)
         letter_index-=key
         letter = alphabet[letter_index]
         code+=letter
    print(f"your hidden message is {code}")


    

choice = input("Type encode to create a message or decode to decrypt a message: ")
if choice == "encode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text,shift)

elif choice == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decrypt(text,shift)
else:
    print("Error: Invalid Choice")