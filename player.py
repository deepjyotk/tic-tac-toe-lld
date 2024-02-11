# create a player class which has player name, and piece(X,Y)
# class Player:
#     def __init__(self, name, piece):
#         self.name = name
#         self.piece = piece

#     def get_name(self):
#         return self.name

#     def get_piece(self):
#         return self.piece


class Player:
    def __init__(self, playerBuilder):
        self.name = playerBuilder.name
        self.piece = playerBuilder.piece

    def get_name(self):
        return self.name
    
    def get_piece(self):
        return self.piece
    

class PlayerBuilder:
    def __init__(self):
        self.name = None
        self.piece = None
        
    
    def set_name(self, name):
        self.name = name
        return self
    
    def set_piece(self, piece):
        self.piece = piece
        return self
    
    def build(self):
        return Player(self)
    
class PlayerCreator:
    
    def __init__(self, playerBuilder: PlayerBuilder):
        self.playerBuilder = playerBuilder
    
    def createPlayerWithX(self,name):
        return self.playerBuilder.set_name(name).set_piece("X").build()
    
    def createPlayerWithO(self,name):
        return self.playerBuilder.set_name(name).set_piece("O").build()
    
    
