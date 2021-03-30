def goFloor(inpFloor, currentFloor):
    if currentFloor > inpFloor:
        print("Going Down!!!! WOOOOOOOH")
        while currentFloor != inpFloor:
            currentFloor -= 1
            print("Floor: ", currentFloor)
        return currentFloor
    elif currentFloor < inpFloor:
        print("Going Up!!!! WEEEEEEEEEH")
        while currentFloor != inpFloor:
            currentFloor += 1
            print("Floor: ", currentFloor)
        return currentFloor
    else:
        print("You are already on that floor")
        return currentFloor


'''def goDown(inpFloor, currentFloor)
    while currentFloor!= inpFloor


def goUp(inpFloor, currentFloor)
'''


currentFloor = 1
while True:
    print("\n\nWelcome to the lift 20 Floors!! Press 0 anytime to exit the lift")
    try:
        inpFloor = eval(input("Enter the floor you want to go to: "))
    except:
        print("Invalid Entry!! Try Again")
        continue
    if inpFloor == 0:
        print("Have Fun!!! BYEEEEEEE")
        break
    if inpFloor > 20:
        print("OOPS!! This building has only 20 floors!! Try again")
        continue
    print("Currently you are on floor:", currentFloor)
    currentFloor = goFloor(inpFloor,currentFloor)
    print("You have reached your Destination Floor: ", currentFloor)
    