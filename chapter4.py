def chapter_4():
    while True:
        print("Chapter 4")
        print("The north of the forest was a steep mountain and under was a cave with an ancient monster")
        options = [ "1. Fight with a boss", "2. Use a key to open the door"]
        for option in options:
            print(option)
        choice = input("Choose an option: ")

        if choice == "1":
            print("You fight the boss and earn points.")
        elif choice == "2":
            print("You use the key to open the door and proceed.")
        from chapter5 import chapter_5
        chapter_5()
        break

    

chapter_4()