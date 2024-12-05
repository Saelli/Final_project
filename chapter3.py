def chapter_3():
    print("Chapter 3.")
    print("Only half of the students remained, and they were expecting that only a 1/3rd of them would pass this year.")

    options = ["1. Decide how to pass", "2. Go to north", "3. Go to south"]
    for option in options:
        print(option)
    choice = input("Choose an option: ")

    if choice == "1":
        print("You need 30 points to pass. Groups make 3 points each; solo earns 5 points per monster.")
    elif choice == "2":
        print("You go north to fight the boss.")
        result = input("Did you fight alone? (yes/no): ")
        if result.lower() == "yes":
            print("You earn 30 points and move to Chapter 4.")
            from chapter4 import chapter_4
            chapter_4()
        else:
            print("Group earns 25 points. Go south to gain points.")
            chapter_4()
    elif choice == "3":
        print("You go south to fight mobs and earn 30 points.")
        from chapter5 import chapter_5
        chapter_5()
    else:
        print("Invalid choice. Try again.")
        chapter_3()

chapter_3()