import random
def play_game():
    secret_number =random.randint(1,100)
    #to count the number of guesses
    guesses= 0
    #selecting the range
    low=1
    high=100

    print(f' The secret number is,{secret_number}')
    guess =int((high-low)/2)
    while secret_number != guess:
        if guess < secret_number:
            print("Too high")
        elif guess > secret_number:
            print("Too low")
    if guess == secret_number:
        print("game over")
        

