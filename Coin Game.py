import random
import time

flip_again = "yes"

while flip_again == "yes" or flip_again == "y" or flip_again == "Yes" or flip_again == "Y":
    print ("\nFlipping the coin...")
    time.sleep(1)

    coin1 = random.randint (1, 2)

    print ("You got:")
    print ("Coin 1 =", coin1)

    flip_again = input ("\nFlip the coin again? (Y/N) ")
    
