

print(" Hi Welcome to Lucky Number Game")

number = 65
answer = "yes"
while True:
    inp_number = eval(input("Please input number to guess: "))
    if inp_number == number:
        print(" Conratulations, You guessed it right ")
        break
    else:
        print(" Wrong No: keep guessing!")
        answer = input("Do you want to continue? Answer Yes or No: ")
        if answer == "no":
            print("You are out as you chose not to continue")
            break
        continue
