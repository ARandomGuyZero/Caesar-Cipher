"""
Caesar Cipher

Author: Alan
Date: August 25th 2024

This script implements the Caesar cipher, a type of substitution cipher where each letter in the plaintext 
is shifted by a certain number of places down or up the alphabet. Users can choose to encode or decode 
a message by specifying the shift amount. The script will continue running until the user decides to stop.
"""

# Adds art for the Caesar cipher project
print(art.logo)

# Define the alphabet used in the Caesar cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    """
    Apply the Caesar cipher to the original_text.

    Parameters:
    original_text (str): The text to encode or decode.
    shift_amount (int): The number of positions to shift each letter in the text.
    encode_or_decode (str): Specify 'encode' to encrypt or 'decode' to decrypt.

    Returns:
    None: The function prints the encoded or decoded text.
    """
    output_text = ""
    
    # Adjust the shift amount for decoding
    if encode_or_decode == "decode":
        shift_amount *= -1
    
    # Loop through each letter in the original text
    for letter in original_text:
        if letter in alphabet:
            # Find the new position of the letter after shifting
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)  # Ensure the position wraps around the alphabet
            output_text += alphabet[shifted_position]
        else:
            # If the character is not in the alphabet, keep it as is (e.g., spaces, punctuation)
            output_text += letter
    
    # Output the result
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# Loop to keep the program running until the user decides to stop
reset_program = "yes"
while reset_program == "yes":

    # Get the user's choice for encoding or decoding
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    
    # Get the text to be encoded or decoded
    text = input("Type your message:\n").lower()
    
    # Get the shift amount
    shift = int(input("Type the shift number:\n"))

    # Call the Caesar cipher function with the provided inputs
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask if the user wants to run the program again
    reset_program = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
