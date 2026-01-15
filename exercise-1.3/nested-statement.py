number_of_oranges = int(input("How many oranges do you have?: "))

if number_of_oranges > 0:
    print("You have some oranges.")

    if number_of_oranges > 50:
        print("But you've got way too many!")
    else:
        # This only runs if oranges > 0 AND NOT > 50
        print("Just the right number of oranges.")

else:
    print("You have no oranges.")