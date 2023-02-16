"""Gives a Player One Shot At Guessing the Correct Secret Word"""

__author__ = "730576359"

# secret word is "haters"

secret: str = input("What is your 6-letter guess? ")
correct: str = "python"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

six_letters: bool = True

boxes: str = ""

while six_letters:
    if len(secret) == len(correct):
        # six_letters = False
        if secret == correct:
            a: int = 0
            while a <= 5:
                if secret[a] == correct[a]:
                   boxes = boxes + GREEN_BOX
                a = a + 1
            print(boxes)
            print("Woo! You got it!")
            exit()
        else:
            a = 0
            
            while a <= 5:
                if secret[a] == correct[a]:
                    boxes = boxes + GREEN_BOX
                 
                else:
                    b: int = 0
                    letter_elsewhere: bool = False
                    while b <= 5:
                        if secret[a] == correct[b]:
                            letter_elsewhere = True
                        b += 1
                    
                    if letter_elsewhere:
                        boxes += YELLOW_BOX
                    else:
                        boxes = boxes + WHITE_BOX
               
                a = a + 1
            print(boxes)
            print("Not quite. Play again soon!")
            exit()

    else:
        new_guess = input("That was not 6 letters! Try again: ")
        six_letters = True
    if len(new_guess) == len(correct):
        if new_guess == correct:
            a = 0
            
            while a <= 5:
                if new_guess[a] == correct[a]:
                    boxes = boxes + GREEN_BOX
                 
                
               
                a = a + 1
            print(boxes)
            print("Woo! You got it!")
            exit()
        else:
            
            x = 0
            
            while x <= 5:
                if new_guess[x] == correct[x]:
                    boxes = boxes + GREEN_BOX
                 
                else:
                    
                    b: int = 0
                    letter_elsewhere: bool = False
                    while b <= 5:
                        if new_guess[x] == correct[b]:
                            letter_elsewhere = True
                        b += 1
                    
                    if letter_elsewhere:
                        boxes += YELLOW_BOX
                    else:
                        boxes = boxes + WHITE_BOX
               
                x = x + 1
            print(boxes)
            print("Not quite. Play again soon!")
            exit()