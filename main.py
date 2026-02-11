from room import Room

from item import Item

kitchen = Room('Kitchen')

kitchen.set_description("A bright, colourful room overflowing with dishes.")

dining_room = Room('Dining Room')

dining_room.set_description("A grand dining room, empty with neglect.")

ballroom = Room('Ballroom')

ballroom.set_description("An empty room, yet haunted with a lingering spirit.")

kitchen.link_room(dining_room, 'south')

dining_room.link_room(kitchen,'north')

dining_room.link_room(ballroom, 'west')

ballroom.link_room(dining_room, 'east')

current_room = kitchen

sword = Item('sword')

sword.set_description("A sharp piece of metal with a black handle")

key = Item('key')

key.set_description("An old looking key")

kitchen.add_items('sword', sword)

dining_room.add_items('key', key)

while True:
    print("\n")
    print('You are currently in the', current_room.name)
    print("---------------------")
    current_room.describe()
    current_room.get_details()
    command = input(">> ")
    current_room = current_room.move(command)
