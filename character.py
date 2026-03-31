class Character:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.inventory = None

    def describe(self):
        print(self.name, "is here!")
        print(self.description)

    def set_convo(self, convo):
        self.conversation = convo
    
    #def talk(self):
        #print(self.conversation, "-", self.name)

    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self):
        print(self.name, "doesn't want to fight.")

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_weakness(self):
        print(self.name, 'weakness:', self.weakness)
        
    def fight(self, combat_item):
        
        if combat_item == self.weakness:
            print("You stopped", self.name, ' with', self.weakness)
            return True
        else:
            print(self.name, 'crushes you!')
            return False