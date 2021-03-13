
print("Hi Lets play a game")

counter = 1
lucky_num = 65
fact = 0
while counter <= 5:
    print("Enter " , counter , "number ")
    lucky_num_guess = eval(input("Enter: "))
    if lucky_num_guess == lucky_num:
        print("Good Guess")
        fact = 1
        break                                              #ques11 modification
    else:
        print("Try again")
    counter += 1

if fact == 0:
    print("Sorry but that was not very successful!")
print("Game over!")
    

