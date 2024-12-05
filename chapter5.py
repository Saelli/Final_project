from random import shuffle


def student():
    global npcName
    global response
# Below is a list we can store lots of things in a list and
# then retrieve them later.
    responses = ["Hi", "Welcome to the academy!", "Do you like it here?"]
    npcNameChoice = ["Dexter", "Ryan", "Dawn", "Andie"]
# Shuffle will shuffle the list contents into a random order
    shuffle(npcNameChoice)
    npcName = npcNameChoice[0]
    print(npcName, ":] Hello, I am ", npcName, " , would you like to talk to me?")
    shuffle(responses)
    answer = input(print("Press y to talk to the student"))
    if answer == "y":
        print(npcName, ":] ", responses[0])
    else:
        print(npcName, ":] Goodbye")

    if answer.lower() == "y":
        print(npcName, ":]", responses[0])
    else:
        print(npcName, ":] Goodbye")

def chapter_5():
    while True:
        print("Chapter 5")
        print("Honored to study at the academy from great sages from all over the world")
        options = [ "1. Gather in dining room", "2. Go to dormitory", "3. Stay" ]
    
        for option in options:
            print(option)
        choice = input("Choose an option: ")

        if choice == "1":
            student()
        elif choice == "2":
            print("You find your room, meet your roommates, and rest.")
        elif choice == "3":
            print("You stay and enjoy the evening.")
            break
        else: print("invalid choice")
        chapter_5

    print("Game continues...")

chapter_5()
