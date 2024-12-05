# Eleonora

from random import shuffle


def villager():
    global npcName
    global response
# Below is a list we can store lots of things in a list and
# then retrieve them later.
    responses = ["Hi", "Are you a hero?", "Are you from this village?"]
    npcNameChoice = ["Dexter", "Ryan", "Dawn", "Andie"]
# Shuffle will shuffle the list contents into a random order
    shuffle(npcNameChoice)
    npcName = npcNameChoice[0]
    print(npcName, ":] Hello, I am ", npcName, " , would you like to talk to me?")
    shuffle(responses)
    answer = input(print("Press y to talk to the villager"))
    if answer == "y":
        print(npcName, ":] ", responses[0])
    else:
        print(npcName, ":] Goodbye")

    if answer.lower() == "n":
        print(npcName, ":]", responses[0])
    else:
        print(npcName, ":] Goodbye")


def chapter_1():
    while True:
        print("Chapter 1: Introduction")
        print("It was a sunny, hot day. At noisy market residents were in anticipation of the upcoming event.")
        options = [
        "1. Interact with locals", "2. Prepare for academy", "3. Stay in hotel", "4. Go to first tour"]
        for option in options:
            print(option)
        choice = input("Choose an option: ")

        if choice == "1":
            print("You interact with locals to find information.")
            villager()
        elif choice == "2":
            print("You prepare for the academy and buy supplies.")
        elif choice == "3":
            print("You find a hotel and rest.")
        elif choice == "4":
            print("You go to the first tour.")
        from chaper2 import chapter_2
        chapter_2()
        break 
chapter_1()
