from room import Room

from item import Item

from character import *



dave = Enemy("Dave", "A smelly zombie")

#dave.describe()

dave.set_convo("What is up dude?")

#dave.talk()

dave.set_weakness("sword")

class_101 = Room("class 101")
class_102 = Room('class 102')
hall_west = Room('west hallway')
hall_east = Room('east hallway')
office = Room("office")
cafeteria = Room('cafeteria')
p_office = Room('principals office')
door = Room('exit')

class_101.link_room(hall_west, 'north')
hall_west.link_room(class_101, 'south')
hall_west.link_room(office, 'north')
hall_west.link_room(hall_east, 'east')
hall_east.link_room(hall_west, 'south')
hall_east.link_room(class_102, 'south')
hall_east.link_room(cafeteria, 'north')
hall_east.link_room(door, 'east')
class_102.link_room(hall_east, 'north')
cafeteria.link_room(hall_east, 'south')
office.link_room(hall_west, 'south')
office.link_room(p_office, 'north')
p_office.link_room(office, 'south')

bob = Character('Bob', 'A 500 pound boy, sitting infront of the office door.')
bob.set_convo("I ain't moving unless it's for a cookie")

current_room = class_101

sword = Item('sword')

sword.set_description("A sharp piece of metal with a black handle")

key = Item('key')

key.set_description("An old looking key")





while True:
    print('You are currently in the', current_room.name)
    print("---------------------")
    current_room.describe()
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        person = 1
    command = input(">> ")
    if command in ['north','south','east','west']:
        current_room = current_room.move(command)
    elif command == 'talk':
        bob.talk()
    
        
    elif command == 'help':
        print("Move command: north, east, south, west. Fight")

    
