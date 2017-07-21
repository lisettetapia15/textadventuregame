from sys import exit
#def main(s):
#    global killer2_alive
#    global killer_alive
#    global knife
#    killer2_alive = True
#    killer_alive = True
#    knife = False

#main()

# Variables
killer_alive = True
killer2_alive = True
knife = False

# Starting room 1 code
def room_1():
    print ("You wake up to find yourself in a big white room with blood covered walls. You have no clue how you got here but you have bleeding wound on your forehead. It's really dark, suprisingly, and all you can see are three doors.")
    print ("One leads east, another north and the last one leads west. Which direction do you go?")

    choice = raw_input(" > ");

    if "west" in choice:
        room_2()

    elif "north" in choice:
        room_4()

    elif "east" in choice:
        game_over("You head out and walk through a narrow hallway. After walking for a few minutes, you seem to be lost. You try to turn around but before you even could, someone knocks you out and ended up killing you. You died trying.. well were you even trying?")

    else:
        room_1()

# Room 2 Code
def room_2():
    print ("You enter another room and it has a low ceiling so you had to crouch to walk. Once the ceiling stopped being low, you see a passage leading west and another leading north. On the very far end of the first passage, you see a bright light. The second one, a really horrible smell comes from there. There's a third passage to east and it leads to the very first room you were in.")
    print ("What do you do?")

    choice = raw_input(" > ");

    if "west" in choice:
        game_over("You follow the bright path that is appearing from the west door. As you walk further, the light starts getting brighter and brighter until it's too blinding that you can't see anything. You fall to the floor only it wasn't the floor but you fell on sharp knives that were all glued together and point up. You died because the knives were stabbing you everywhere.")

    elif "north" in choice:
        room_3()

    elif "east" in choice:
        room_1()

    else:
        room_2()

# Room 3 code
def room_3():

    global killer2_alive
    global knife

    if killer2_alive:
        print ("As you walk into the room, you start to understand where the smell came from. The floor was covered with rotting corpses. Suddenly you hear a sickening laugh and it's a tall man with a white mask covering his face but he hasn't made a move just observes you. You quickly check your surroundings and see a passage to the east, a flaming torch on the ground and a corspe holding a knife and a hole on the far side of the room. The passage to the south leads to the second room.")
        print ("What do you do?")

        choice = raw_input(" ss> ")

        if "east" in choice:
            game_over("You run towards the east room but you were too slow and the tall masked killer grabs you and says, 'Better luck next time' and stabbed you repeatedly.")

        elif "torch" in choice:
            print("You take the flaming torch and throw it on the killer. The fire overtakes him and he stumbles and falls in the hole, disappearing from the room screaming.")
            killer2_alive = False
            room_3()

        elif "knife" in choice:
            print ("You take the knife and suddenly you feel unbeatable. With courage, you jump forward and kill the killer.")
            killer2_alive = False
            knife = True
            room_3()

        elif "hole" in choice:
            game_over("You jump in the dark hole suddenly feeling like it wasn't such a great idea. After a few days, you still kept falling never hitting a floor and you end up dying a few days later without food or water in your system.")

        elif "south" in choice:
            room_2()

        else:
            room_3()

# Room 4 Code
def room_4():
    global killer_alive

    if killer_alive:
        print ("The room you enter is huge and breathtaking but it is for a good reason because this room belongs to the actual main killer who brought you here. You thought that the killer you killed was the only one but there are two killers and you just killed one that was weaker than this one.")

    if knife:
        print ("Suddenly your knife starts to shine. Some weird force encourages you to leap forward and stab the killer right in the heart. He dies with loud horrifying screams.")
        killer_alive = False
        room_4()

    else:
        game_over("The killer leaps in front of you before you can do anything and stabs you in the heart.")

# Game Over
def game_over():

    global killer2_alive
    global killer_alive
    global knife

    killer2_alive = True
    killer_alive = True
    knife = False

answer = raw_input("Restart?")
if answer == "Yes":
    print("Leaving the game")
    sys.exit(0) # import sys module
elif answer == "No":
    print("Starting new game")
    game()
