class Character:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        print(self.name, "is here!")
        print(self.description)

    def set_convo(self, convo):
        self.conversation = convo
    
    def talk(self):
        print(self.conversation, "-", self.name)

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)