while True:
    try:
        name=input("What is your name? ")
        age=int(input("What is your age? "))
        fav_color=input("What is your favourite colour? ")

        print("Hey " + name + ", how are you?")

        if age < 20:
            print("You are below driving age.")

        elif age < 30:
            print("Ah you are fine, in your 20s.")
            if age < 25:
                print("You are less than 25")
            else:
                print("You are above 25")

        elif age < 40:
            print("Ah I see you are your 30s, might be a good time for a school reunion.")
        else:
            print("All the conditions are false.")

        if fav_color == "blue":
            if age < 20:
                print("Join the blue dragon karate club.")
            elif age < 30:
                print("Join the swimming class.")
                

        if fav_color == "red":
            print("Join the dodge ball club.")

        if fav_color == "yellow":
            print("Join the energy conservation club.")

        if fav_color == "green":
            print("Gardening club")
    except ValueError:
        print("Invlid input")