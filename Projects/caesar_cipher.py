alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    final_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
          position = alphabet.index(char)
          new_position = position + shift
          final_text += alphabet[new_position]

        else:
            final_text += char #space is a char, this helps insert space

    print(f"Here's the {direction}d result: {final_text}")

end_cipher = False
while not end_cipher:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26

        caesar( text, shift, direction)

        restart = input("Type 'yes' if you want to go again. Otherwise type no.\n")
        if restart == "no":
           end_cipher = True
           print("Goodbye")







