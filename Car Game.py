started = False
stopped = True

while True:
    command = input(">: ").lower()

    if command == "help":
        print("""
Start - starts the car
Stop - stops the car
Quit - quits the game
              """)
        
    elif command == "start":
        if started:
            print("Car is already started.")
        else:
            started = True
            stopped = False
            print("Car started...")

    elif command == "stop":
        if stopped:
            print("Car is already stopped.")
        else:
            stopped = True
            started = False
            print("Car stopped.")
        
    elif command == "quit":
        break

    else:
        print("I don't understand that...")