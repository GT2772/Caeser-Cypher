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
  print(f"your {direction}d data is {encoded_string}")



cypher(text,shift)
