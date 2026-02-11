from exproom import World
from exproom import Room


game_world = World()

room_0_0 = Room('Entryway','A split entrance staircase with high ceilings and lots of natural light.', 0,0)
room_0_1 = Room('Upstairs hallway', 'A long narrow hallway littered with family pictures', 0, 1)


game_world.add_room(room_0_0)
game_world.add_room(room_0_1)

room_0_0.add_conections('north', room_0_1)

