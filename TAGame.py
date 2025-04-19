import time

print('================================================================')
print('Welcome in TerminalAdventer Game by qomel')
print('================================================================')

# Define the available rooms
rooms = {
    'start': {
        'description': 'You are in the entrance of a mysterious cave. A glowing torchlight illuminates the path ahead.', # Description of the room
        'exits': {'north': 'dark_room', 'east': 'treasure_room'}, # Possible moves to north, east
        'monsters': None, # List of monesters in the room
        'items': None, # List of items in the room
    },
    'dark_room': {
        'description': 'You are in a dark, narrow room. The walls are adorned with ancient, intricate carvings. There is a passage to your left and a door to your left.',
        'exits': {'south': 'start', 'west': 'ice_room'},
        'monsters': None,
        'items': 'magic_sword'
    },
    'ice_room': {
        'description': 'You are in an icy room. The floor is covered in crystalline formations. You can see a monster in the corner',
        'exits': {'east': 'dark_room'},
        'monsters': ('Ice demon'),
        'items': 'icy_sword'
    },
    'treasure_room': {
        'description': 'You are in a treasure room. A massive chest lies open, containing a precious artifact.',
        'exits': {'west': 'start'},
        'monsters': None,
        'items': 'golden_treasure'
    }
}   

# Status of player - stores the placement of the player and his inventory

player = {
    'current_room': 'start',
    'inventory': [],
    'monsters_defeated': False
}

def show_description(room):
# Shows description of the current room
    print("\n" + rooms[room]['description'] + "\n")

    if 'monsters' in rooms[room]: # If there is a monster
        print(f"Monsters in this room: {rooms[room]['monsters']}!\n")
    
    if rooms[room]['items']: # If there is a items
        print(f"You see a item in this room: {rooms[room]['items']}!\n")

def move_player(direction):
# Movment of player
    current_room = player['current_room'] # Taken a current room

    if direction in rooms[current_room]['exits']: # If direction is in exits
        player ['current_room'] = rooms[current_room]['exits'][direction]
    
    else: # If there isn't a possible move
        print("You can't go that way!\n")

def pick_item():
# Picking items from room
    current_room = player['current_room'] # Taken a current room
    items = rooms[current_room].get('items') # Taken a possible item 

    if items: # If there is an item
        print(f"You pick {items}!")
        player['inventory'].append(items) # Add item to eq
        rooms[current_room]['items'] = None # Remove item from room 
    else:
        print("There is no item here\n!")

def fight_monsters():
# Fighting monsters in room
    current_room = player['current_room'] # Taken a current room
    if 'monsters' in rooms[current_room]:
        if 'magic_sword' in player['inventory']: # Chceck if player has magic_sword in inventory
            print(f"You defeted {rooms[current_room]['monsters']}")
            del rooms[current_room]['monsters'] # Delete monster from room
            player['monsters_defeated'] = True # You defeated a monster
        else:
            print("You don't have a weapon here! You DIED :(\n")
            time.sleep(1)
            exit()
    else:
        print("There is no monster here!\n")

while True:
# Loop for whole game
    show_description(player['current_room'])
    
    # Take command from player
    
    command = input("What you what to do?\nMOVE [direction]| PICK | FIGHT | QUIT\nDirection: North, South, East, West)")


    if command.startswith('move'):
        _, direction = command.split()
        move_player(direction)
        time.sleep(1)
    elif command == 'pick':
        pick_item()
        time.sleep(1)
    elif command == 'fight':
        fight_monsters()
        time.sleep(1)
    elif command == 'quit':
        print("Goodbye!")
        break
    else:
        print("I don't understand that command.")

    if 'golden_treasure' in player['inventory'] and player['monsters_defeated']:
        print("Congratulations! You have found the golden treasure and defeat monsters!")
        break