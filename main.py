# Importing necessary libraries
import os
from pokemontcgsdk import Card

# Function to get card information
def get_card_info(setname, card_number):
    try:
        # Find the card using set name and card number
        res = Card.find(f'{setname}-{card_number}')
        # Return the card number and name
        return f'{card_number} {res.name}'
    except Exception:
        # If card not found, return an error message
        return f'{card_number} Unable to find'

# Main function
def main():
    # Get the deck id from the user
    setname = input("Enter deck id \n> ")
    cards = []

    print("Enter card numbers one by one and press enter. Type done when finished.")

    while True:
        # Get the card number from the user
        card_number = input("> ")
        # Break the loop if the user types 'done'
        if card_number.lower() == "done":
            break

        # Get the card info using the deck id and card number
        card_info = get_card_info(setname, card_number)
        if card_info is not None:
            # Add the card info to the cards list
            cards.append(card_info)

    # Sort the cards list
    cards.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

    # Write the cards info to a text file
    with open('PikaPrint_Output.txt', 'w+') as f:
        f.writelines("Set: " + setname + "\n" + "\n".join(cards))

    print("Would you like to send the file to your default printer? (y/n)")
    # Print the text file if the user types 'y'
    if input('> ').lower() == 'y':
        os.startfile('PikaPrint_Output.txt', "print")

# Run the main function
if __name__ == "__main__":
    main()
