import random

score = 0  
round = 0


while True:
    round +=1
    
    player = random.randint(1, 100)
    computer = random.randint(1, 100)
    print(f"Round {round}")
    print(f"Your number is {player}")
    
    
    guess = input("Do you think your number is higher, lower, or equal to the computer's? (type 'quit' to exit): ").lower()

   
    if guess == 'quit':
        print("Thanks for playing! \nGood job, you played really well!")
        break

    
    if (guess == "higher" and player > computer) or (guess == "lower" and player < computer):
        print(f"You were right! The computer's number was {computer}")
        score += 1
        print(f"Your score is now {score}")
    elif guess == "equal" and player == computer:
        print(f"Good guess! The numbers are equal. The computer's number was also {computer}")
        score += 1
        print(f"Your score is now {score}")
    else:
        print(f"You lose! The computer's number was {computer}")
        score-=1
        print(f"Your score is now {score}")

    
    print("-" * 30)
