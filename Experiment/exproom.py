class Room():
    def __init__(self,name,description,x,y):
        self.name = name
        self.description = description
        self.x=x
        self.y=y
        self.connections = {}

    def add_conections(self, direction, room):
        self.connections[direction] = room


    def get_details(self):
        details = f"You are in the {self.name}."
        details += self.description
        return details



class World():
    def __init__(self):
        self.grid = {}
        self.player_x = 0
        self.player_y = 0

    def add_room(self, room):
        self.grid[(room.x, room.y)] = room

    def get_current_room(self):
        return self.grid.get((self.player_x, self.player_y))
    
    def move_player(self, direction):
        current_room = self.get_current_room()
        if direction in current_room.connections:
            if direction == 'north':
                self.player_y += 1
            elif direction == 'south':
                self.player_y -= 1
            elif direction == 'east':
                self.player_x += 1
            elif direction == 'west':
                self.player_x -= 1
            print("You moved", direction)
        else:
            print("You can't go that way.")

    
