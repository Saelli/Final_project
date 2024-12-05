from random import shuffle

def student():
    global npcName
    global response
# Below is a list we can store lots of things in a list and
# then retrieve them later.
    responses = ["Hi", "Are you a new student?", "Where are you from?"]
    npcNameChoice = ["Dexter", "Ryan", "Dawn", "Andie"]
# Shuffle will shuffle the list contents into a random order
    shuffle(npcNameChoice)
    npcName = npcNameChoice[0]
    print(npcName, ":] Hello, I am ", npcName, " , would you like to talk to me? There are a lot strong students from all over the world")
    shuffle(responses)
    answer = input(print("Press y to talk to the student"))
    if answer == "y":
        print(npcName, ":] ", responses[0])
    else:
        print(npcName, ":] Goodbye")

    if answer.lower() == "n":
        print(npcName, ":]", responses[0])
    else:
        print(npcName, ":] Goodbye")

def chapter_2():
    while True:
        print("Chapter 2: Introduction")
        print("There is a lot of pupils from all over the world came here to pass exam to academy")
    
        options = ["1. Talk with students", "2. First tour, sparring" ]
        for option in options:
            print(option)
        choice = input("Choose an option: ")

        if choice == "1":
            student()
            print("You learn about the academy and influential guests.")
        elif choice == "2":
            print("You are in a 1vs1 sparring match.")
        result = input("Did you win? (yes/no): ")
        if result.lower() == "yes":
            print("You win the match!")
            from chapter3 import chapter_3
            chapter_3()
        else:
            print("You lose and return to Chapter 2.")
            chapter_2()
            break
    else:
        print("Invalid choice. Try again.")
        chapter_2()

chapter_2()