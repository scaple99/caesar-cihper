alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift_amount, choice):
    choice = input("Choose what you want to do: encode or decode?: ")
    text = input("Enter your text: ")
    shift_amount = input("Enter the key: ")
    if choice is not "decode" or "encode":
        print("Invalid Choice.")
    plain_text=""
    if choice == "decode":
        shift_amount*= -1
    for letter in text:
        letter_position=alphabet.index(letter)
        new_position = letter_position + shift_amount
        letter = alphabet[new_position]
        plain_text+=letter
        print(f"Your {choice}d message is {plain_text}")
    
    
caesar(text=message, shift_amount=key,choice=direction)
