import pet
import time


pet_name = input("Enter your pet's name: ")
pet = pet_name

game_on = True
while game_on == True:
    print("What would you like to do with", str(pet.name) + "?")
    print("1. Feed")
    print("2. Play")
    print("3. Sleep")
    print("4. Check status")
    print("5. Earn coins")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        pet.feed()
    elif choice == "2":
        pet.play()
    elif choice == "3":
        pet.sleep()
    elif choice == "4":
        pet.check_status()
    elif choice == "5":
        pet.earn_coins()
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

    # Decrease bars every iteration
    pet.hunger += 5
    pet.sleepiness += 5
    if pet.hunger >= 100:
        print(pet.name + " is hungry! Feed it.")
    if pet.sleepiness >= 100:
        print(pet.name + " is sleepy! Let it sleep.")
    time.sleep(2)


