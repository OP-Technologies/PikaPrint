# PikaPrint
PikaPrint is a useful utility for Pokemon TCG collectors. It allows you to input a list of owned Pokemon cards in a set (e.g. all cards owned in Sword & Shield: Astral Radiance) and sort them into numerical order, fetch the name of the Pokemon associated with each card and store them into a text file for easy printing.

## Features
- Enter deck ID & list of card IDs
- Automatically fetch the name of each Pokémon
- Sort list into numerical order
- Save list into a text file

## Download
To download PikaPrint, head to the releases section of this GitHub repository.

## How to Use
1. **Start the Program:** Run the executable file to start the program.
2. **Enter the Deck ID:** The program will prompt you to enter a deck ID. This should be the ID of the deck you want to get card information from.
3. **Enter Card Numbers:** After entering the deck ID, the program will ask you to enter card numbers one by one. After entering each card number, press enter to submit it. Continue this process until you have entered all the card numbers you are interested in.
4. **Finish Entering Card Numbers:** Once you have entered all the card numbers, type ‘done’ and press enter. This will signal the program that you have finished entering card numbers.
5. **Create Output File:** The program will then create a text file named ‘PikaPrint_Output.txt’. This file will contain the card numbers and names of the cards from the deck you specified, sorted in ascending order of card number. You can find this file in the same directory as the executable.
6. **Print the Output File:** Finally, the program will ask if you want to send the file to your default printer. If you want to print the file, type ‘y’ and press enter. If you do not want to print the file, type ‘n’ and press enter.

## Obtaining Deck IDs
If you are unsure of what a deck ID is, or where to find the correct one, you're in the right place.
1. Go to the [TCG Guru](https://pokemontcg.guru/sets) website.
2. Click on the set you are going to be working with.
3. Copy the last part of the URL. For example, the deck ID for https://pokemontcg.guru/set/astral-radiance/*swsh10* would be *swsh10*.

## Known Limitations & Bugs
- Cards in Trainer Galleries will have separate deck IDs, so you will have to process them separately. When processing these, **DO NOT** include the letters at the beginning of the card ID.
- If you accidentally submit a card ID with letters in it, the whole program will crash! We would recommend using the number pad, if your computer has one.
- If the executable file will not work, you may need to install Python on your system, as well as the required Python packages listed in [requirements.txt](https://github.com/OP-Technologies/PikaPrint/main/requirements.txt).

## Contributions
If you feel like you could improve this program, please feel free to add features or improve the code & open a pull request!

## License
PikaPrint © 2023 by OP Technologies is licensed under CC BY-NC-SA 4.0 