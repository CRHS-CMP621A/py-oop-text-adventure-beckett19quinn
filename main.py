from room import Room

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



while True:
    print("\n")
    current_room.get_details()
    command = input(">> ")
    current_room = current_room.move(command)
