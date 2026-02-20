class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.all_items = {}
        self.character = {}

    

    def set_description(self,room_description):
        self.description = room_description

    def get_descritpion(self):
        return self.description
    
    def get_name(self):
        return self.name
    
    def describe(self):
        print(self.description)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        #print(self.name, 'linked rooms :', repr(self.linked_rooms))

    def get_details(self):
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print('The ' + room.get_name() + ' is', direction)
        for item_obj in self.all_items:
            #item_obj = self.all_items[item_name]
            
            print( "There is a " + item_obj.name + ": " + item_obj.description)
        for char in self.character:
            print( "There is " + self.name)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
    
    def add_items(self, item_obj, item_name):
        self.all_items[item_name] = item_obj

    def remove_item(self, item_name):
        del self.all_items[item_name]

    def get_character(self):
        for i in self.character:
            return i

    def set_character(self,char, char_name ):
        self.character[char_name] = char


        
        
        
    

        
    
            
