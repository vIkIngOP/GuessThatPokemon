import random
prizes_list = ["3 nights stay in OYO","I-Phone 12 pro max","PS 5","1Kg onion","oops! Nothing","A trip to Thailand","Bidi","Khaini","1 Lakh Rupees","Mera KADDU mila hai"]
prizes = random.choice(prizes_list)
Hiddennum = random.randint(1,100)
totalguesses = 10
UsrName = input("*****Welcome to \"GUESS THAT POKEMON\" game*****\nPlease enter your name- ")
print(f"\n--Hey {UsrName}, There is a hidden number which you have to guess, for which you will be getting 10 chances and if you guessed it right you will get rewarded.\n\n+++Don't worry you will be getting hints...GOOD LUCK+++")
input("\n//////PRESS ENTER TO START THE GAME//////")
print("\n-----START-----\nThe Number is between \"1-100\"")


while(True):
    totalguesses = totalguesses-1
    if(totalguesses==-1):
        print(f"\n\noops! you ran out of chances.\nThe hiddden number is--> {Hiddennum}")
        break 
    lft_with = 10-totalguesses
    
    inp1=input()

    if inp1.isalpha():
        print("\nInvalid Input,Try again")

    elif int(inp1)==Hiddennum:
        print(f"\nCongratulations {UsrName} YOU WON and got:",prizes)
        print(f"You cracked the number in just {lft_with} guesses")
        break
        
    elif int(inp1)>Hiddennum:
        print("\nOh No!! the number is SMALLER then what you have entered......Try AGAIN")
        print(f"You are left with {totalguesses} guesses")

    elif int(inp1)<Hiddennum:
        print("\nOh No!! the number is GREATER then what you have entered......Try AGAIN")
        print(f"You are left with {totalguesses} guesses")

exit_ = input("\n\n.....Press ENTER Key to Exit.....") 



    
