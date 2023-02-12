alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "decode":
  shift = -shift

def cypher(text,shift):
  encoded_string = ''
  for char in text: 
    encoded_char = chr(ord(char) + shift)
    encoded_string += encoded_char
  print(f"your {direction}d is {encoded_string}")



cypher(text,shift)

