import random

print('''
Welcome to "Find The Treassure"! Move around the house to find the treassure,
or enter "Q" to quit.
''')
# descriptioins of the rooms
lobby_description = '''This room is the lobby.
There is a set of stairs to the North leading to a door, and other two doors:
one to the East, and one to the West'''
dinningroom_description = '''This is teh dinning room.
There is a big table in the middle of the room, a door to the East,
and another door on the North side.'''
kitchen_description = '''You are now in the kitchen.
There is a huge gas stove in the middle of the room with pans and
pots hanging over it. The pantry is at the North side.
There is a door on the South side'''
livingroom_description = '''This is the living room.
There are many couches and seats. Ther is a piano on the far West of the room,
and a small book shelf to the South.
There are 2 doors, one to the West and another one to the North.'''
library_description = '''This room is the library.
There are huge book shelves Covering the East, North and West sides of the room.
Light comes in from a round glass window in the ceiling.
The only door is on the South wall.'''
bedroom_description = '''This is the bedroom.
There is a big bed with a wooden frame at the East side.
The room is full of big windows, decorated with light,
translucid white courtines. To the south, the only door.'''
rooms_dict = {"Lobby": lobby_description, "Dinningroom": dinningroom_description, "Kitchen": kitchen_description, "Livingroom": livingroom_description, "Library": library_description, "Bedroom": bedroom_description}
rooms = ["Lobby", "Dinningroom", "Kitchen", "Livingroom", "Library", "Bedroom"]

treassure = random.randint(1,6) # sets a random location for the treassure

#check the player's location
x = 0
def player_is_in(this_room):
        if this_room == rooms[x]:
            return True
        else:
            return False

# run the game as long as the player is not in the same room as the treassure
while x != treassure:
    if player_is_in("Lobby"):
        print(rooms_dict["Lobby"])
        move = input("Choose a door [N, E, W]: ").capitalize()
        if move == "N":
            x = 5
        elif move == "E":
            x = 3
        elif move == "W":
            x = 1
        elif move == "Q":
            break
        else:
            print("Invalid choice, Try again.")
    elif player_is_in("Dinningroom"):
        print(rooms_dict["Dinningroom"])
        move = input("Choose a door [N, E]: ").capitalize()
        if move == "N":
            x = 2
        elif move == "E":
            x = 0
        elif move == "Q":
            break
        else:
            print("Invalid choice, Try again.")
    elif player_is_in("Kitchen"):
        print(rooms_dict["Kitchen"])
        move = input("You can only go to the south door [S]: ").capitalize()
        if move == "S":
            x = 1
        elif move == "Q":
            break
        else:
            print("Invalid choice, Try again.")
    elif player_is_in("Livingroom"):
        print(rooms_dict["Livingroom"])
        move = input("Choose a dooor [N, W]: ").capitalize()
        if move == "N":
            x = 4
        elif move == "W":
            x = 0
        elif move == "Q":
            break
        else:
            print("Invalid choice, Try again.")
    elif player_is_in("Library"):
        print(rooms_dict["Library"])
        move = input("You can only go south [S]: ").capitalize()
        if move == "S":
            x = 3
        elif move == "Q":
            break
        else:
            print("Invalid choice, Try again.")
    elif player_is_in("Bedroom"):
        print(rooms_dict["Bedroom"])
        move = input(" You can only go south [S]: ").capitalize()
        if move == "S":
            x = 0
        elif move == "Q":
            break
        else:
            print("Invalid choice, Try again.")
    else:
        print('''I have no idea where you are. You may have discovered
        a new dimension!''')
        break
if x == treassure:
    print('''You have found the hidden treassure! It's an empty box.
    You stare at the box for a few seconds, only to realize that
    the treassure was inside you all along.''')
