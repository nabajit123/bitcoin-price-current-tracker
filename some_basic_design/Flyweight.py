# here for one character obj should not be more than one.

class Character:
    def __init__(self, char):
        self.char = char

    def draw(self, position):
        print(f"Drawing {self.char} at position {position}.")

class CharacterFactory:
    def __init__(self):
        self.characters = {}

    def get_character(self, char):
        if char not in self.characters:
            self.characters[char] = Character(char)
        return self.characters[char]


factory = CharacterFactory()

characters = [
    factory.get_character('h'),
    factory.get_character('e'),
    factory.get_character('l'),
    factory.get_character('l'),
    factory.get_character('o')
]

positions = [0, 1, 2, 3, 4]

for char, position in zip(characters, positions):
    char.draw(position)



# ++ Outputs
# Drawing h at position 0.
# Drawing e at position 1.
# Drawing l at position 2.
# Drawing l at position 3.
# Drawing o at position 4.
#In this example, we have a Character class that represents a single character in a document. The Character class has an intrinsic state that consists of the character itself (i.e., the letter or symbol), and an extrinsic state that consists of the character's position in the document.

#We also have a CharacterFactory class that is responsible for creating and sharing instances of Character objects. The CharacterFactory maintains a dictionary of characters that have already been created and returns an existing character if it already exists in the dictionary. This way, we avoid creating duplicate instances of characters and conserve memory.