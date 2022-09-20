import random
def play_game():
    secret_number =random.randint(1,100)
    
    guess= None
    
    too_low=1
    too_high=100

    print(f' Shhh, The secret number is,{secret_number}')
    guess =int((too_high-too_low)/2)
    while secret_number != guess:
        if guess < secret_number:
            print("Too high")
        elif guess > secret_number:
            print("Too low")
    if guess == secret_number:
        print("You've got it! game over")
        

