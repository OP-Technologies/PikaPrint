import os
from pokemontcgsdk import Card

def get_card_info(setname, card_number):
    try:
        res = Card.find(f'{setname}-{card_number}')
        return f'{card_number} {res.name}'
    except Exception:
        return f'{card_number} Unable to find'

def main():
    setname = input("Enter deck id \n> ")
    cards = []

    print("Enter card numbers one by one and press enter. Type done when finished.")

    while True:
        card_number = input("> ")
        if card_number.lower() == "done":
            break

        card_info = get_card_info(setname, card_number)
        if card_info is not None:
            cards.append(card_info)

    cards.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

    with open('PikaPrint_Output.txt', 'w+') as f:
        f.writelines("Set: " + setname + "\n" + "\n".join(cards))

    print("Would you like to send the file to your default printer? (y/n)")
    if input('> ').lower() == 'y':
        os.startfile('PikaPrint_Output.txt', "print")

if __name__ == "__main__":
    main()
