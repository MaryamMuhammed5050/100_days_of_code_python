def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char.isalpha():
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}\n")

  run = True
while run:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  # This cleanly handles numbers larger than 26 by finding the remainder
  if shift > 26:
    shift = shift % 26

  # This calls the function and passes the inputs you typed above
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  
  choice = input("Do you want to run this program again?\nType 'yes' or 'no': ")
  if choice == 'no':
    run = False
    print("Goodbye.")

